"""
Vocação - Criativos v2 NACIONAL (corrige os problemas do plano de mídia)

Correções aplicadas:
  - sem "Sorocaba" e sem "1 empresa por bairro"
  - sem "a partir de R$ 450" (preço fica só no site até a decisão)
  - sem "0.4s" nem "6 segundos": usa só o que foi medido (ver medicoes-velocidade.md)
  - versão 9:16 com margens seguras da Meta (topo 240px, base 340px, laterais 64px)
"""
import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
ROOT = BASE_DIR.parent.parent
SITE_DIR = (ROOT / "Site").resolve()
OUT_DIR = BASE_DIR / "v2-nacional"
OUT_DIR.mkdir(exist_ok=True)

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME):
    CHROME = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&family=Geist+Mono:wght@500;600;700&display=swap" rel="stylesheet" />
"""


def render(html_path: Path, out_png: Path, w: int, h: int):
    with tempfile.TemporaryDirectory() as prof:
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--user-data-dir={prof}",
            f"--window-size={w},{h}", "--virtual-time-budget=4000",
            f"--screenshot={out_png.resolve()}", html_path.resolve().as_uri(),
        ], check=True)
    im = Image.open(out_png)
    if im.size != (w, h):
        im.crop((0, 0, w, h)).save(out_png)


def page(w, h, pad_t, pad_b, pad_x, h1_px, show_h, logo, old_img, new_img,
         old_label, new_label, new_strong):
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{FONTS}
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ width:{w}px; height:{h}px; overflow:hidden; background:#061B28;
    color:#F8F9F9; font-family:'Manrope',sans-serif; -webkit-font-smoothing:antialiased; }}
  .canvas {{ width:{w}px; height:{h}px; padding:{pad_t}px {pad_x}px {pad_b}px {pad_x}px;
    display:flex; flex-direction:column; justify-content:space-between;
    background: radial-gradient(850px 650px at 50% 55%, rgba(229,185,16,.12), transparent 70%), #061B28; }}
  .top {{ display:flex; align-items:center; justify-content:space-between; }}
  .brand {{ display:flex; align-items:center; gap:16px; }}
  .brand img {{ height:38px; }}
  .brand span {{ font-size:24px; font-weight:700; letter-spacing:-.02em; }}
  .pill {{ font-family:'Geist Mono',monospace; font-size:16px; color:#E5B910;
    border:1px solid rgba(229,185,16,.4); padding:10px 22px; border-radius:999px; }}
  h1 {{ font-family:'Instrument Serif',Georgia,serif; font-size:{h1_px}px; font-weight:400;
    line-height:.98; letter-spacing:-.01em; }}
  h1 em {{ color:#E5B910; font-style:italic; }}
  .show {{ border-radius:26px; overflow:hidden; border:2px solid rgba(229,185,16,.5);
    box-shadow:0 32px 80px rgba(0,0,0,.7); height:{show_h}px; position:relative; background:#041018; }}
  .old {{ position:absolute; inset:0; clip-path:polygon(0 0,56% 0,44% 100%,0 100%); z-index:1; overflow:hidden; }}
  .old img {{ width:100%; height:100%; object-fit:cover; object-position:top center;
    filter:grayscale(40%) contrast(.9) brightness(.78); }}
  .new {{ position:absolute; inset:0; clip-path:polygon(56% 0,100% 0,100% 100%,44% 100%); z-index:2; overflow:hidden; }}
  .new img {{ width:100%; height:100%; object-fit:cover; object-position:top center; }}
  svg.bolt {{ position:absolute; inset:0; z-index:5; pointer-events:none; }}
  .tag-old {{ position:absolute; top:22px; left:22px; z-index:10; background:rgba(11,20,26,.9);
    border:1px solid rgba(255,90,90,.4); color:#FF8080; font-family:'Geist Mono',monospace;
    font-size:15px; font-weight:700; padding:8px 18px; border-radius:999px; }}
  .tag-new {{ position:absolute; bottom:22px; right:22px; z-index:10; background:rgba(6,27,40,.94);
    border:1.5px solid #E5B910; color:#F8F9F9; font-family:'Geist Mono',monospace;
    font-size:16px; padding:10px 22px; border-radius:999px; }}
  .tag-new strong {{ color:#E5B910; }}
  .bottom {{ display:flex; align-items:center; justify-content:space-between; gap:24px; }}
  .meta {{ font-size:22px; color:#B8BFC3; font-weight:500; line-height:1.3; }}
  .meta strong {{ color:#F8F9F9; font-weight:700; }}
  .cta {{ background:#E5B910; color:#061B28; font-size:22px; font-weight:800;
    padding:18px 34px; border-radius:999px; white-space:nowrap; }}
</style></head>
<body><div class="canvas">
  <div class="top">
    <div class="brand"><img src="{logo}" alt="Vocação" /><span>Vocação</span></div>
    <span class="pill">Zero mensalidade</span>
  </div>

  <h1>Seu site refeito <em>em até 5 dias.</em></h1>

  <div class="show">
    <div class="old"><img src="{old_img}" alt="Antes" /></div>
    <div class="new"><img src="{new_img}" alt="Depois" /></div>
    <svg class="bolt" width="100%" height="100%" viewBox="0 0 1000 1000" preserveAspectRatio="none">
      <defs><filter id="g" x="-30%" y="-30%" width="160%" height="160%">
        <feGaussianBlur stdDeviation="7" result="b1"/><feGaussianBlur stdDeviation="15" result="b2"/>
        <feMerge><feMergeNode in="b2"/><feMergeNode in="b1"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter></defs>
      <polyline points="560,0 535,286 555,330 475,661 500,705 440,1000" fill="none"
        stroke="#E5B910" stroke-width="4.5" vector-effect="non-scaling-stroke" filter="url(#g)"/>
      <polyline points="560,0 535,286 555,330 475,661 500,705 440,1000" fill="none"
        stroke="#FFFFFF" stroke-width="2" vector-effect="non-scaling-stroke"/>
    </svg>
    <div class="tag-old">{old_label}</div>
    <div class="tag-new">{new_label} · <strong>{new_strong}</strong></div>
  </div>

  <div class="bottom">
    <span class="meta">Você paga a 2ª metade <strong>só depois de aprovar</strong></span>
    <div class="cta">vocacao.digital ↗</div>
  </div>
</div></body></html>"""


def main():
    logo = (SITE_DIR / "logo-vocacao-white-gold.svg").as_uri()
    cases = {
        "safety-first": dict(
            old=(SITE_DIR / "cases" / "safety-antigo.png").as_uri(),
            new=(SITE_DIR / "cases" / "safety-novo.png").as_uri(),
            old_label="✕ Como estava antes",
            new_label="✓ Depois da Vocação",
            strong="3x mais rápido no celular",
        ),
        "maca-de-amor": dict(
            old=(SITE_DIR / "cases" / "maca-antigo.png").as_uri(),
            new=(SITE_DIR / "cases" / "maca-novo.png").as_uri(),
            old_label="✕ Cardápio antigo",
            new_label="✓ Novo cardápio",
            strong="pedido no WhatsApp",
        ),
    }
    formats = {
        # nome: (w, h, pad_top, pad_bottom, pad_x, h1_px, showcase_h)
        "4x5": (1080, 1350, 80, 80, 84, 96, 560),
        # 9:16 com margens seguras da Meta: topo 240, base 340, laterais 64
        "9x16-safe": (1080, 1920, 240, 340, 64, 104, 640),
    }
    for cname, c in cases.items():
        for fname, (w, h, pt, pb, px, h1, sh) in formats.items():
            html = page(w, h, pt, pb, px, h1, sh, logo, c["old"], c["new"],
                        c["old_label"], c["new_label"], c["strong"])
            stem = f"split-raio-{cname}-{fname}"
            hp, pp = OUT_DIR / f"{stem}.html", OUT_DIR / f"{stem}.png"
            hp.write_text(html, encoding="utf-8")
            render(hp, pp, w, h)
            print("OK", pp)


if __name__ == "__main__":
    main()
