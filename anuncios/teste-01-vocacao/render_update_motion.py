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


def render_frame(html_path: Path, out_png: Path, width: int = 1080, height: int = 1920):
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


def build_scenes():
    logo_svg = (SITE_DIR / "logo-vocacao-white-gold.svg").as_uri()
    safety_old = (SITE_DIR / "cases" / "safety-antigo.png").as_uri()
    safety_new = (SITE_DIR / "cases" / "safety-novo.png").as_uri()

    fonts = """
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&family=Geist+Mono:wght@500;600;700&display=swap" rel="stylesheet" />
    """

    common_css = f"""
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      width: 1080px;
      height: 1920px;
      overflow: hidden;
      background: #061B28;
      color: #F8F9F9;
      font-family: 'Manrope', sans-serif;
      -webkit-font-smoothing: antialiased;
    }}
    .stage {{
      width: 1080px;
      height: 1920px;
      padding: 100px 80px 110px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      background:
        radial-gradient(900px 700px at 85% 15%, rgba(229, 185, 16, 0.16), transparent 70%),
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
    .brand img {{ height: 46px; }}
    .brand span {{
      font-size: 28px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #F8F9F9;
    }}
    .badge {{
      font-family: 'Geist Mono', monospace;
      font-size: 18px;
      color: #E5B910;
      border: 1px solid rgba(229, 185, 16, 0.4);
      padding: 10px 22px;
      border-radius: 999px;
    }}
    .serif {{
      font-family: 'Instrument Serif', Georgia, serif;
      font-weight: 400;
    }}
    .gold {{ color: #E5B910; }}
    .foot {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 36px;
      border-top: 1px solid rgba(184, 191, 195, 0.16);
    }}
    .foot .meta {{
      font-family: 'Geist Mono', monospace;
      font-size: 20px;
      color: #B8BFC3;
    }}
    .foot .btn {{
      background: #E5B910;
      color: #061B28;
      font-size: 24px;
      font-weight: 800;
      padding: 18px 36px;
      border-radius: 999px;
    }}
    """

    # CENA 1: A Dor do Site Antigo (0 a 3.5s)
    c1 = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">Vocação Update</span>
  </div>
  
  <div style="margin: auto 0;">
    <h1 class="serif" style="font-size: 112px; line-height: 0.98;">
      Seu site atual dá orgulho ou você tem vergonha de mandar o link?
    </h1>
    <p style="margin-top: 44px; font-size: 34px; line-height: 1.4; color: #B8BFC3; font-weight: 400;">
      A maioria dos sites de empresas locais foi feita anos atrás: demora para carregar e fica horrível na tela do celular.
    </p>
  </div>

  <div class="foot">
    <span class="meta">Seu cliente repara nisso</span>
    <span class="btn">vocacao.digital ↗</span>
  </div>
</div>
</body></html>"""

    # CENA 2: O Alívio / A Solução Sem Esforço (3.5 a 7s)
    c2 = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">Sem reunião · Sem enrolação</span>
  </div>
  
  <div style="margin: auto 0;">
    <h1 class="serif" style="font-size: 104px; line-height: 0.98;">
      A gente reforma tudo <em class="gold">em 5 dias úteis.</em>
    </h1>
    <div style="margin-top: 48px; display: flex; flex-direction: column; gap: 24px;">
      <div style="background: rgba(248,249,249,0.05); border: 1px solid rgba(184,191,195,0.2); border-radius: 20px; padding: 28px 32px; font-size: 28px; color: #F8F9F9;">
        Você não precisa escrever nenhum texto do zero
      </div>
      <div style="background: rgba(248,249,249,0.05); border: 1px solid rgba(184,191,195,0.2); border-radius: 20px; padding: 28px 32px; font-size: 28px; color: #F8F9F9;">
        Aproveitamos as informações que já estão lá
      </div>
      <div style="background: rgba(229,185,16,0.12); border: 1.5px solid #E5B910; border-radius: 20px; padding: 28px 32px; font-size: 28px; color: #F8F9F9;">
        Seu site novo abre em menos de meio segundo
      </div>
    </div>
  </div>

  <div class="foot">
    <span class="meta">Entrega travada no prazo</span>
    <span class="btn">vocacao.digital ↗</span>
  </div>
</div>
</body></html>"""

    # CENA 3: Prova Visual Limpa (7 a 11s)
    c3 = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">Antes &amp; Depois</span>
  </div>
  
  <div style="margin: auto 0;">
    <h1 class="serif" style="font-size: 88px; line-height: 0.98;">
      De site lento a máquina rápida no WhatsApp.
    </h1>
    <div style="margin-top: 36px; border-radius: 24px; overflow: hidden; border: 1.5px solid rgba(229,185,16,0.4); box-shadow: 0 24px 60px rgba(0,0,0,0.6); height: 680px; position: relative;">
      <img src="{safety_new}" style="width: 100%; height: 100%; object-fit: cover; object-position: top center;" />
      <div style="position: absolute; bottom: 24px; left: 24px; background: rgba(6,27,40,0.92); border: 1px solid #E5B910; color: #F8F9F9; font-family: 'Geist Mono', monospace; font-size: 20px; padding: 12px 24px; border-radius: 999px;">
        Abre em <strong>0.4s</strong> no celular
      </div>
    </div>
  </div>

  <div class="foot">
    <span class="meta">Caso real da Vocação</span>
    <span class="btn">vocacao.digital ↗</span>
  </div>
</div>
</body></html>"""

    # CENA 4: Preço Transparente + Risco Zero (11 a 15s)
    c4 = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">R$ 980 à vista</span>
  </div>
  
  <div style="margin: auto 0; text-align: center;">
    <div style="font-family: 'Geist Mono', monospace; font-size: 22px; color: #E5B910; margin-bottom: 24px;">
      Zero mensalidade obrigatória
    </div>
    <h1 class="serif" style="font-size: 104px; line-height: 0.98;">
      50% de entrada.
      <em class="gold">O restante só depois que aprovar tudo no ar.</em>
    </h1>
    <p style="margin-top: 40px; font-size: 32px; color: #B8BFC3; line-height: 1.4;">
      Peça uma avaliação gratuita do seu site hoje pelo WhatsApp da Vocação.
    </p>
    <div style="margin-top: 60px; display: inline-block; background: #E5B910; color: #061B28; font-size: 40px; font-weight: 800; padding: 28px 60px; border-radius: 999px;">
      vocacao.digital ↗
    </div>
  </div>

  <div class="foot">
    <span class="meta">1 empresa por bairro</span>
    <span class="meta" style="color: #E5B910;">WhatsApp: (15) 98151-2083</span>
  </div>
</div>
</body></html>"""

    scenes = [("cena_1", c1), ("cena_2", c2), ("cena_3", c3), ("cena_4", c4)]
    png_paths = []
    for name, content in scenes:
        hpath = BASE_DIR / f"{name}.html"
        ppath = BASE_DIR / f"{name}.png"
        hpath.write_text(content, encoding="utf-8")
        render_frame(hpath, ppath, 1080, 1920)
        png_paths.append(ppath)
        print("Rendered:", ppath)
    return png_paths


def build_motion_video(png_paths):
    out_mp4 = BASE_DIR / "vocacao-update-video-motion-9x16.mp4"
    # Remotion motion principles: smooth scale/zoom pan + clean crossfade transitions
    filter_complex = (
        "[0:v]scale=1140:2026,zoompan=z='min(zoom+0.0003,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=114:s=1080x1920:fps=30,format=yuv420p[v0];"
        "[1:v]scale=1140:2026,zoompan=z='min(zoom+0.0003,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=114:s=1080x1920:fps=30,format=yuv420p[v1];"
        "[2:v]scale=1140:2026,zoompan=z='min(zoom+0.0003,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=114:s=1080x1920:fps=30,format=yuv420p[v2];"
        "[3:v]scale=1140:2026,zoompan=z='min(zoom+0.0003,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=114:s=1080x1920:fps=30,format=yuv420p[v3];"
        "[v0][v1]xfade=transition=fadeblack:duration=0.4:offset=3.4[vx1];"
        "[vx1][v2]xfade=transition=slideleft:duration=0.4:offset=6.8[vx2];"
        "[vx2][v3]xfade=transition=fadeblack:duration=0.4:offset=10.2,format=yuv420p[vout]"
    )
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1", "-t", "3.8", "-i", str(png_paths[0]),
        "-loop", "1", "-t", "3.8", "-i", str(png_paths[1]),
        "-loop", "1", "-t", "3.8", "-i", str(png_paths[2]),
        "-loop", "1", "-t", "3.8", "-i", str(png_paths[3]),
        "-f", "lavfi", "-t", "14.0", "-i", "sine=frequency=110:sample_rate=44100",
        "-filter_complex", filter_complex,
        "-af", "lowpass=f=220,volume=0.05,afade=t=in:st=0:d=0.8,afade=t=out:st=13.0:d=1.0",
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
    print("Video rendered:", out_mp4)
    return out_mp4


if __name__ == "__main__":
    scenes = build_scenes()
    build_motion_video(scenes)
