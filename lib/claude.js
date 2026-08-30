// Raw Anthropic /v1/messages client — vision only, zero dependencies.
//
// Auth: ANTHROPIC_API_KEY if present, otherwise the Claude Code subscription OAuth token
// seeded read-only at /seed/.credentials.json (the reseed-daemon on the host rotates it
// every few hours, so the file is re-read on every request, never cached).
// OAuth mode REQUIRES the exact Claude Code identity line as the system prompt — without it
// the API answers 429 rate_limit_error on every call. Task instructions go in the user turn.
// (Same contract as travel-serve's app/claude_client.py, which this is ported from.)
const fs = require('fs');

const API_URL = 'https://api.anthropic.com/v1/messages';
const OAUTH_SYSTEM = "You are Claude Code, Anthropic's official CLI for Claude.";
const CREDS = process.env.CLAUDE_CREDS_PATH || '/seed/.credentials.json';

const model = () => process.env.REZ_CLAUDE_MODEL || 'claude-opus-5';

class ClaudeAuthError extends Error {}
class ClaudeError extends Error {}

function credsStatus() {
  if (process.env.ANTHROPIC_API_KEY) return { mode: 'api_key', present: true };
  try {
    const st = fs.statSync(CREDS);
    return { mode: 'oauth', present: true, age_s: Math.round((Date.now() - st.mtimeMs) / 1000) };
  } catch {
    return { mode: 'oauth', present: false };
  }
}

function authHeaders() {
  if (process.env.ANTHROPIC_API_KEY) {
    return [{ 'x-api-key': process.env.ANTHROPIC_API_KEY }, false];
  }
  let token;
  try {
    token = JSON.parse(fs.readFileSync(CREDS, 'utf8')).claudeAiOauth.accessToken;
  } catch (e) {
    throw new ClaudeAuthError(`no Claude credentials at ${CREDS}: ${e.message}`);
  }
  return [{ authorization: `Bearer ${token}`, 'anthropic-beta': 'oauth-2025-04-20' }, true];
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

/** One user turn. `content` is a string or a list of content blocks. Returns the joined text. */
async function messages(content, { maxTokens = 4000, timeoutMs = 180000 } = {}) {
  if (typeof content === 'string') content = [{ type: 'text', text: content }];
  const [auth, isOauth] = authHeaders();
  const body = { model: model(), max_tokens: maxTokens, messages: [{ role: 'user', content }] };
  if (isOauth) body.system = OAUTH_SYSTEM;

  let last;
  for (let attempt = 0; attempt < 3; attempt++) {
    let r;
    try {
      r = await fetch(API_URL, {
        method: 'POST',
        headers: { 'anthropic-version': '2023-06-01', 'content-type': 'application/json', ...auth },
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(timeoutMs),
      });
    } catch (e) {
      last = new ClaudeError(`network error calling Claude: ${e.message}`);
      await sleep(2000 * (attempt + 1));
      continue;
    }
    if (r.status === 401) {
      throw new ClaudeAuthError('Claude API 401 — the seeded token expired; reseed it on the host');
    }
    if ([429, 500, 502, 503, 529].includes(r.status)) {
      last = new ClaudeError(`Claude API ${r.status}: ${(await r.text()).slice(0, 300)}`);
      await sleep(4000 * (attempt + 1));
      continue;
    }
    if (!r.ok) throw new ClaudeError(`Claude API ${r.status}: ${(await r.text()).slice(0, 500)}`);
    const data = await r.json();
    if (data.stop_reason === 'refusal') throw new ClaudeError('Claude declined to read this image');
    return (data.content || []).filter(b => b.type === 'text').map(b => b.text).join('');
  }
  throw last || new ClaudeError('Claude call failed');
}

function imageBlock(base64, mediaType = 'image/jpeg') {
  return { type: 'image', source: { type: 'base64', media_type: mediaType, data: base64 } };
}

/** First balanced {...} object in a reply (models like to wrap JSON in prose or fences). */
function extractJson(text) {
  const start = text.indexOf('{');
  if (start < 0) return null;
  let depth = 0, inStr = false, esc = false;
  for (let i = start; i < text.length; i++) {
    const c = text[i];
    if (esc) { esc = false; continue; }
    if (c === '\\') { esc = true; continue; }
    if (c === '"') { inStr = !inStr; continue; }
    if (inStr) continue;
    if (c === '{') depth++;
    else if (c === '}' && --depth === 0) {
      try { return JSON.parse(text.slice(start, i + 1)); } catch { return null; }
    }
  }
  return null;
}

module.exports = { messages, imageBlock, extractJson, credsStatus, model, ClaudeAuthError, ClaudeError };
