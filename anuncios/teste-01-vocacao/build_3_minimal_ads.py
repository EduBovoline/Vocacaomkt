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


def build_three_options():
    logo_white_gold = (SITE_DIR / "logo-vocacao-white-gold.svg").as_uri()
    logo_dark = (BASE_DIR.parent.parent / "documentacao" / "Logotipo Vocação 2027.svg").as_uri()
    safety_new = (SITE_DIR / "cases" / "safety-novo.png").as_uri()

    fonts = """
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
    """

    # OPÇÃO 1: Editorial Tipográfico Escuro (Obsidian + Citron Gold, puro respiro)
    html_op1 = f"""<!doctype html>
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
    padding: 96px 96px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: radial-gradient(900px 900px at 85% 15%, rgba(229, 185, 16, 0.08), transparent 70%), #061B28;
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
    color: #F8F9F9;
  }}
  .tag {{
    font-family: 'Geist Mono', monospace;
    font-size: 16px;
    color: #B8BFC3;
    letter-spacing: 0.02em;
  }}
  .center {{
    margin: auto 0;
  }}
  h1 {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 112px;
    font-weight: 400;
    line-height: 0.98;
    letter-spacing: -0.015em;
    color: #F8F9F9;
  }}
  h1 em {{
    color: #E5B910;
    font-style: italic;
    display: block;
    margin-top: 14px;
  }}
  p {{
    margin-top: 48px;
    font-size: 30px;
    line-height: 1.45;
    color: #B8BFC3;
    font-weight: 400;
    max-width: 760px;
  }}
  p strong {{
    color: #F8F9F9;
    font-weight: 600;
  }}
  .bottom {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 40px;
    border-top: 1px solid rgba(184, 191, 195, 0.18);
  }}
  .meta {{
    font-family: 'Geist Mono', monospace;
    font-size: 18px;
    color: #B8BFC3;
  }}
  .cta {{
    background: #E5B910;
    color: #061B28;
    font-size: 22px;
    font-weight: 800;
    padding: 18px 34px;
    border-radius: 999px;
    letter-spacing: -0.01em;
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
      <span class="tag">Sorocaba e região</span>
    </div>

    <div class="center">
      <h1>
        Sua empresa é ótima no balcão.
        <em>No celular, ela parece?</em>
      </h1>
      <p>
        Arrumamos seu <strong>Google Maps</strong> e colocamos seu <strong>site novo no ar</strong> em uma semana. Sem mensalidade.
      </p>
    </div>

    <div class="bottom">
      <span class="meta">1 empresa por bairro · Pagamento 50/50</span>
      <div class="cta">vocacao.digital ↗</div>
    </div>
  </div>
</body>
</html>"""

    # OPÇÃO 2: Editorial Claro Minimalista (Chalk White + Obsidian + Detalhe Citron)
    html_op2 = f"""<!doctype html>
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
    background: #F8F9F9;
    color: #061B28;
    font-family: 'Manrope', sans-serif;
    -webkit-font-smoothing: antialiased;
  }}
  .canvas {{
    width: 1080px;
    height: 1350px;
    padding: 96px 96px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #F8F9F9;
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
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #061B28;
  }}
  .tag {{
    font-family: 'Geist Mono', monospace;
    font-size: 16px;
    color: #526370;
    background: #ECEFF1;
    padding: 10px 20px;
    border-radius: 999px;
  }}
  .center {{
    margin: auto 0;
  }}
  h1 {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 108px;
    font-weight: 400;
    line-height: 0.98;
    letter-spacing: -0.015em;
    color: #061B28;
  }}
  .highlight {{
    display: inline-block;
    background: #E5B910;
    color: #061B28;
    font-style: italic;
    padding: 0 18px 6px;
    border-radius: 12px;
    margin-top: 12px;
  }}
  p {{
    margin-top: 48px;
    font-size: 30px;
    line-height: 1.45;
    color: #243542;
    font-weight: 500;
    max-width: 780px;
  }}
  .bottom {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 40px;
    border-top: 1px solid rgba(6, 27, 40, 0.12);
  }}
  .meta {{
    font-family: 'Geist Mono', monospace;
    font-size: 18px;
    color: #526370;
  }}
  .cta {{
    background: #061B28;
    color: #F8F9F9;
    font-size: 22px;
    font-weight: 700;
    padding: 18px 34px;
    border-radius: 999px;
  }}
</style>
</head>
<body>
  <div class="canvas">
    <div class="top">
      <div class="brand">
        <img src="{logo_dark}" alt="Vocação" />
        <span>Vocação</span>
      </div>
      <span class="tag">Sites · Google Maps · Tour 360°</span>
    </div>

    <div class="center">
      <h1>
        Tem gente procurando seu serviço agora.
        <span class="highlight">Vão achar você</span><br/>
        ou o vizinho?
      </h1>
      <p>
        Você paga 50% na entrada e os outros 50% só depois que ver tudo funcionando no ar.
      </p>
    </div>

    <div class="bottom">
      <span class="meta">Sem mensalidade · Pronto em 5 a 7 dias</span>
      <div class="cta">vocacao.digital ↗</div>
    </div>
  </div>
</body>
</html>"""

    # OPÇÃO 3: Minimalista com 1 Vitrine Flutuante Limpa (Foco visual único)
    html_op3 = f"""<!doctype html>
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
    padding: 84px 88px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background:
      radial-gradient(800px 600px at 50% 60%, rgba(229, 185, 16, 0.14), transparent 70%),
      #061B28;
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
    margin-top: 20px;
  }}
  h1 {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 92px;
    font-weight: 400;
    line-height: 0.98;
    letter-spacing: -0.01em;
  }}
  h1 em {{
    color: #E5B910;
    font-style: italic;
  }}
  .showcase {{
    margin: 28px 0;
    border-radius: 24px;
    overflow: hidden;
    border: 1.5px solid rgba(229, 185, 16, 0.45);
    box-shadow: 0 32px 80px rgba(0, 0, 0, 0.65);
    height: 560px;
    position: relative;
    background: #041018;
  }}
  .showcase img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
  }}
  .speed-badge {{
    position: absolute;
    bottom: 24px;
    left: 24px;
    background: rgba(6, 27, 40, 0.92);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(229, 185, 16, 0.5);
    color: #F8F9F9;
    font-family: 'Geist Mono', monospace;
    font-size: 18px;
    padding: 12px 22px;
    border-radius: 999px;
  }}
  .speed-badge strong {{
    color: #E5B910;
  }}
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

    <div class="showcase">
      <img src="{safety_new}" alt="Projeto Vocação" />
      <div class="speed-badge">Carrega em <strong>0.4s</strong> no celular</div>
    </div>

    <div class="bottom">
      <span class="meta">Projetos fechados a partir de <strong>R$ 450</strong></span>
      <div class="cta">vocacao.digital ↗</div>
    </div>
  </div>
</body>
</html>"""

    options = [
        ("op1-minimal-escuro", html_op1),
        ("op2-minimal-claro", html_op2),
        ("op3-minimal-vitrine", html_op3),
    ]
    outputs = []
    for name, content in options:
        hpath = BASE_DIR / f"{name}.html"
        ppath = BASE_DIR / f"{name}.png"
        hpath.write_text(content, encoding="utf-8")
        render_html_to_png(hpath, ppath, 1080, 1350)
        outputs.append(ppath)
        print("Saved:", ppath)
    return outputs


if __name__ == "__main__":
    build_three_options()
