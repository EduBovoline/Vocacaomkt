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
    safety_img = (SITE_DIR / "cases" / "safety-novo.png").as_uri()
    maca_img = (SITE_DIR / "cases" / "maca-novo.png").as_uri()

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
      background: radial-gradient(circle at 50% 12%, rgba(229,185,16,0.09) 0%, rgba(4,18,27,1) 75%);
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
      height: 760px;
      border-radius: 28px;
      border: 2px solid rgba(229,185,16,0.35);
      position: relative;
      background: #000;
      box-shadow: 0 20px 60px rgba(0,0,0,0.6);
      overflow: hidden;
    }
    .video-overlay-tag {
      position: absolute;
      top: 24px;
      left: 24px;
      background: rgba(4,18,27,0.88);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(229,185,16,0.4);
      padding: 10px 22px;
      border-radius: 999px;
      display: flex;
      align-items: center;
      gap: 10px;
      color: #FFF;
      font-size: 16px;
      font-weight: 800;
      letter-spacing: 0.04em;
      z-index: 10;
    }
    .bottom-content {
      margin-top: 32px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .safe-footer {
      height: 110px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(255,255,255,0.08);
      padding-top: 14px;
      font-size: 16px;
      color: #94A3B8;
      font-weight: 600;
    }
    """

    # Cena 1: Hipnose pura (0s a 6s) - Sem venda, silêncio/curiosidade
    c1 = f"""<!doctype html><html><head><meta charset="utf-8"/>{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top-header">
    <div class="logo-box">
      <img src="{logo_svg}" class="logo-img"/>
      <span class="brand-title">Vocação Digital</span>
    </div>
    <div class="badge-pill">Experimento Visual</div>
  </div>

  <div class="video-viewport">
    <div class="video-overlay-tag">
      <span style="display:inline-block; width:10px; height:10px; background:#E5B910; border-radius:50%;"></span>
      OBSERVE ATÉ O FINAL
    </div>
  </div>

  <div class="bottom-content" style="justify-content: center; align-items: center; text-align: center;">
    <div>
      <div style="font-size: 40px; font-weight: 800; color: rgba(255,255,255,0.25); letter-spacing: 0.04em;">
        • • •
      </div>
      <div style="font-size: 24px; color: #64748B; font-weight: 600; margin-top: 12px; letter-spacing: 0.02em;">
        (Não pule este vídeo)
      </div>
    </div>

    <div class="safe-footer" style="width: 100%;">
      <span>vocacao.digital</span>
      <span style="color: #64748B;">0:00 / 0:20</span>
    </div>
  </div>
</div>
</body></html>"""

    # Cena 2: A Quebra de Padrão (6s a 9.5s) - "Você ficou preso aqui 6 segundos..."
    c2 = f"""<!doctype html><html><head><meta charset="utf-8"/>{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top-header">
    <div class="logo-box">
      <img src="{logo_svg}" class="logo-img"/>
      <span class="brand-title">Vocação Digital</span>
    </div>
    <div class="badge-pill" style="background: rgba(239,68,68,0.15); border-color: rgba(239,68,68,0.4); color: #F87171;">Atenção Capturada</div>
  </div>

  <div class="video-viewport">
    <div class="video-overlay-tag" style="border-color: #EF4444;">
      <span style="display:inline-block; width:10px; height:10px; background:#EF4444; border-radius:50%;"></span>
      6 SEGUNDOS DE RETENÇÃO
    </div>
  </div>

  <div class="bottom-content">
    <div>
      <div style="font-size: 20px; font-weight: 800; color: #E5B910; letter-spacing: 0.08em; text-transform: uppercase;">
        Você percebeu?
      </div>
      <h1 style="font-size: 52px; font-weight: 900; line-height: 1.12; color: #FFF; margin-top: 10px;">
        Você ficou preso aqui <span style="color: #E5B910;">6 segundos</span>.
      </h1>
      <p style="font-size: 28px; color: #CBD5E1; margin-top: 18px; line-height: 1.45;">
        Imagina se o site da sua empresa <strong>prendesse a atenção do seu cliente</strong> desse mesmo jeito?
      </p>

      <div style="margin-top: 26px; background: rgba(255,255,255,0.04); border-left: 4px solid #E5B910; padding: 18px 24px; border-radius: 0 16px 16px 0;">
        <p style="font-size: 21px; color: #F1F5F9; font-weight: 600;">
          Em vez dele fechar a aba em 3 segundos, ele navega encantado e compra de você. Veja os exemplos a seguir ↴
        </p>
      </div>
    </div>

    <div class="safe-footer">
      <span>vocacao.digital</span>
      <span style="color: #E5B910;">Retenção ➔ Conversão</span>
    </div>
  </div>
</div>
</body></html>"""

    # Cena 3: Case 1 - Safety First (9.5s a 12.5s)
    c3 = f"""<!doctype html><html><head><meta charset="utf-8"/>{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top-header">
    <div class="logo-box">
      <img src="{logo_svg}" class="logo-img"/>
      <span class="brand-title">Sites Vocação</span>
    </div>
    <div class="badge-pill" style="background: rgba(16, 185, 129, 0.15); border-color: rgba(16, 185, 129, 0.4); color: #34D399;">Modelo Real 01</div>
  </div>

  <div class="video-viewport" style="border-color: rgba(16,185,129,0.5);">
    <div class="video-overlay-tag" style="border-color: #10B981;">
      <span style="display:inline-block; width:10px; height:10px; background:#10B981; border-radius:50%;"></span>
      SAFETY FIRST • EPIs & INDÚSTRIA
    </div>
    <img src="{safety_img}" style="width: 100%; height: 100%; object-fit: cover; object-position: top center;"/>
  </div>

  <div class="bottom-content">
    <div>
      <div style="font-size: 18px; font-weight: 800; color: #34D399; letter-spacing: 0.08em; text-transform: uppercase;">
        Caso Real de Modernização
      </div>
      <h1 style="font-size: 46px; font-weight: 900; line-height: 1.15; color: #FFF; margin-top: 8px;">
        Autoridade imediata que gera pedidos de cotação.
      </h1>
      <p style="font-size: 25px; color: #CBD5E1; margin-top: 16px; line-height: 1.4;">
        Design sóbrio, catálogo organizado e carregamento instantâneo. O cliente encontra o que precisa em segundos.
      </p>

      <div style="margin-top: 24px; display: flex; gap: 16px;">
        <span style="background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.3); color: #34D399; font-size: 18px; font-weight: 700; padding: 8px 18px; border-radius: 999px;">
          ⚡ 0.4s de carregamento
        </span>
        <span style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.15); color: #FFF; font-size: 18px; font-weight: 700; padding: 8px 18px; border-radius: 999px;">
          WhatsApp Integrado
        </span>
      </div>
    </div>

    <div class="safe-footer">
      <span>Case: Safety First</span>
      <span style="color: #34D399;">Próximo modelo ➔</span>
    </div>
  </div>
</div>
</body></html>"""

    # Cena 4: Case 2 - Maçã d'Amor (12.5s a 15.5s)
    c4 = f"""<!doctype html><html><head><meta charset="utf-8"/>{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top-header">
    <div class="logo-box">
      <img src="{logo_svg}" class="logo-img"/>
      <span class="brand-title">Sites Vocação</span>
    </div>
    <div class="badge-pill" style="background: rgba(229,185,16,0.15); border-color: rgba(229,185,16,0.4); color: #E5B910;">Modelo Real 02</div>
  </div>

  <div class="video-viewport" style="border-color: rgba(229,185,16,0.5);">
    <div class="video-overlay-tag" style="border-color: #E5B910;">
      <span style="display:inline-block; width:10px; height:10px; background:#E5B910; border-radius:50%;"></span>
      MAÇÃ D'AMOR • CONFEITARIA & EVENTOS
    </div>
    <img src="{maca_img}" style="width: 100%; height: 100%; object-fit: cover; object-position: top center;"/>
  </div>

  <div class="bottom-content">
    <div>
      <div style="font-size: 18px; font-weight: 800; color: #E5B910; letter-spacing: 0.08em; text-transform: uppercase;">
        Cardápio & Venda Direta
      </div>
      <h1 style="font-size: 46px; font-weight: 900; line-height: 1.15; color: #FFF; margin-top: 8px;">
        Do site lento ao cliente pedindo no WhatsApp em 1 clique.
      </h1>
      <p style="font-size: 25px; color: #CBD5E1; margin-top: 16px; line-height: 1.4;">
        Fotos apetitosas, experiência 100% pensada no celular e botão de WhatsApp que converte na hora.
      </p>

      <div style="margin-top: 24px; display: flex; gap: 16px;">
        <span style="background: rgba(229,185,16,0.12); border: 1px solid rgba(229,185,16,0.3); color: #E5B910; font-size: 18px; font-weight: 700; padding: 8px 18px; border-radius: 999px;">
          ✓ De 4.6s para 0.4s
        </span>
        <span style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.15); color: #FFF; font-size: 18px; font-weight: 700; padding: 8px 18px; border-radius: 999px;">
          Alta Conversão
        </span>
      </div>
    </div>

    <div class="safe-footer">
      <span>Case: Maçã d'Amor</span>
      <span style="color: #E5B910;">Veja a oferta ➔</span>
    </div>
  </div>
</div>
</body></html>"""

    # Cena 5: Oferta Vocação Update (15.5s a 20.0s)
    c5 = f"""<!doctype html><html><head><meta charset="utf-8"/>{fonts}<style>{common_css}</style></head>
<body>
<div class="stage">
  <div class="top-header">
    <div class="logo-box">
      <img src="{logo_svg}" class="logo-img"/>
      <span class="brand-title">Vocação Update</span>
    </div>
    <div class="badge-pill">Sem Mensalidade</div>
  </div>

  <div class="video-viewport" style="display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: radial-gradient(circle, rgba(229,185,16,0.15) 0%, rgba(4,18,27,0.95) 80%); padding: 40px;">
    <div style="font-size: 20px; font-weight: 800; color: #E5B910; text-transform: uppercase; letter-spacing: 0.1em;">
      A Oferta Vocação Update
    </div>
    <div style="font-size: 50px; font-weight: 900; color: #FFF; line-height: 1.15; margin-top: 14px;">
      Seu site novo, veloz e vendedor pronto nesta semana.
    </div>
    <div style="font-size: 24px; color: #CBD5E1; margin-top: 16px;">
      Sem reuniões sem fim. Sem escrever nada do zero.
    </div>
  </div>

  <div class="bottom-content">
    <div>
      <div style="background: rgba(229,185,16,0.06); border: 1px solid rgba(229,185,16,0.25); border-radius: 20px; padding: 24px 28px;">
        <div style="font-size: 16px; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">Investimento Único</div>
        <div style="display: flex; align-items: baseline; gap: 14px; margin-top: 6px;">
          <span style="font-size: 56px; font-weight: 900; color: #E5B910; letter-spacing: -0.02em;">R$ 980</span>
          <span style="font-size: 22px; color: #CBD5E1; font-weight: 600;">à vista ou em até 12x</span>
        </div>
        <div style="font-size: 16px; color: #94A3B8; margin-top: 8px;">
          ✓ Entrega em 4 a 5 dias úteis &nbsp;•&nbsp; ✓ Validação PageSpeed &nbsp;•&nbsp; ✓ Foco no WhatsApp
        </div>
      </div>

      <div style="margin-top: 26px; background: #E5B910; color: #04121B; font-size: 32px; font-weight: 900; padding: 22px 36px; border-radius: 999px; text-align: center; box-shadow: 0 16px 40px rgba(229,185,16,0.35);">
        Toque em "Saiba mais" ↗
      </div>
    </div>

    <div class="safe-footer">
      <span>WhatsApp: (15) 98151-2083</span>
      <span style="color: #E5B910; font-weight: 800;">vocacao.digital/vocacao-update</span>
    </div>
  </div>
</div>
</body></html>"""

    scenes = [
        ("meta_cena_1", c1),
        ("meta_cena_2", c2),
        ("meta_cena_3", c3),
        ("meta_cena_4", c4),
        ("meta_cena_5", c5),
    ]
    png_paths = []
    for name, content in scenes:
        hpath = BASE_DIR / f"{name}.html"
        ppath = BASE_DIR / f"{name}.png"
        hpath.write_text(content, encoding="utf-8")
        render_html_frame(hpath, ppath, 1080, 1920)
        png_paths.append(ppath)
        print("Rendered frame:", ppath.name)
    return png_paths


def composite_meta_ad_video(png_paths):
    out_mp4 = BASE_DIR / "vocacao-update-anuncio-meta-retencao-20s.mp4"
    
    # Timeline 20s:
    # 0:00 a 0:06 (6.0s) -> cena 1 (prensa hipnótica + silêncio de venda)
    # 0:06 a 0:09.5 (3.5s) -> cena 2 (você ficou preso 6 segundos...)
    # 0:09.5 a 0:12.5 (3.0s) -> cena 3 (case Safety First)
    # 0:12.5 a 0:15.5 (3.0s) -> cena 4 (case Maçã d'Amor)
    # 0:15.5 a 0:20.0 (4.5s) -> cena 5 (oferta R$ 980 + CTA Saiba Mais)

    # Note: O vídeo da prensa roda durante as cenas 1 e 2 (0 a 9.5s) no topo!
    # A partir de 9.5s, as cenas 3 e 4 trazem os screenshots dos sites dentro da viewport.
    
    filter_complex = (
        "[0:v]trim=0:9.5,setpts=PTS-STARTPTS,scale=980:760:force_original_aspect_ratio=increase,crop=980:760[press_scaled];"
        "[1:v]loop=loop=180:size=1:start=0,setpts=PTS-STARTPTS[bg0];"
        "[2:v]loop=loop=105:size=1:start=0,setpts=PTS-STARTPTS[bg1];"
        "[3:v]loop=loop=90:size=1:start=0,setpts=PTS-STARTPTS[bg2];"
        "[4:v]loop=loop=90:size=1:start=0,setpts=PTS-STARTPTS[bg3];"
        "[5:v]loop=loop=135:size=1:start=0,setpts=PTS-STARTPTS[bg4];"
        "[bg0][bg1]xfade=transition=fade:duration=0.3:offset=5.8[bga];"
        "[bga][bg2]xfade=transition=slideleft:duration=0.3:offset=9.3[bgb];"
        "[bgb][bg3]xfade=transition=slideleft:duration=0.3:offset=12.3[bgc];"
        "[bgc][bg4]xfade=transition=fadeblack:duration=0.35:offset=15.3[bg_full];"
        "[bg_full][press_scaled]overlay=50:164:enable='between(t,0,9.5)',format=yuv420p[vout]"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(PRESS_VIDEO),
        "-i", str(png_paths[0]),
        "-i", str(png_paths[1]),
        "-i", str(png_paths[2]),
        "-i", str(png_paths[3]),
        "-i", str(png_paths[4]),
        "-f", "lavfi", "-t", "20.0", "-i", "sine=frequency=110:sample_rate=44100",
        "-filter_complex", filter_complex,
        "-af", "lowpass=f=220,volume=0.03,afade=t=in:st=0:d=0.5,afade=t=out:st=19.0:d=1.0",
        "-map", "[vout]",
        "-map", "6:a",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        "-t", "20.0",
        str(out_mp4),
    ]

    print("Running FFmpeg composite pipeline for 20s meta-retention ad...")
    subprocess.run(cmd, check=True)
    print("Final MP4 Created successfully:", out_mp4)
    return out_mp4


if __name__ == "__main__":
    pngs = build_scenes()
    composite_meta_ad_video(pngs)
