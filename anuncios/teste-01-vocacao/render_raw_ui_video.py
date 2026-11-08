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


def build_raw_ui_scenes():
    safety_old = (SITE_DIR / "cases" / "safety-antigo.png").as_uri()
    safety_new = (SITE_DIR / "cases" / "safety-novo.png").as_uri()

    # CENA 1: TELA REAL DO WHATSAPP (A DOR CRUA)
    # A conversa que todo empresário vive: alguém pede o link e ele sente aquele desconforto.
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
    display: flex; flex-direction: column;
    justify-content: space-between;
    padding: 80px 48px;
    background: #0B141A;
  }}
  .status-bar {{
    display: flex; justify-content: space-between; align-items: center;
    font-size: 28px; color: #8696A0; padding-bottom: 40px;
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
    display: flex; flex-direction: column; gap: 32px;
    margin: auto 0;
  }}
  .bubble {{
    max-width: 78%;
    padding: 24px 32px;
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
    font-size: 20px; color: rgba(233,237,239,0.6); text-align: right; margin-top: 8px;
  }}
  .vergonha-tag {{
    background: #EF4444; color: #FFF; font-weight: 700; font-size: 26px;
    padding: 8px 20px; border-radius: 999px; display: inline-block; margin-top: 14px;
  }}
  .footer-hook {{
    background: #111B21; border: 1px solid #222E35; border-radius: 28px;
    padding: 36px 40px; font-size: 36px; line-height: 1.4; color: #E9EDEF;
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
          <div class="contact-name">Cliente Novo (Sorocaba)</div>
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

      <div class="bubble bubble-out" style="opacity: 0.95;">
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

    # CENA 2: A REALIDADE CRUA (O SITE QUE TRAVA VS O QUE VENDE)
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
    display: flex; flex-direction: column;
    justify-content: space-between;
    padding: 80px 48px;
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
    height: 720px; position: relative; background: #000;
  }}
  .browser-body img {{
    width: 100%; height: 100%; object-fit: cover; object-position: top;
  }}
  .pain-pill {{
    position: absolute; bottom: 24px; left: 24px; right: 24px;
    background: rgba(239, 68, 68, 0.95); color: #FFF; font-size: 28px; font-weight: 700;
    padding: 20px 24px; border-radius: 18px; text-align: center;
  }}
  .solution-box {{
    background: #18181B; border: 2px solid #22C55E; border-radius: 24px;
    padding: 32px 36px; font-size: 36px; line-height: 1.35;
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
        <div class="pain-pill">Demora pra abrir • Letra minúscula • Botão não funciona</div>
      </div>
    </div>

    <div class="solution-box">
      Em <b>5 dias</b> a gente pega tudo que você já tem e coloca um site veloz no ar.
    </div>
  </div>
</body>
</html>"""

    # CENA 3: O RESULTADO REAL (SITE NOVO VOANDO)
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
    display: flex; flex-direction: column;
    justify-content: space-between;
    padding: 80px 48px;
  }}
  .header {{
    font-size: 52px; font-weight: 800; line-height: 1.15;
  }}
  .header span {{ color: #22C55E; }}
  .browser-mockup {{
    background: #061B28; border-radius: 28px; border: 2px solid #E5B910;
    overflow: hidden; margin: 30px 0; box-shadow: 0 20px 60px rgba(229,185,16,0.25);
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
    height: 720px; position: relative; background: #061B28;
  }}
  .browser-body img {{
    width: 100%; height: 100%; object-fit: cover; object-position: top;
  }}
  .win-pill {{
    position: absolute; bottom: 24px; left: 24px; right: 24px;
    background: #E5B910; color: #061B28; font-size: 30px; font-weight: 800;
    padding: 20px 24px; border-radius: 18px; text-align: center;
  }}
  .feature-list {{
    display: flex; flex-direction: column; gap: 16px; font-size: 30px; color: #D4D4D8;
  }}
  .feature-item {{
    display: flex; align-items: center; gap: 16px;
  }}
  .check {{ color: #22C55E; font-size: 36px; font-weight: 900; }}
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
        <div class="win-pill">Carrega na hora • Bonito no celular • Botão WhatsApp direto</div>
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

    # CENA 4: CONVITE DIRETO E HUMANO (SEM PAPO DE AGÊNCIA)
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
    display: flex; flex-direction: column;
    justify-content: space-between;
    padding: 100px 56px;
    text-align: center;
  }}
  .hero-text {{
    margin: auto 0;
  }}
  .title {{
    font-size: 72px; font-weight: 900; line-height: 1.1; letter-spacing: -0.02em;
  }}
  .title span {{ color: #E5B910; }}
  .desc {{
    font-size: 34px; line-height: 1.45; color: #A1A1AA; margin-top: 40px;
  }}
  .cta-button {{
    background: #E5B910; color: #061B28; font-size: 44px; font-weight: 900;
    padding: 32px 50px; border-radius: 999px; display: inline-block;
    margin-top: 50px; box-shadow: 0 12px 40px rgba(229,185,16,0.3);
  }}
  .footer {{
    font-size: 26px; color: #71717A;
  }}
</style>
</head>
<body>
  <div class="screen">
    <div style="font-size: 24px; color: #E5B910; font-family: monospace; letter-spacing: 0.1em; text-transform: uppercase;">
      Vocação • Sorocaba e Região
    </div>

    <div class="hero-text">
      <div class="title">
        Manda o link do seu site no nosso WhatsApp.
      </div>
      <div class="desc">
        A gente grava um vídeo de 2 minutos mostrando o que dá pra arrumar e quanto tempo leva. <strong style="color: #FFF;">Sem custo e sem compromisso.</strong>
      </div>
      <div class="cta-button">
        Tocar em "Saiba mais" ↗
      </div>
    </div>

    <div class="footer">
      vocacao.digital • Atendemos 1 empresa por bairro
    </div>
  </div>
</body>
</html>"""

    scenes = [("real_1", c1), ("real_2", c2), ("real_3", c3), ("real_4", c4)]
    png_paths = []
    for name, content in scenes:
        hpath = BASE_DIR / f"{name}.html"
        ppath = BASE_DIR / f"{name}.png"
        hpath.write_text(content, encoding="utf-8")
        render_html_frame(hpath, ppath, 1080, 1920)
        png_paths.append(ppath)
        print("Rendered raw UI frame:", ppath)
    return png_paths


def build_raw_video(png_paths):
    out_mp4 = BASE_DIR / "vocacao-update-video-humano-real.mp4"
    # Cuts secos ou transições curtas nativas de Stories/Reels reais
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
    print("Raw human video ready:", out_mp4)
    return out_mp4


if __name__ == "__main__":
    scenes = build_raw_ui_scenes()
    build_raw_video(scenes)
