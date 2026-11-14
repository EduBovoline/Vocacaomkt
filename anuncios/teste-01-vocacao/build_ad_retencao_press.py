import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
SITE_DIR = (BASE_DIR.parent.parent / "Site").resolve()
ASSETS_DIR = BASE_DIR / "assets"
PRESS_VIDEO = ASSETS_DIR / "press_cut.mp4"

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


def build_scenes():
    logo_svg = (SITE_DIR / "logo-vocacao-white-gold.svg").as_uri()
    safety_old = (SITE_DIR / "cases" / "safety-antigo.png").as_uri()
    safety_new = (SITE_DIR / "cases" / "safety-novo.png").as_uri()

    fonts = """
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800;900&family=Geist+Mono:wght@500;600;700&display=swap" rel="stylesheet" />
    """

    common_css = """
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body {
      width: 1080px;
      height: 1920px;
      overflow: hidden;
      background: #04121B;
      color: #F8F9F9;
      font-family: 'Manrope', sans-serif;
      -webkit-font-smoothing: antialiased;
    }
    .stage {
      width: 1080px;
      height: 1920px;
      position: relative;
      background: radial-gradient(circle at 50% 15%, rgba(229,185,16,0.08) 0%, rgba(4,18,27,1) 70%);
      padding: 60px 50px;
      display: flex;
      flex-direction: column;
    }
    .top-header {
      height: 80px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      padding-bottom: 20px;
    }
    .logo-box {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .logo-img {
      height: 38px;
    }
    .brand-title {
      font-size: 20px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #F8F9F9;
    }
    .badge-pill {
      background: rgba(229,185,16,0.12);
      border: 1px solid rgba(229,185,16,0.35);
      color: #E5B910;
      font-size: 15px;
      font-weight: 700;
      padding: 6px 16px;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .video-viewport {
      margin-top: 24px;
      width: 980px;
      height: 840px;
      border-radius: 28px;
      border: 2px solid rgba(229,185,16,0.3);
      position: relative;
      background: #000;
      box-shadow: 0 20px 60px rgba(0,0,0,0.6);
      overflow: hidden;
    }
    .video-overlay-tag {
      position: absolute;
      top: 24px;
      left: 24px;
      background: rgba(4,18,27,0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(229,185,16,0.4);
      padding: 10px 22px;
      border-radius: 999px;
      display: flex;
      align-items: center;
      gap: 10px;
      color: #FFF;
      font-size: 17px;
      font-weight: 800;
      letter-spacing: 0.04em;
      z-index: 10;
    }
    .bottom-content {
      margin-top: 36px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .safe-footer {
      height: 120px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(255,255,255,0.08);
      padding-top: 16px;
      font-size: 17px;
      color: #94A3B8;
      font-weight: 600;
    }
    """

    # Scene 1: O Choque de Realidade (0 a 4.5s)
    c1 = f"""<!doctype html><html><head><meta charset="utf-8"/>{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top-header">
    <div class="logo-box">
      <img src="{logo_svg}" class="logo-img"/>
      <span class="brand-title">Vocação Digital</span>
    </div>
    <div class="badge-pill">Diagnóstico Visual</div>
  </div>

  <div class="video-viewport">
    <div class="video-overlay-tag">
      <span style="display:inline-block; width:12px; height:12px; background:#EF4444; border-radius:50%;"></span>
      É ASSIM QUE SEU SITE TRATA SEU CLIENTE
    </div>
  </div>

  <div class="bottom-content">
    <div>
      <h1 style="font-size: 52px; font-weight: 900; line-height: 1.12; color: #FFF; margin-top: 10px;">
        Seu site demora mais de 3 segundos pra abrir?
      </h1>
      <p style="font-size: 27px; color: #CBD5E1; margin-top: 20px; line-height: 1.45;">
        Ele está literalmente <strong style="color: #EF4444;">esmagando seu faturamento</strong>. Quem entra no celular não espera: fecha a aba e vai direto pro seu concorrente.
      </p>
      
      <div style="margin-top: 32px; background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 18px; padding: 22px 28px; display: flex; align-items: center; gap: 20px;">
        <span style="font-size: 38px;">🚨</span>
        <div style="font-size: 21px; color: #FCA5A5; font-weight: 700; line-height: 1.35;">
          53% dos visitantes abandonam páginas que levam mais de 3 segundos para carregar no celular.
        </div>
      </div>
    </div>

    <div class="safe-footer">
      <span>vocacao.digital/vocacao-update</span>
      <span style="color: #E5B910;">Modernização Expressa 4 a 5 dias</span>
    </div>
  </div>
</div>
</body></html>"""

    # Scene 2: A Solução e Prova (4.5 a 9.5s)
    c2 = f"""<!doctype html><html><head><meta charset="utf-8"/>{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top-header">
    <div class="logo-box">
      <img src="{logo_svg}" class="logo-img"/>
      <span class="brand-title">Vocação Update</span>
    </div>
    <div class="badge-pill" style="background: rgba(16, 185, 129, 0.15); border-color: rgba(16, 185, 129, 0.4); color: #34D399;">Case Real</div>
  </div>

  <div class="video-viewport">
    <div class="video-overlay-tag">
      <span style="display:inline-block; width:12px; height:12px; background:#10B981; border-radius:50%;"></span>
      TRANSFORMAÇÃO COMPLETA
    </div>
  </div>

  <div class="bottom-content">
    <div>
      <h1 style="font-size: 50px; font-weight: 900; line-height: 1.12; color: #FFF; margin-top: 10px;">
        Do site pesado ao carregamento em <span style="color: #E5B910;">0.4 segundos</span>.
      </h1>
      <p style="font-size: 26px; color: #CBD5E1; margin-top: 18px; line-height: 1.45;">
        A gente pega tudo o que sua empresa já tem e moderniza a estrutura inteira. Sem reuniões sem fim e sem você precisar escrever nada do zero.
      </p>

      <div style="margin-top: 26px; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
        <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 20px; text-align: center;">
          <div style="font-size: 15px; color: #94A3B8; text-transform: uppercase; font-weight: 700;">Antes</div>
          <div style="font-size: 38px; font-weight: 900; color: #EF4444; margin-top: 6px;">4.6s</div>
          <div style="font-size: 15px; color: #94A3B8; margin-top: 4px;">Lento no Mobile</div>
        </div>
        <div style="background: rgba(229,185,16,0.08); border: 1px solid rgba(229,185,16,0.4); border-radius: 16px; padding: 20px; text-align: center;">
          <div style="font-size: 15px; color: #E5B910; text-transform: uppercase; font-weight: 800;">Depois</div>
          <div style="font-size: 38px; font-weight: 900; color: #34D399; margin-top: 6px;">0.4s</div>
          <div style="font-size: 15px; color: #E5B910; margin-top: 4px;">Direto no WhatsApp</div>
        </div>
      </div>
    </div>

    <div class="safe-footer">
      <span>Entrega expressa garantida</span>
      <span style="color: #E5B910;">Pronto nesta semana</span>
    </div>
  </div>
</div>
</body></html>"""

    # Scene 3: A Oferta Irrecusável e CTA (9.5 a 15s)
    c3 = f"""<!doctype html><html><head><meta charset="utf-8"/>{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top-header">
    <div class="logo-box">
      <img src="{logo_svg}" class="logo-img"/>
      <span class="brand-title">Vocação Update</span>
    </div>
    <div class="badge-pill">Sem Mensalidade</div>
  </div>

  <div class="video-viewport">
    <div class="video-overlay-tag">
      <span style="display:inline-block; width:12px; height:12px; background:#E5B910; border-radius:50%;"></span>
      OFERTA OFICIAL
    </div>
  </div>

  <div class="bottom-content">
    <div>
      <h1 style="font-size: 52px; font-weight: 900; line-height: 1.15; color: #FFF; margin-top: 10px;">
        Site novo, ágil e vendedor em 4 a 5 dias úteis.
      </h1>
      
      <div style="margin-top: 24px; background: rgba(229,185,16,0.06); border: 1px solid rgba(229,185,16,0.25); border-radius: 20px; padding: 24px 28px;">
        <div style="font-size: 16px; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">Investimento Único</div>
        <div style="display: flex; align-items: baseline; gap: 14px; margin-top: 6px;">
          <span style="font-size: 54px; font-weight: 900; color: #E5B910; letter-spacing: -0.02em;">R$ 980</span>
          <span style="font-size: 22px; color: #CBD5E1; font-weight: 600;">à vista ou em até 12x</span>
        </div>
        <div style="font-size: 16px; color: #94A3B8; margin-top: 8px;">
          ✓ Código ultraleve &nbsp;•&nbsp; ✓ Validação PageSpeed &nbsp;•&nbsp; ✓ Botão WhatsApp
        </div>
      </div>

      <div style="margin-top: 30px; background: #E5B910; color: #04121B; font-size: 30px; font-weight: 900; padding: 22px 36px; border-radius: 999px; text-align: center; box-shadow: 0 16px 40px rgba(229,185,16,0.35);">
        Toque em "Saiba mais" ↗
      </div>
    </div>

    <div class="safe-footer">
      <span>WhatsApp direto: (15) 98151-2083</span>
      <span style="color: #E5B910; font-weight: 800;">vocacao.digital</span>
    </div>
  </div>
</div>
</body></html>"""

    scenes = [("retencao_cena_1", c1), ("retencao_cena_2", c2), ("retencao_cena_3", c3)]
    png_paths = []
    for name, content in scenes:
        hpath = BASE_DIR / f"{name}.html"
        ppath = BASE_DIR / f"{name}.png"
        hpath.write_text(content, encoding="utf-8")
        render_html_frame(hpath, ppath, 1080, 1920)
        png_paths.append(ppath)
        print("Rendered frame:", ppath.name)
    return png_paths


def composite_ad_video(png_paths):
    out_mp4 = BASE_DIR / "vocacao-update-anuncio-retencao-prensa-9x16.mp4"
    
    # 0: video da prensa (recortado e posicionado na viewport: x=50, y=164, w=980, h=840)
    # 1: cena 1 (0 a 4.5s)
    # 2: cena 2 (4.5 a 9.5s)
    # 3: cena 3 (9.5 a 15.0s)
    
    filter_complex = (
        "[0:v]trim=0:15,setpts=PTS-STARTPTS,scale=980:840:force_original_aspect_ratio=increase,crop=980:840[press_scaled];"
        "[1:v]loop=loop=135:size=1:start=0,setpts=PTS-STARTPTS[bg0];"
        "[2:v]loop=loop=150:size=1:start=0,setpts=PTS-STARTPTS[bg1];"
        "[3:v]loop=loop=165:size=1:start=0,setpts=PTS-STARTPTS[bg2];"
        "[bg0][bg1]xfade=transition=fade:duration=0.3:offset=4.3[bg_m1];"
        "[bg_m1][bg2]xfade=transition=fade:duration=0.3:offset=9.2[bg_full];"
        "[bg_full][press_scaled]overlay=50:164:enable='between(t,0,15)',format=yuv420p[vout]"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(PRESS_VIDEO),
        "-i", str(png_paths[0]),
        "-i", str(png_paths[1]),
        "-i", str(png_paths[2]),
        "-f", "lavfi", "-t", "15.0", "-i", "sine=frequency=110:sample_rate=44100",
        "-filter_complex", filter_complex,
        "-af", "lowpass=f=220,volume=0.03,afade=t=in:st=0:d=0.5,afade=t=out:st=14.2:d=0.8",
        "-map", "[vout]",
        "-map", "4:a",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        "-t", "15.0",
        str(out_mp4),
    ]

    print("Running FFmpeg composite pipeline...")
    subprocess.run(cmd, check=True)
    print("Final MP4 Created successfully:", out_mp4)
    return out_mp4


if __name__ == "__main__":
    pngs = build_scenes()
    composite_ad_video(pngs)
