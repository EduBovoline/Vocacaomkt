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


def render_html_to_png(html_path: Path, out_png: Path, width: int, height: int):
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
            "--virtual-time-budget=4000",
            f"--screenshot={str(out_png.resolve())}",
            uri,
        ]
        subprocess.run(cmd, check=True)
    im = Image.open(out_png)
    if im.size != (width, height):
        im = im.crop((0, 0, width, height))
        im.save(out_png)


def make_video_scenes():
    logo_uri = (SITE_DIR / "logo-vocacao-white-gold.svg").as_uri()
    safety_old = (SITE_DIR / "cases" / "safety-antigo.png").as_uri()
    safety_new = (SITE_DIR / "cases" / "safety-novo.png").as_uri()
    maca_old = (SITE_DIR / "cases" / "maca-antigo.png").as_uri()
    maca_new = (SITE_DIR / "cases" / "maca-novo.png").as_uri()

    common_head = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&family=Geist+Mono:wght@500;600;700&display=swap" rel="stylesheet" />
<style>
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
  .frame {
    position: relative;
    width: 1080px;
    height: 1920px;
    padding: 96px 68px 110px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background:
      radial-gradient(950px 750px at 85% 12%, rgba(229, 185, 16, 0.22), transparent 70%),
      radial-gradient(900px 700px at 15% 88%, rgba(229, 185, 16, 0.12), transparent 70%),
      linear-gradient(180deg, #061B28 0%, #030E16 100%);
  }
  .frame::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(248,249,249,0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(248,249,249,0.035) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
  }
  .top {
    position: relative;
    z-index: 2;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 18px;
  }
  .brand img { height: 52px; }
  .brand span { font-size: 34px; font-weight: 800; letter-spacing: -0.02em; }
  .pill {
    font-family: 'Geist Mono', monospace;
    font-size: 18px;
    font-weight: 700;
    color: #E5B910;
    background: rgba(229, 185, 16, 0.14);
    border: 1.5px solid rgba(229, 185, 16, 0.45);
    padding: 12px 24px;
    border-radius: 999px;
  }
  .serif {
    font-family: 'Instrument Serif', Georgia, serif;
    font-weight: 400;
  }
  .gold { color: #E5B910; }
  .footer-bar {
    position: relative;
    z-index: 2;
    background: rgba(248,249,249,0.06);
    border: 1px solid rgba(248,249,249,0.16);
    border-radius: 24px;
    padding: 26px 34px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .footer-bar .url {
    font-family: 'Geist Mono', monospace;
    font-size: 26px;
    font-weight: 700;
    color: #E5B910;
  }
  .footer-bar .tag {
    font-size: 22px;
    color: #B8BFC3;
    font-weight: 600;
  }
</style>
</head>"""

    # SCENE 1: HOOK (Humanized PT-BR)
    s1 = common_head + f"""
<body>
  <div class="frame">
    <div class="top">
      <div class="brand"><img src="{logo_uri}" /><span>Vocação</span></div>
      <div class="pill">Sorocaba e região</div>
    </div>

    <div style="position:relative;z-index:2;margin:auto 0;">
      <div style="font-family:'Geist Mono',monospace;font-size:23px;color:#E5B910;margin-bottom:26px;">
        Para quem tem empresa em Sorocaba
      </div>
      <h1 class="serif" style="font-size:108px;line-height:0.96;letter-spacing:-0.01em;">
        Tem gente procurando o seu serviço <em class="gold">agora no Google.</em>
      </h1>
      <h2 style="font-size:50px;font-weight:800;margin-top:36px;line-height:1.2;color:#F8F9F9;">
        Eles vão chamar a sua empresa no WhatsApp ou vão fechar com o vizinho?
      </h2>
      <div style="margin-top:52px;display:grid;grid-template-columns:1fr 1fr;gap:24px;">
        <div style="background:rgba(255,77,77,0.12);border:1.5px solid rgba(255,77,77,0.45);border-radius:22px;padding:28px;">
          <div style="font-family:'Geist Mono',monospace;font-size:20px;color:#FF7A7A;font-weight:700;">O que faz perder venda</div>
          <div style="font-size:27px;font-weight:700;margin-top:10px;line-height:1.3;">Google Maps largado e site que demora 6 segundos para abrir</div>
        </div>
        <div style="background:rgba(229,185,16,0.15);border:2px solid #E5B910;border-radius:22px;padding:28px;">
          <div style="font-family:'Geist Mono',monospace;font-size:20px;color:#E5B910;font-weight:700;">Como nós resolvemos</div>
          <div style="font-size:27px;font-weight:700;margin-top:10px;line-height:1.3;">Maps arrumado e site que abre na hora, prontos em até 7 dias</div>
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <span class="tag">Sem mensalidade · 1 empresa por bairro</span>
      <span class="url">vocacao.digital ↗</span>
    </div>
  </div>
</body></html>"""

    # SCENE 2: REAL BEFORE & AFTER PROOF (Humanized PT-BR)
    s2 = common_head + f"""
<body>
  <div class="frame">
    <div class="top">
      <div class="brand"><img src="{logo_uri}" /><span>Vocação</span></div>
      <div class="pill">Antes e depois real</div>
    </div>

    <div style="position:relative;z-index:2;">
      <h1 class="serif" style="font-size:86px;line-height:1.0;">
        No balcão a sua empresa passa confiança. <em class="gold">No celular, ela precisa passar também.</em>
      </h1>

      <div style="margin-top:36px;display:flex;flex-direction:column;gap:28px;">
        <div style="background:rgba(255,255,255,0.03);border:1.5px solid rgba(255,90,90,0.4);border-radius:24px;padding:22px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
            <span style="background:rgba(255,77,77,0.2);color:#FF7A7A;font-family:'Geist Mono',monospace;font-size:20px;font-weight:700;padding:8px 18px;border-radius:10px;">Como era antes</span>
            <span style="font-family:'Geist Mono',monospace;font-size:22px;color:#B8BFC3;">Lento e difícil de ler no celular</span>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;height:360px;">
            <img src="{safety_old}" style="width:100%;height:100%;object-fit:cover;object-position:top;border-radius:14px;filter:grayscale(35%) brightness(0.8);" />
            <img src="{maca_old}" style="width:100%;height:100%;object-fit:cover;object-position:top;border-radius:14px;filter:grayscale(35%) brightness(0.8);" />
          </div>
        </div>

        <div style="background:linear-gradient(160deg,rgba(229,185,16,0.2),rgba(6,27,40,0.95));border:2.5px solid #E5B910;border-radius:24px;padding:22px;box-shadow:0 20px 60px rgba(0,0,0,0.6);">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
            <span style="background:#E5B910;color:#061B28;font-family:'Geist Mono',monospace;font-size:20px;font-weight:800;padding:8px 18px;border-radius:10px;">Depois da Vocação</span>
            <span style="font-family:'Geist Mono',monospace;font-size:24px;color:#E5B910;font-weight:700;">Abre em 0.4 segundo</span>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;height:400px;">
            <img src="{safety_new}" style="width:100%;height:100%;object-fit:cover;object-position:top;border-radius:14px;" />
            <img src="{maca_new}" style="width:100%;height:100%;object-fit:cover;object-position:top;border-radius:14px;" />
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <span class="tag">Aproveitamos seus textos atuais · Sem reunião longa</span>
      <span class="url">vocacao.digital ↗</span>
    </div>
  </div>
</body></html>"""

    # SCENE 3: THE 4 REAL OFFERS & PRICES (Humanized PT-BR)
    s3 = common_head + f"""
<body>
  <div class="frame">
    <div class="top">
      <div class="brand"><img src="{logo_uri}" /><span>Vocação</span></div>
      <div class="pill">Preço fechado no site</div>
    </div>

    <div style="position:relative;z-index:2;">
      <div style="font-family:'Geist Mono',monospace;font-size:22px;color:#E5B910;margin-bottom:16px;">
        Você paga uma vez só e não fica preso em mensalidade
      </div>
      <h1 class="serif" style="font-size:88px;line-height:0.98;">
        Escolha só o que a sua empresa <em class="gold">precisa hoje:</em>
      </h1>

      <div style="margin-top:42px;display:flex;flex-direction:column;gap:22px;">
        <div style="background:rgba(248,249,249,0.05);border:1.5px solid rgba(184,191,195,0.3);border-radius:24px;padding:28px 34px;display:flex;justify-content:space-between;align-items:center;">
          <div>
            <div style="font-size:32px;font-weight:800;">1. Google Maps completo</div>
            <div style="font-size:22px;color:#B8BFC3;margin-top:6px;">Sua ficha organizada para aparecer nas buscas do seu bairro</div>
          </div>
          <div style="text-align:right;font-family:'Geist Mono',monospace;">
            <div style="font-size:44px;font-weight:700;color:#E5B910;">R$ 450</div>
            <div style="font-size:18px;color:#B8BFC3;">Valor único</div>
          </div>
        </div>

        <div style="background:rgba(248,249,249,0.05);border:1.5px solid rgba(184,191,195,0.3);border-radius:24px;padding:28px 34px;display:flex;justify-content:space-between;align-items:center;">
          <div>
            <div style="font-size:32px;font-weight:800;">2. Tour Virtual 360° no Google</div>
            <div style="font-size:22px;color:#B8BFC3;margin-top:6px;">O cliente conhece sua loja por dentro direto pelo Google Maps</div>
          </div>
          <div style="text-align:right;font-family:'Geist Mono',monospace;">
            <div style="font-size:44px;font-weight:700;color:#E5B910;">R$ 750</div>
            <div style="font-size:18px;color:#B8BFC3;">Pronto em 5 dias</div>
          </div>
        </div>

        <div style="background:rgba(229,185,16,0.14);border:2.5px solid #E5B910;border-radius:24px;padding:30px 34px;display:flex;justify-content:space-between;align-items:center;">
          <div>
            <div style="font-size:34px;font-weight:800;color:#F8F9F9;">3. Vocação Start (Site + Maps)</div>
            <div style="font-size:22px;color:#F8F9F9;opacity:0.9;margin-top:6px;">Para quem ainda não tem site: página rápida + Google Maps</div>
          </div>
          <div style="text-align:right;font-family:'Geist Mono',monospace;">
            <div style="font-size:46px;font-weight:700;color:#E5B910;">R$ 850</div>
            <div style="font-size:18px;color:#E5B910;">Pronto em 7 dias</div>
          </div>
        </div>

        <div style="background:rgba(229,185,16,0.14);border:2.5px solid #E5B910;border-radius:24px;padding:30px 34px;display:flex;justify-content:space-between;align-items:center;">
          <div>
            <div style="font-size:34px;font-weight:800;color:#F8F9F9;">4. Vocação Update (Reforma de site)</div>
            <div style="font-size:22px;color:#F8F9F9;opacity:0.9;margin-top:6px;">Seu site antigo refeito do zero em 5 dias sem você escrever nada</div>
          </div>
          <div style="text-align:right;font-family:'Geist Mono',monospace;">
            <div style="font-size:46px;font-weight:700;color:#E5B910;">R$ 980</div>
            <div style="font-size:18px;color:#E5B910;">Pronto em 5 dias</div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <span class="tag">50% no início e 50% só depois que aprovar no ar</span>
      <span class="url">vocacao.digital ↗</span>
    </div>
  </div>
</body></html>"""

    # SCENE 4: GUARANTEE + CTA (Humanized PT-BR)
    s4 = common_head + f"""
<body>
  <div class="frame">
    <div class="top">
      <div class="brand"><img src="{logo_uri}" /><span>Vocação</span></div>
      <div class="pill">Pagamento 50/50</div>
    </div>

    <div style="position:relative;z-index:2;text-align:center;padding:0 12px;">
      <div style="display:inline-block;background:rgba(229,185,16,0.16);border:1.5px solid #E5B910;color:#E5B910;font-family:'Geist Mono',monospace;font-size:23px;font-weight:700;padding:14px 30px;border-radius:999px;margin-bottom:34px;">
        Atendemos só 1 empresa de cada ramo por bairro
      </div>
      <h1 class="serif" style="font-size:106px;line-height:0.96;">
        Você só paga a segunda metade <em class="gold">depois de ver tudo pronto no ar.</em>
      </h1>
      <p style="font-size:32px;color:#B8BFC3;margin-top:34px;line-height:1.4;font-weight:500;">
        Entre no site e peça uma <strong style="color:#F8F9F9;">avaliação gratuita</strong> de como a sua empresa aparece hoje no Google Maps e no celular.
      </p>

      <div style="margin-top:64px;background:#E5B910;color:#061B28;border-radius:28px;padding:38px 44px;box-shadow:0 24px 60px rgba(229,185,16,0.4);">
        <div style="font-family:'Geist Mono',monospace;font-size:22px;font-weight:700;">
          Toque em "Saiba mais" ou acesse:
        </div>
        <div style="font-size:64px;font-weight:800;margin-top:8px;letter-spacing:-0.02em;">
          vocacao.digital ↗
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <span class="tag">Sorocaba e região · Entrega em 5 a 7 dias úteis</span>
      <span class="url">WhatsApp: (15) 98151-2083</span>
    </div>
  </div>
</body></html>"""

    scenes = [s1, s2, s3, s4]
    png_paths = []
    for idx, html_content in enumerate(scenes, start=1):
        hpath = BASE_DIR / f"scene_{idx}.html"
        ppath = BASE_DIR / f"scene_{idx}.png"
        hpath.write_text(html_content, encoding="utf-8")
        render_html_to_png(hpath, ppath, 1080, 1920)
        png_paths.append(ppath)
    return png_paths


def build_video(png_paths):
    out_mp4 = BASE_DIR / "anuncio-01-video-reels-9x16.mp4"
    filter_complex = (
        "[0:v]scale=1140:2026,zoompan=z='min(zoom+0.0004,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=114:s=1080x1920:fps=30,format=yuv420p[v0];"
        "[1:v]scale=1140:2026,zoompan=z='min(zoom+0.0004,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=120:s=1080x1920:fps=30,format=yuv420p[v1];"
        "[2:v]scale=1140:2026,zoompan=z='min(zoom+0.0004,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=126:s=1080x1920:fps=30,format=yuv420p[v2];"
        "[3:v]scale=1140:2026,zoompan=z='min(zoom+0.0004,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=114:s=1080x1920:fps=30,format=yuv420p[v3];"
        "[v0][v1]xfade=transition=fadeblack:duration=0.4:offset=3.4[vx1];"
        "[vx1][v2]xfade=transition=slideleft:duration=0.4:offset=7.0[vx2];"
        "[vx2][v3]xfade=transition=fadeblack:duration=0.4:offset=10.8,format=yuv420p[vout]"
    )
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1", "-t", "3.8", "-i", str(png_paths[0]),
        "-loop", "1", "-t", "4.0", "-i", str(png_paths[1]),
        "-loop", "1", "-t", "4.2", "-i", str(png_paths[2]),
        "-loop", "1", "-t", "3.8", "-i", str(png_paths[3]),
        "-f", "lavfi", "-t", "14.6", "-i", "sine=frequency=110:sample_rate=44100",
        "-filter_complex", filter_complex,
        "-af", "lowpass=f=240,volume=0.06,afade=t=in:st=0:d=0.8,afade=t=out:st=13.5:d=1.1",
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
    return out_mp4


if __name__ == "__main__":
    static_html = BASE_DIR / "anuncio-01-estatico.html"
    static_png = BASE_DIR / "anuncio-01-estatico-feed-4x5.png"
    print("Rendering humanized static ad...")
    render_html_to_png(static_html, static_png, 1080, 1350)
    print("Static ad saved:", static_png)

    print("Rendering humanized video scenes...")
    scenes = make_video_scenes()
    print("Building humanized MP4 video...")
    mp4 = build_video(scenes)
    print("Video saved:", mp4)
