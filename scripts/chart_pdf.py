#!/usr/bin/env python3
"""Rolling chart+chat PDF — the token-free memory of the exit advisor.

ONE PDF (data/advisor/charts.pdf). One consult = one section, headed by its id and UTC
timestamp, containing EVERYTHING about that chart in chronological order: the first picture,
the notebook's verdict, any follow-up picture the trader draws questions on, and every message
either side sent. Follow-up pictures stay inside the same section — same id, same discussion —
which is what tells NotebookLM they are the same position, not a new one.

The whole file is rebuilt from data/advisor/consults.json on every change, so upload, chat and
erase all go through one path; the rebuilt PDF then replaces the single "REZSABM chart uploads"
source in the notebook.

Usage: chart_pdf.py sync   -> rebuild charts.pdf from consults.json, print JSON
"""
import json
import os
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, 'data', 'advisor')
PDF = os.path.join(DIR, 'charts.pdf')
CONSULTS = os.path.join(DIR, 'consults.json')
RAW = os.path.join(DIR, 'raw')

MAX_CONSULTS = int(os.environ.get('REZ_MAX_CHART_PAGES', '40'))
W = 1600                     # page width; pictures are scaled into it
HEADER_H = 104
PAD = 24
LINE_H = 26
PAGE_MAX_H = 2600            # split a long section into continuation pages


def font(size, bold=False):
    base = '/usr/share/fonts/truetype/dejavu/DejaVuSans'
    try:
        return ImageFont.truetype(f'{base}-Bold.ttf' if bold else f'{base}.ttf', size)
    except OSError:
        return ImageFont.load_default()


F_TITLE, F_META, F_ROLE, F_BODY = font(30, True), font(21), font(21, True), font(20)


def _ascii(t):
    """NLM answers are full of box-drawing and emoji that add nothing to a printed transcript
    (and break PIL's fallback bitmap font outright)."""
    return ''.join(c if ord(c) < 0x2500 else ' ' for c in t)


def wrap(text, chars=150):
    out = []
    for para in _ascii(text).replace('\r', '').split('\n'):
        out.extend(textwrap.wrap(para, chars) or [''])
    return out


def load_picture(name):
    p = os.path.join(RAW, name)
    if not os.path.exists(p):
        return None
    im = Image.open(p)
    if getattr(im, 'n_frames', 1) > 1:
        im.seek(0)
    im = im.convert('RGB')
    if im.width != W - 2 * PAD:
        w = W - 2 * PAD
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    return im


def walk_block(consult):
    """The guided walk drawn as the tree it is: each question, the trader's answer indented one
    step further, then the rule the course's tree lands on. This is what makes the PDF a
    decision database rather than a pile of screenshots."""
    w = consult.get('walk')
    if not w:
        return []
    state = 'IN PROGRESS' if w.get('inProgress') else 'COMPLETED'
    rows = [('role', f"SABM DECISION TREE ({state}) — the trader walked the course's own questions")]
    for i, p in enumerate(w.get('path', [])):
        pad = '  ' * i
        rows.append(('body', f'{pad}|- {p.get("q", "")}'))
        unit = f' {p.get("unit")}' if p.get('kind') == 'number' and p.get('unit') else ''
        rows.append(('body', f'{pad}|  ANSWER: {p.get("answer", "")}{unit}'))
    pad = '  ' * len(w.get('path', []))
    if w.get('inProgress'):
        rows.append(('body', f'{pad}=> (walk not finished — no rule reached yet)'))
        rows.append(('body', ''))
        return rows
    rows.append(('body', f'{pad}=> RULE (provisional, from the local spine): {w.get("rule", "")}'))
    for ln in wrap(f'{pad}   EXIT: {w.get("exit", "")}'):
        rows.append(('body', ln))
    if w.get('quote'):
        for ln in wrap(f'{pad}   COURSE: "{w["quote"]}"'):
            rows.append(('body', ln))
    if w.get('reading'):
        rows.append(('role', 'THE NOTEBOOK READ THE SAME QUESTIONS FROM THE PICTURE AS'))
        rows.extend(('body', ln) for ln in wrap(w['reading']))
    rows.append(('body', ''))
    return rows


def blocks_for(consult):
    """The whole section as a flat block list: pictures, the decision walk and text, in order."""
    blocks, shot = [], 0
    for t in consult.get('turns', []):
        if t.get('image'):
            shot += 1
            im = load_picture(t['image'])
            label = f"PICTURE {shot} — uploaded {t.get('at', '')} UTC"
            # label + picture are ONE block: a page break between them stranded the caption
            blocks.append(('shot', (label, im)) if im else ('body', f'{label} [picture missing]'))
        if (t.get('text') or '').strip():
            who = 'TRADER' if t['role'] == 'user' else 'SABM NOTEBOOK'
            blocks.append(('role', f"{who} — {t.get('at', '')} UTC"))
            blocks.extend(('body', ln) for ln in wrap(t['text']))
        blocks.append(('body', ''))
    blocks = walk_block(consult) + blocks if consult.get('walk') else blocks
    return blocks or [('body', '(no exchange yet)')]


def height(block):
    kind, val = block
    if kind == 'shot':
        return LINE_H + val[1].height + 8
    return LINE_H


def render_page(consult, blocks, cont):
    h = HEADER_H + PAD + sum(height(b) for b in blocks) + PAD
    page = Image.new('RGB', (W, h), 'white')
    d = ImageDraw.Draw(page)
    d.text((PAD, 14), _ascii(f"CHART UPLOAD {consult['id']}{'  (continued)' if cont else ''}"),
           fill='black', font=F_TITLE)
    d.text((PAD, 52), _ascii(f"opened {consult['when']} UTC"), fill='black', font=F_META)
    if consult.get('notes'):
        d.text((PAD, 76), _ascii(f"trader note: {consult['notes']}")[:190], fill='black', font=F_META)
    d.line([(0, HEADER_H - 2), (W, HEADER_H - 2)], fill='black', width=2)

    y = HEADER_H + PAD
    for kind, val in blocks:
        if kind == 'shot':
            label, im = val
            d.text((PAD, y), label, fill='black', font=F_ROLE)
            y += LINE_H
            page.paste(im, (PAD, y))
            y += im.height + 8
        else:
            d.text((PAD, y), val, fill='#000000' if kind == 'role' else '#1a1a1a',
                   font=F_ROLE if kind == 'role' else F_BODY)
            y += LINE_H
    return page


def pages_for(consult):
    pages, batch, used, cont = [], [], 0, False
    room = PAGE_MAX_H - HEADER_H - 2 * PAD
    for b in blocks_for(consult):
        hb = height(b)
        if batch and used + hb > room:
            pages.append(render_page(consult, batch, cont))
            batch, used, cont = [], 0, True
        batch.append(b)
        used += hb
        if used > room:            # a tall screenshot alone can exceed a page — give it one
            pages.append(render_page(consult, batch, cont))
            batch, used, cont = [], 0, True
    if batch:
        pages.append(render_page(consult, batch, cont))
    return pages


def sync():
    try:
        with open(CONSULTS) as f:
            consults = json.load(f)
    except (OSError, ValueError):
        consults = []
    consults = consults[-MAX_CONSULTS:]

    pages = []
    for c in consults:
        pages.extend(pages_for(c))
    if not pages:
        if os.path.exists(PDF):
            os.remove(PDF)
        print(json.dumps({'pdf': None, 'consults': 0, 'pages': 0}))
        return

    os.makedirs(DIR, exist_ok=True)
    pages[0].save(PDF, save_all=True, append_images=pages[1:], resolution=110)
    print(json.dumps({'pdf': PDF, 'consults': len(consults), 'pages': len(pages),
                      'latest': consults[-1]['id'], 'bytes': os.path.getsize(PDF)}))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == 'sync':
        sync()
    else:
        sys.exit(__doc__)
