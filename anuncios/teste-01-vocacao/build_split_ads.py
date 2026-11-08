import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
SITE_DIR = (BASE_DIR.parent.parent / "Site").resolve()
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME):
    CHROME = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def render_html_to_png(html_path: Path, out_png: Path, width: int = 1080, height: int = 1350):
    with tempfile.TemporaryDirectory() as tmp_profile:
        uri = html_path.resolve().as_uri()
        cmd = [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"--user-data-dir={tmp_profile}",
            f"--window-size={width},{height}",
            "--virtual-time-budget=3500",
            f"--screenshot={str(out_png.resolve())}",
            uri,
        ]
        subprocess.run(cmd, check=True)
    im = Image.open(out_png)
    if im.size != (width, height):
        im = im.crop((0, 0, width, height))
        im.save(out_png)


def build_split_ads():
    logo_white_gold = (SITE_DIR / "logo-vocacao-white-gold.svg").as_uri()

    safety_old = (SITE_DIR / "cases" / "safety-antigo.png").as_uri()
    safety_new = (SITE_DIR / "cases" / "safety-novo.png").as_uri()

    maca_old = (SITE_DIR / "cases" / "maca-antigo.png").as_uri()
    maca_new = (SITE_DIR / "cases" / "maca-novo.png").as_uri()

    fonts = """
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&family=Geist+Mono:wght@500;600;700&display=swap" rel="stylesheet" />
    """

    def generate_html(case_name: str, old_img: str, new_img: str, old_label: str, new_label: str, badge_meta: str):
        return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
{fonts}
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1080px;
    height: 1350px;
    overflow: hidden;
    background: #061B28;
    color: #F8F9F9;
    font-family: 'Manrope', sans-serif;
    -webkit-font-smoothing: antialiased;
  }}
  .canvas {{
    width: 1080px;
    height: 1350px;
    padding: 80px 84px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background:
      radial-gradient(850px 650px at 50% 55%, rgba(229, 185, 16, 0.12), transparent 70%),
      #061B28;
    position: relative;
  }}
  .top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .brand {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}
  .brand img {{ height: 38px; }}
  .brand span {{
    font-size: 24px;
    font-weight: 700;
    letter-spacing: -0.02em;
  }}
  .pill {{
    font-family: 'Geist Mono', monospace;
    font-size: 16px;
    color: #E5B910;
    border: 1px solid rgba(229, 185, 16, 0.4);
    padding: 10px 22px;
    border-radius: 999px;
  }}
  .headline-wrap {{
    margin-top: 24px;
  }}
  h1 {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 90px;
    font-weight: 400;
    line-height: 0.98;
    letter-spacing: -0.01em;
  }}
  h1 em {{
    color: #E5B910;
    font-style: italic;
  }}

  /* Moldura Showcase Dividida por Raio Transversal */
  .split-showcase {{
    margin: 28px 0;
    border-radius: 26px;
    overflow: hidden;
    border: 2px solid rgba(229, 185, 16, 0.5);
    box-shadow: 0 32px 80px rgba(0, 0, 0, 0.7);
    height: 560px;
    position: relative;
    background: #041018;
  }}

  /* Lado Esquerdo / Superior: Site Antigo */
  .half-old {{
    position: absolute;
    inset: 0;
    clip-path: polygon(0 0, 56% 0, 44% 100%, 0 100%);
    background: #0B141A;
    overflow: hidden;
    z-index: 1;
  }}
  .half-old img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    filter: grayscale(40%) contrast(0.9) brightness(0.78);
  }}

  /* Lado Direito / Inferior: Site Novo */
  .half-new {{
    position: absolute;
    inset: 0;
    clip-path: polygon(56% 0, 100% 0, 100% 100%, 44% 100%);
    overflow: hidden;
    z-index: 2;
  }}
  .half-new img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
  }}

  /* Linha de Raio / Corte Transversal com Brilho Neon */
  .lightning-cut {{
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 5;
  }}

  /* Rótulos Flutuantes nos Cantos */
  .tag-old {{
    position: absolute;
    top: 24px;
    left: 24px;
    background: rgba(11, 20, 26, 0.9);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 90, 90, 0.4);
    color: #FF8080;
    font-family: 'Geist Mono', monospace;
    font-size: 15px;
    font-weight: 700;
    padding: 8px 18px;
    border-radius: 999px;
    z-index: 10;
  }}
  .tag-new {{
    position: absolute;
    bottom: 24px;
    right: 24px;
    background: rgba(6, 27, 40, 0.94);
    backdrop-filter: blur(8px);
    border: 1.5px solid #E5B910;
    color: #F8F9F9;
    font-family: 'Geist Mono', monospace;
    font-size: 16px;
    padding: 10px 22px;
    border-radius: 999px;
    z-index: 10;
  }}
  .tag-new strong {{
    color: #E5B910;
  }}

  /* Rodapé */
  .bottom {{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .meta {{
    font-size: 24px;
    color: #B8BFC3;
    font-weight: 500;
  }}
  .meta strong {{
    color: #F8F9F9;
    font-weight: 700;
  }}
  .cta {{
    background: #E5B910;
    color: #061B28;
    font-size: 22px;
    font-weight: 800;
    padding: 18px 34px;
    border-radius: 999px;
  }}
</style>
</head>
<body>
  <div class="canvas">
    <div class="top">
      <div class="brand">
        <img src="{logo_white_gold}" alt="Vocação" />
        <span>Vocação</span>
      </div>
      <span class="pill">Zero mensalidade</span>
    </div>

    <div class="headline-wrap">
      <h1>Site rápido e Google Maps arrumado <em>em até 7 dias.</em></h1>
    </div>

    <!-- Moldura Dividida por Raio Transversal -->
    <div class="split-showcase">
      <!-- Metade Antiga -->
      <div class="half-old">
        <img src="{old_img}" alt="Antes" />
      </div>

      <!-- Metade Nova -->
      <div class="half-new">
        <img src="{new_img}" alt="Depois Vocação" />
      </div>

      <!-- Efeito Raio Transversal (SVG Line com Glow Dourado) -->
      <svg class="lightning-cut" width="100%" height="100%" viewBox="0 0 1000 560" preserveAspectRatio="none">
        <defs>
          <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="7" result="blur1" />
            <feGaussianBlur stdDeviation="15" result="blur2" />
            <feMerge>
              <feMergeNode in="blur2" />
              <feMergeNode in="blur1" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>
        <!-- Linha do Raio Cortando na Transversal -->
        <polyline points="560,0 535,160 555,185 475,370 500,395 440,560" 
                  fill="none" stroke="#E5B910" stroke-width="4.5" filter="url(#glow)" />
        <polyline points="560,0 535,160 555,185 475,370 500,395 440,560" 
                  fill="none" stroke="#FFFFFF" stroke-width="2" />
      </svg>

      <!-- Selos comparativos nos cantos -->
      <div class="tag-old">{old_label}</div>
      <div class="tag-new">{new_label} · <strong>{badge_meta}</strong></div>
    </div>

    <div class="bottom">
      <span class="meta">Projetos fechados a partir de <strong>R$ 450</strong></span>
      <div class="cta">vocacao.digital ↗</div>
    </div>
  </div>
</body>
</html>"""

    html_safety = generate_html(
        case_name="Safety First",
        old_img=safety_old,
        new_img=safety_new,
        old_label="✕ Como estava antes",
        new_label="✓ Depois da Vocação",
        badge_meta="Abre em 0.4s",
    )

    html_maca = generate_html(
        case_name="Maçã do Amor",
        old_img=maca_old,
        new_img=maca_new,
        old_label="✕ Cardápio antigo",
        new_label="✓ Novo cardápio online",
        badge_meta="Direto pro WhatsApp",
    )

    outputs = []
    cases = [
        ("anuncio-split-raio-safety-first", html_safety),
        ("anuncio-split-raio-maca-de-amor", html_maca),
    ]

    for name, content in cases:
        hpath = BASE_DIR / f"{name}.html"
        ppath = BASE_DIR / f"{name}.png"
        hpath.write_text(content, encoding="utf-8")
        render_html_to_png(hpath, ppath, 1080, 1350)
        outputs.append(ppath)
        print("Generated split ad:", ppath)

    return outputs


if __name__ == "__main__":
    build_split_ads()
