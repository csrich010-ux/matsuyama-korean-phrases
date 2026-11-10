#!/usr/bin/env python3
"""Generate QR codes (SVG + PNG) for the audio site.

Usage:
    pip install qrcode pillow
    python3 tools/make_qr.py https://<user>.github.io/matsuyama-korean-phrases/
    python3 tools/make_qr.py https://<user>.github.io/matsuyama-korean-phrases/situations/ situations

Outputs into qr/:
    top.svg / top.png        -> site top page
    c1..c4.svg / .png        -> category (one QR per card on the flyer)
    p01..p24.svg / .png      -> single phrase
    qr/index.html            -> printable preview sheet
"""
import json
import pathlib
import sys

import qrcode
import qrcode.image.svg

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "qr"


def make(url: str, name: str) -> None:
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(OUT / f"{name}.svg")
    qr.make_image(fill_color="#3A3843", back_color="white").save(OUT / f"{name}.png")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: make_qr.py <BASE_URL>")
    global OUT
    base = sys.argv[1].rstrip("/") + "/"
    src = ROOT / sys.argv[2] if len(sys.argv) > 2 else ROOT  # optional sub-site dir, e.g. "situations"
    OUT = src / "qr"
    data = json.loads((src / "phrases.json").read_text(encoding="utf-8"))
    OUT.mkdir(exist_ok=True)

    items = [("top", base, "トップページ")]
    for c in data["categories"]:
        items.append((c["id"], f"{base}#{c['id']}", c["title"]))
        for p in c["phrases"]:
            items.append((p["id"], f"{base}#{p['id']}", f"{p['kana']}（{p['ja']}）"))

    for name, url, _ in items:
        make(url, name)

    cards = "\n".join(
        f'<figure><img src="{n}.svg" alt=""><figcaption><b>{n}</b><br>{label}<br><small>{url}</small></figcaption></figure>'
        for n, url, label in items
    )
    (OUT / "index.html").write_text(
        f"""<!doctype html><html lang="ja"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>QRコード一覧</title>
<style>body{{font-family:sans-serif;margin:16px}}main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px}}
figure{{margin:0;border:1px solid #ddd;border-radius:8px;padding:8px;text-align:center;font-size:12px}}img{{width:100%}}small{{word-break:break-all;color:#777}}</style>
<h1>QRコード一覧</h1><main>{cards}</main></html>""",
        encoding="utf-8",
    )
    print(f"generated {len(items)} QR codes for {base}")


if __name__ == "__main__":
    main()
