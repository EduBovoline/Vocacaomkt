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


def render_html_frame(html_path: Path, out_png: Path, width: int = 1080, height: int = 1920):
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
            "--virtual-time-budget=3000",
            f"--screenshot={str(out_png.resolve())}",
            uri,
        ]
        subprocess.run(cmd, check=True)
    im = Image.open(out_png)
    if im.size != (width, height):
        im = im.crop((0, 0, width, height))
        im.save(out_png)


def build_safe_scenes():
    safety_old = (SITE_DIR / "cases" / "safety-antigo.png").as_uri()
    safety_new = (SITE_DIR / "cases" / "safety-novo.png").as_uri()

    # Meta Safe Area Standard:
    # Width: 1080px (Margins: 64px left/right -> 952px active width)
    # Height: 1920px (Safe Top: 240px, Safe Bottom: 320px -> Active Content: 240px to 1600px)
    # No footer clutter, clean and focused!

    # CENA 1: WHATSAPP COM SANGRAS RESPEITADAS
    c1 = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1080px; height: 1920px;
    background: #0B141A;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #E9EDEF;
  }}
  .screen {{
    width: 1080px; height: 1920px;
    padding: 240px 64px 340px 64px;
    display: flex; flex-direction: column;
    justify-content: space-between;
    background: #0B141A;
  }}
  .status-bar {{
    display: flex; justify-content: space-between; align-items: center;
    font-size: 28px; color: #8696A0; padding-bottom: 30px;
    border-bottom: 1px solid #202C33;
  }}
  .contact {{
    display: flex; align-items: center; gap: 20px;
  }}
  .avatar {{
    width: 68px; height: 68px; border-radius: 50%; background: #2A3942;
    display: flex; align-items: center; justify-content: center; font-size: 32px;
  }}
  .contact-name {{ font-size: 34px; font-weight: 600; color: #E9EDEF; }}
  .contact-status {{ font-size: 22px; color: #8696A0; }}

  .chat-area {{
    display: flex; flex-direction: column; gap: 36px;
    margin: auto 0;
  }}
  .bubble {{
    max-width: 82%;
    padding: 28px 34px;
    border-radius: 24px;
    font-size: 36px;
    line-height: 1.35;
    position: relative;
  }}
  .bubble-in {{
    align-self: flex-start;
    background: #202C33;
    color: #E9EDEF;
    border-top-left-radius: 4px;
  }}
  .bubble-out {{
    align-self: flex-end;
    background: #005C4B;
    color: #E9EDEF;
    border-top-right-radius: 4px;
  }}
  .time {{
    font-size: 20px; color: rgba(233,237,239,0.6); text-align: right; margin-top: 10px;
  }}
  .footer-hook {{
    background: #111B21; border: 1.5px solid #222E35; border-radius: 24px;
    padding: 34px 36px; font-size: 36px; line-height: 1.35; color: #E9EDEF;
    text-align: center;
  }}
  .footer-hook b {{ color: #25D366; }}
</style>
</head>
<body>
  <div class="screen">
    <div class="status-bar">
      <div class="contact">
        <div class="avatar">👤</div>
        <div>
          <div class="contact-name">Cliente Novo</div>
          <div class="contact-status">online</div>
        </div>
      </div>
      <div>14:32</div>
    </div>

    <div class="chat-area">
      <div class="bubble bubble-in">
        Boa tarde! Gostei do atendimento no balcão. Você me passa o link do site pra eu ver os serviços e mandar pro meu sócio?
        <div class="time">14:31</div>
      </div>

      <div class="bubble bubble-out">
        Putz... nosso site tá meio antigo e não abre direito no celular. Deixa que eu te mando um PDF mesmo.
        <div class="time">14:32</div>
      </div>
    </div>

    <div class="footer-hook">
      Você também tem <b>vergonha de mandar o link</b> do seu site?
    </div>
  </div>
</body>
</html>"""

    # CENA 2: SITE QUE DEMORA (DENTRO DA ZONA SEGURA)
    c2 = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1080px; height: 1920px;
    background: #000;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #FFF;
  }}
  .screen {{
    width: 1080px; height: 1920px;
    padding: 240px 64px 340px 64px;
    display: flex; flex-direction: column;
    justify-content: space-between;
  }}
  .header {{
    font-size: 52px; font-weight: 800; line-height: 1.15;
  }}
  .header span {{ color: #EF4444; }}
  .browser-mockup {{
    background: #18181B; border-radius: 28px; border: 2px solid #27272A;
    overflow: hidden; margin: 30px 0;
  }}
  .browser-bar {{
    background: #27272A; padding: 18px 24px; display: flex; align-items: center; gap: 12px;
  }}
  .dot {{ width: 16px; height: 16px; border-radius: 50%; }}
  .dot-red {{ background: #EF4444; }}
  .dot-yellow {{ background: #F59E0B; }}
  .dot-green {{ background: #10B981; }}
  .url-input {{
    background: #18181B; border-radius: 10px; padding: 8px 18px; font-size: 20px;
    color: #A1A1AA; flex: 1; font-family: monospace;
  }}
  .browser-body {{
    height: 680px; position: relative; background: #000;
  }}
  .browser-body img {{
    width: 100%; height: 100%; object-fit: cover; object-position: top;
  }}
  .pain-pill {{
    position: absolute; bottom: 24px; left: 24px; right: 24px;
    background: rgba(239, 68, 68, 0.95); color: #FFF; font-size: 28px; font-weight: 700;
    padding: 18px 20px; border-radius: 16px; text-align: center;
  }}
  .solution-box {{
    background: #18181B; border: 2px solid #22C55E; border-radius: 22px;
    padding: 30px 34px; font-size: 34px; line-height: 1.35;
  }}
  .solution-box b {{ color: #22C55E; }}
</style>
</head>
<body>
  <div class="screen">
    <div class="header">
      O cliente abre no celular...<br/>
      <span>e desiste em 4 segundos.</span>
    </div>

    <div class="browser-mockup">
      <div class="browser-bar">
        <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
        <div class="url-input">seusite.com.br (carregando...)</div>
      </div>
      <div class="browser-body">
        <img src="{safety_old}" />
        <div class="pain-pill">Demora pra abrir • Letra miúda • Botão não funciona</div>
      </div>
    </div>

    <div class="solution-box">
      Em <b>5 dias</b> a gente pega o que você tem e coloca um site veloz no ar.
    </div>
  </div>
</body>
</html>"""

    # CENA 3: SITE NOVO COM SANGRAS PERFEITAS
    c3 = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1080px; height: 1920px;
    background: #000;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #FFF;
  }}
  .screen {{
    width: 1080px; height: 1920px;
    padding: 240px 64px 340px 64px;
    display: flex; flex-direction: column;
    justify-content: space-between;
  }}
  .header {{
    font-size: 52px; font-weight: 800; line-height: 1.15;
  }}
  .header span {{ color: #22C55E; }}
  .browser-mockup {{
    background: #061B28; border-radius: 28px; border: 2px solid #E5B910;
    overflow: hidden; margin: 26px 0; box-shadow: 0 20px 60px rgba(229,185,16,0.25);
  }}
  .browser-bar {{
    background: #0B2538; padding: 18px 24px; display: flex; align-items: center; gap: 12px;
  }}
  .dot {{ width: 16px; height: 16px; border-radius: 50%; }}
  .dot-green {{ background: #22C55E; }}
  .url-input {{
    background: #061B28; border-radius: 10px; padding: 8px 18px; font-size: 20px;
    color: #22C55E; flex: 1; font-family: monospace; font-weight: 700;
  }}
  .browser-body {{
    height: 660px; position: relative; background: #061B28;
  }}
  .browser-body img {{
    width: 100%; height: 100%; object-fit: cover; object-position: top;
  }}
  .win-pill {{
    position: absolute; bottom: 20px; left: 20px; right: 20px;
    background: #E5B910; color: #061B28; font-size: 28px; font-weight: 800;
    padding: 18px 20px; border-radius: 16px; text-align: center;
  }}
  .feature-list {{
    display: flex; flex-direction: column; gap: 16px; font-size: 28px; color: #D4D4D8;
  }}
  .feature-item {{
    display: flex; align-items: center; gap: 16px;
  }}
  .check {{ color: #22C55E; font-size: 34px; font-weight: 900; }}
</style>
</head>
<body>
  <div class="screen">
    <div class="header">
      Como fica com o <span>Update:</span><br/>
      Direto pro seu WhatsApp.
    </div>

    <div class="browser-mockup">
      <div class="browser-bar">
        <div class="dot dot-green"></div>
        <div class="url-input">seusite.com.br (abre em 0.4s ⚡)</div>
      </div>
      <div class="browser-body">
        <img src="{safety_new}" />
        <div class="win-pill">Carrega na hora • Bonito no celular • WhatsApp direto</div>
      </div>
    </div>

    <div class="feature-list">
      <div class="feature-item"><span class="check">✓</span> Sem você ter que escrever nada</div>
      <div class="feature-item"><span class="check">✓</span> Sem perder tempo em reunião</div>
      <div class="feature-item"><span class="check">✓</span> Entregue e testado em 5 dias úteis</div>
    </div>
  </div>
</body>
</html>"""

    # CENA 4: CTA LIMPO TOTALMENTE DENTRO DAS MARGENS (SEM RODAPÉ EXTRA)
    c4 = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1080px; height: 1920px;
    background: #061B28;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #FFF;
  }}
  .screen {{
    width: 1080px; height: 1920px;
    padding: 240px 64px 340px 64px;
    display: flex; flex-direction: column;
    justify-content: center;
    text-align: center;
  }}
  .tag {{
    display: inline-block; background: rgba(229,185,16,0.14); border: 1.5px solid rgba(229,185,16,0.4);
    color: #E5B910; font-family: monospace; font-size: 24px; font-weight: 700;
    padding: 12px 28px; border-radius: 999px; margin-bottom: 40px; align-self: center;
  }}
  .title {{
    font-size: 72px; font-weight: 900; line-height: 1.1; letter-spacing: -0.02em;
  }}
  .desc {{
    font-size: 34px; line-height: 1.45; color: #A1A1AA; margin-top: 40px;
  }}
  .desc strong {{ color: #FFF; }}
  .cta-button {{
    background: #E5B910; color: #061B28; font-size: 42px; font-weight: 900;
    padding: 30px 56px; border-radius: 999px; display: inline-block;
    margin-top: 52px; box-shadow: 0 16px 40px rgba(229,185,16,0.3); align-self: center;
  }}
</style>
</head>
<body>
  <div class="screen">
    <div class="tag">Vocação • Sorocaba e Região</div>
    <div class="title">
      Manda o link do seu site no nosso WhatsApp.
    </div>
    <div class="desc">
      A gente grava um vídeo de 2 minutos mostrando o que dá pra arrumar e quanto tempo leva. <strong>Sem custo e sem compromisso.</strong>
    </div>
    <div class="cta-button">
      Tocar em "Saiba mais" ↗
    </div>
  </div>
</body>
</html>"""

    scenes = [("safe_1", c1), ("safe_2", c2), ("safe_3", c3), ("safe_4", c4)]
    png_paths = []
    for name, content in scenes:
        hpath = BASE_DIR / f"{name}.html"
        ppath = BASE_DIR / f"{name}.png"
        hpath.write_text(content, encoding="utf-8")
        render_html_frame(hpath, ppath, 1080, 1920)
        png_paths.append(ppath)
        print("Rendered safe frame:", ppath)
    return png_paths


def build_safe_video(png_paths):
    out_mp4 = BASE_DIR / "vocacao-update-video-safe-areas.mp4"
    filter_complex = (
        "[0:v]scale=1080:1920,fps=30[v0];"
        "[1:v]scale=1080:1920,fps=30[v1];"
        "[2:v]scale=1080:1920,fps=30[v2];"
        "[3:v]scale=1080:1920,fps=30[v3];"
        "[v0][v1]xfade=transition=fade:duration=0.2:offset=3.5[vx1];"
        "[vx1][v2]xfade=transition=slideleft:duration=0.25:offset=7.0[vx2];"
        "[vx2][v3]xfade=transition=fade:duration=0.2:offset=10.5,format=yuv420p[vout]"
    )
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1", "-t", "3.7", "-i", str(png_paths[0]),
        "-loop", "1", "-t", "3.7", "-i", str(png_paths[1]),
        "-loop", "1", "-t", "3.7", "-i", str(png_paths[2]),
        "-loop", "1", "-t", "4.0", "-i", str(png_paths[3]),
        "-f", "lavfi", "-t", "14.5", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-filter_complex", filter_complex,
        "-map", "[vout]",
        "-map", "4:a",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        "-shortest",
        str(out_mp4),
    ]
    subprocess.run(cmd, check=True)
    print("Video with Meta Safe Areas ready:", out_mp4)
    return out_mp4


if __name__ == "__main__":
    scenes = build_safe_scenes()
    build_safe_video(scenes)
