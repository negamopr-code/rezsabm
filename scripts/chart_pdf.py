#!/usr/bin/env python3
"""Rolling chart-upload PDF — the token-free eye of the exit advisor.

Every picture the user drops into the "Exit advisor" tab becomes one page of ONE PDF
(data/advisor/charts.pdf), newest page LAST, each page stamped with a header line the
notebook can quote back: consult id, UTC date/time, symbol/timeframe and the user's note.
The whole PDF is rewritten on every upload and replaces the single "REZSABM chart uploads"
source in the SABM notebook — so NotebookLM reads the picture itself (zero Claude tokens),
always sees the history, and the notebook never accumulates sources.

Usage: chart_pdf.py add <image> <id> <iso-utc> <caption>   -> rewrites the PDF, prints JSON
       chart_pdf.py list                                    -> pages currently in the PDF
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, 'data', 'advisor')
PDF = os.path.join(DIR, 'charts.pdf')
INDEX = os.path.join(DIR, 'pages.json')
SHOTS = os.path.join(DIR, 'shots')
MAX_PAGES = int(os.environ.get('REZ_MAX_CHART_PAGES', '40'))
MAX_W = 1600          # NotebookLM re-rasterises anyway; keep the file small and the text crisp
HEADER_H = 96


_DEFAULT_FONT = [None]


def _font(size):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
              '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'):
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                pass
    _DEFAULT_FONT[0] = True     # PIL's built-in bitmap font is latin-1 only
    return ImageFont.load_default()


def _safe(text):
    """The fallback bitmap font raises on any non-latin-1 character (em dashes, arrows, →)."""
    if not _DEFAULT_FONT[0]:
        return text
    return text.encode('latin-1', 'replace').decode('latin-1')


def page(img_path, pid, when, caption):
    """One PDF page: a white header carrying the stamp, then the picture."""
    im = Image.open(img_path)
    if getattr(im, 'n_frames', 1) > 1:      # animated webp/gif — the first frame is the chart
        im.seek(0)
    im = im.convert('RGB')
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)

    out = Image.new('RGB', (im.width, im.height + HEADER_H), 'white')
    d = ImageDraw.Draw(out)
    f30, f22, f20 = _font(30), _font(22), _font(20)
    d.text((16, 12), _safe(f'CHART UPLOAD {pid}'), fill='black', font=f30)
    d.text((16, 50), _safe(f'uploaded {when} UTC'), fill='black', font=f22)
    if caption:
        d.text((16, 74), _safe(caption[:160]), fill='black', font=f20)
    d.line([(0, HEADER_H - 1), (im.width, HEADER_H - 1)], fill='black', width=2)
    out.paste(im, (0, HEADER_H))
    return out


def load_index():
    try:
        with open(INDEX) as f:
            return json.load(f)
    except (OSError, ValueError):
        return []


def cmd_add(img_path, pid, when, caption):
    os.makedirs(SHOTS, exist_ok=True)
    kept = os.path.join(SHOTS, f'{pid}.png')
    page(img_path, pid, when, caption).save(kept)          # the composed page, reusable on rewrite

    pages = [p for p in load_index() if p['id'] != pid]
    pages.append({'id': pid, 'when': when, 'caption': caption, 'file': kept})
    pages = pages[-MAX_PAGES:]
    for p in load_index():                                  # drop the images that rolled off
        if p not in pages and os.path.exists(p['file']) and p['file'] != kept:
            try:
                os.remove(p['file'])
            except OSError:
                pass

    imgs = [Image.open(p['file']).convert('RGB') for p in pages]
    imgs[0].save(PDF, save_all=True, append_images=imgs[1:], resolution=110)
    with open(INDEX, 'w') as f:
        json.dump(pages, f, indent=1)
    print(json.dumps({'pdf': PDF, 'pages': len(pages), 'latest': pid,
                      'bytes': os.path.getsize(PDF)}))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == 'list':
        print(json.dumps(load_index(), indent=1))
    elif len(sys.argv) >= 5 and sys.argv[1] == 'add':
        os.makedirs(DIR, exist_ok=True)
        cmd_add(sys.argv[2], sys.argv[3], sys.argv[4], ' '.join(sys.argv[5:]))
    else:
        sys.exit(__doc__)
