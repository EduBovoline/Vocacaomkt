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


def build_interactive_scenes():
    logo_svg = (SITE_DIR / "logo-vocacao-white-gold.svg").as_uri()
    safety_old = (SITE_DIR / "cases" / "safety-antigo.png").as_uri()
    safety_new = (SITE_DIR / "cases" / "safety-novo.png").as_uri()

    fonts = """
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&family=Geist+Mono:wght@500;600;700&display=swap" rel="stylesheet" />
    """

    common_css = """
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body {
      width: 1080px;
      height: 1920px;
      overflow: hidden;
      background: #061B28;
      color: #F8F9F9;
      font-family: 'Manrope', sans-serif;
      -webkit-font-smoothing: antialiased;
    }
    .stage {
      width: 1080px;
      height: 1920px;
      padding: 96px 80px 104px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      background:
        radial-gradient(900px 700px at 85% 15%, rgba(229, 185, 16, 0.16), transparent 70%),
        #061B28;
    }
    .top {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .brand img { height: 46px; }
    .brand span {
      font-size: 28px;
      font-weight: 800;
      letter-spacing: -0.02em;
    }
    .badge {
      font-family: 'Geist Mono', monospace;
      font-size: 18px;
      color: #E5B910;
      border: 1px solid rgba(229, 185, 16, 0.4);
      padding: 10px 22px;
      border-radius: 999px;
    }
    .serif {
      font-family: 'Instrument Serif', Georgia, serif;
      font-weight: 400;
    }
    .gold { color: #E5B910; font-style: italic; }
    .foot {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 36px;
      border-top: 1px solid rgba(184, 191, 195, 0.16);
    }
    .foot .meta {
      font-family: 'Geist Mono', monospace;
      font-size: 20px;
      color: #B8BFC3;
    }
    .foot .btn {
      background: #E5B910;
      color: #061B28;
      font-size: 24px;
      font-weight: 800;
      padding: 18px 36px;
      border-radius: 999px;
    }
    """

    # ATO 1 - FASE A (0 a 1.8s): Apenas a primeira pergunta
    c1a = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">Vocação Update</span>
  </div>
  
  <div style="margin: auto 0;">
    <h1 class="serif" style="font-size: 112px; line-height: 0.98;">
      Seu site atual dá orgulho?
    </h1>
    <div style="height: 180px;"></div>
  </div>

  <div class="foot">
    <span class="meta">Seu cliente repara nisso</span>
    <span class="btn">vocacao.digital ↗</span>
  </div>
</div>
</body></html>"""

    # ATO 1 - FASE B (1.8 a 4.2s): Entra o gancho "ou você tem vergonha de mandar o link?" + subtexto com atraso
    c1b = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">Vocação Update</span>
  </div>
  
  <div style="margin: auto 0;">
    <h1 class="serif" style="font-size: 104px; line-height: 0.98;">
      Seu site atual dá orgulho<br/>
      <em class="gold">ou você tem vergonha de mandar o link?</em>
    </h1>
    <p style="margin-top: 48px; font-size: 32px; line-height: 1.45; color: #B8BFC3;">
      A maioria dos sites de empresas locais foi feita anos atrás: demora para carregar e fica horrível na tela do celular.
    </p>
  </div>

  <div class="foot">
    <span class="meta">Seu cliente repara nisso</span>
    <span class="btn">vocacao.digital ↗</span>
  </div>
</div>
</body></html>"""

    # ATO 2 (4.2 a 7.5s): O Alívio + Pilares Rotativos destacados
    c2 = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">Prazo Fechado</span>
  </div>
  
  <div style="margin: auto 0;">
    <h1 class="serif" style="font-size: 108px; line-height: 0.98;">
      Em 5 dias a gente <em class="gold">reforma tudo.</em>
    </h1>
    
    <div style="margin-top: 48px; display: flex; flex-direction: column; gap: 20px;">
      <div style="background: rgba(229,185,16,0.12); border: 2px solid #E5B910; border-radius: 20px; padding: 26px 32px; display: flex; align-items: center; justify-content: space-between;">
        <span style="font-size: 32px; font-weight: 800; color: #F8F9F9;">Zero reunião</span>
        <span style="font-family:'Geist Mono',monospace; color: #E5B910; font-size: 20px;">Não tomamos seu tempo</span>
      </div>
      
      <div style="background: rgba(248,249,249,0.06); border: 1px solid rgba(184,191,195,0.25); border-radius: 20px; padding: 26px 32px; display: flex; align-items: center; justify-content: space-between;">
        <span style="font-size: 32px; font-weight: 800; color: #F8F9F9;">Aproveitamos as informações</span>
        <span style="font-family:'Geist Mono',monospace; color: #B8BFC3; font-size: 20px;">Sem escrever do zero</span>
      </div>

      <div style="background: rgba(248,249,249,0.06); border: 1px solid rgba(184,191,195,0.25); border-radius: 20px; padding: 26px 32px; display: flex; align-items: center; justify-content: space-between;">
        <span style="font-size: 32px; font-weight: 800; color: #F8F9F9;">Abre em menos de meio segundo</span>
        <span style="font-family:'Geist Mono',monospace; color: #B8BFC3; font-size: 20px;">Abre na hora (&lt;0.5s)</span>
      </div>
    </div>
  </div>

  <div class="foot">
    <span class="meta">Entrega travada em 5 dias</span>
    <span class="btn">vocacao.digital ↗</span>
  </div>
</div>
</body></html>"""

    # ATO 3 (7.5 a 11.0s): Comparativo Flutuante do Site Anterior vs Atual
    c3 = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">Caso Real: Safety First</span>
  </div>
  
  <div style="margin: auto 0;">
    <h1 class="serif" style="font-size: 92px; line-height: 0.98;">
      De site lento a máquina de encaminhar pro WhatsApp.
    </h1>

    <div style="margin-top: 36px; display: flex; flex-direction: column; gap: 20px;">
      <!-- Antes -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,90,90,0.35); border-radius: 20px; padding: 18px 24px; display: flex; gap: 24px; align-items: center;">
        <img src="{safety_old}" style="width: 280px; height: 160px; object-fit: cover; object-position: top; border-radius: 12px; filter: grayscale(40%) brightness(0.8);" />
        <div>
          <div style="font-family:'Geist Mono',monospace; font-size: 18px; color: #FF7A7A; font-weight: 700;">SITE ANTERIOR</div>
          <div style="font-size: 24px; font-weight: 700; margin-top: 6px;">Visual antigo e demorava 6 segundos</div>
          <div style="font-size: 18px; color: #B8BFC3; margin-top: 4px;">O cliente fechava a aba</div>
        </div>
      </div>

      <!-- Atual -->
      <div style="background: linear-gradient(160deg, rgba(229,185,16,0.18), rgba(6,27,40,0.96)); border: 2.5px solid #E5B910; border-radius: 22px; padding: 22px 24px; display: flex; gap: 24px; align-items: center; box-shadow: 0 20px 60px rgba(0,0,0,0.6);">
        <img src="{safety_new}" style="width: 280px; height: 190px; object-fit: cover; object-position: top; border-radius: 12px;" />
        <div>
          <div style="font-family:'Geist Mono',monospace; font-size: 18px; color: #E5B910; font-weight: 700;">PADRÃO VOCAÇÃO UPDATE</div>
          <div style="font-size: 26px; font-weight: 800; margin-top: 6px;">Autoridade imediata no celular</div>
          <div style="display: inline-block; background: #E5B910; color: #061B28; font-family:'Geist Mono',monospace; font-size: 18px; font-weight: 800; padding: 6px 14px; border-radius: 8px; margin-top: 10px;">
            Carrega em 0.4s no celular
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="foot">
    <span class="meta">Pronto em 5 dias úteis</span>
    <span class="btn">vocacao.digital ↗</span>
  </div>
</div>
</body></html>"""

    # ATO 4 (11.0 a 15.0s): A Frase Coca-Cola + Sonho do Negócio
    c4 = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8" />{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top">
    <div class="brand"><img src="{logo_svg}" /><span>Vocação</span></div>
    <span class="badge">vocacao.digital</span>
  </div>
  
  <div style="margin: auto 0; text-align: center;">
    <div style="display: inline-block; background: rgba(229,185,16,0.14); border: 1px solid rgba(229,185,16,0.4); color: #E5B910; font-family: 'Geist Mono', monospace; font-size: 22px; font-weight: 700; padding: 12px 28px; border-radius: 999px; margin-bottom: 28px;">
      1 empresa por bairro em Sorocaba
    </div>
    
    <h1 class="serif" style="font-size: 108px; line-height: 0.98;">
      O seu trabalho é de primeira linha.<br/>
      <em class="gold">Seu site precisa vender essa mesma certeza.</em>
    </h1>
    
    <p style="margin-top: 36px; font-size: 30px; color: #B8BFC3; line-height: 1.45; max-width: 860px; margin-left: auto; margin-right: auto;">
      Reformamos seu site em 5 dias. Sem reunião e sem mensalidade.
    </p>

    <div style="margin-top: 52px; display: inline-block; background: #E5B910; color: #061B28; font-size: 38px; font-weight: 800; padding: 26px 56px; border-radius: 999px; box-shadow: 0 16px 40px rgba(229,185,16,0.35);">
      Toque em "Saiba mais" ↗
    </div>
  </div>

  <div class="foot">
    <span class="meta">WhatsApp: (15) 98151-2083</span>
    <span class="meta" style="color: #E5B910;">vocacao.digital</span>
  </div>
</div>
</body></html>"""

    scenes = [("cena_1a", c1a), ("cena_1b", c1b), ("cena_2", c2), ("cena_3", c3), ("cena_4", c4)]
    png_paths = []
    for name, content in scenes:
        hpath = BASE_DIR / f"{name}.html"
        ppath = BASE_DIR / f"{name}.png"
        hpath.write_text(content, encoding="utf-8")
        render_html_frame(hpath, ppath, 1080, 1920)
        png_paths.append(ppath)
        print("Rendered frame:", ppath)
    return png_paths


def build_remotion_style_video(png_paths):
    out_mp4 = BASE_DIR / "vocacao-update-motion-inovador-9x16.mp4"
    # Timing:
    # 0: cena_1a (0 a 1.8s) -> pergunta inicial
    # 1: cena_1b (1.8 a 4.4s) -> gancho e subtexto revelado
    # 2: cena_2 (4.4 a 7.6s) -> alívio + 3 pilares
    # 3: cena_3 (7.6 a 11.2s) -> antes vs atual com selo 0.4s
    # 4: cena_4 (11.2 a 15.2s) -> frase coca-cola + sonho + CTA
    filter_complex = (
        "[0:v]scale=1120:1990,zoompan=z='min(zoom+0.0003,1.03)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=54:s=1080x1920:fps=30,format=yuv420p[v0];"
        "[1:v]scale=1120:1990,zoompan=z='min(zoom+0.0003,1.03)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=78:s=1080x1920:fps=30,format=yuv420p[v1];"
        "[2:v]scale=1120:1990,zoompan=z='min(zoom+0.0003,1.03)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=96:s=1080x1920:fps=30,format=yuv420p[v2];"
        "[3:v]scale=1120:1990,zoompan=z='min(zoom+0.0003,1.03)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=108:s=1080x1920:fps=30,format=yuv420p[v3];"
        "[4:v]scale=1120:1990,zoompan=z='min(zoom+0.0003,1.03)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=120:s=1080x1920:fps=30,format=yuv420p[v4];"
        "[v0][v1]xfade=transition=fade:duration=0.25:offset=1.6[vx1];"
        "[vx1][v2]xfade=transition=fadeblack:duration=0.35:offset=4.0[vx2];"
        "[vx2][v3]xfade=transition=slideleft:duration=0.35:offset=7.0[vx3];"
        "[vx3][v4]xfade=transition=fadeblack:duration=0.35:offset=10.4,format=yuv420p[vout]"
    )
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1", "-t", "1.85", "-i", str(png_paths[0]),
        "-loop", "1", "-t", "2.65", "-i", str(png_paths[1]),
        "-loop", "1", "-t", "3.25", "-i", str(png_paths[2]),
        "-loop", "1", "-t", "3.65", "-i", str(png_paths[3]),
        "-loop", "1", "-t", "4.0", "-i", str(png_paths[4]),
        "-f", "lavfi", "-t", "14.2", "-i", "sine=frequency=110:sample_rate=44100",
        "-filter_complex", filter_complex,
        "-af", "lowpass=f=220,volume=0.04,afade=t=in:st=0:d=0.8,afade=t=out:st=13.2:d=0.9",
        "-map", "[vout]",
        "-map", "5:a",
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
    print("Inovative Remotion-style video ready:", out_mp4)
    return out_mp4


if __name__ == "__main__":
    scenes = build_interactive_scenes()
    build_remotion_style_video(scenes)
