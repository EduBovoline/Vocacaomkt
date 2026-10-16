import json
import os

def generate_subcrm():
    with open('leads_100_santa_rosalia_brasilandia.json', 'r', encoding='utf-8') as f:
        leads_100 = json.load(f)

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vocação 2027 · Sub-CRM Executivo & Cockpit em Tempo Real</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-main: #0a0f0d;
    --bg-card: #121915;
    --bg-card-hover: #17221d;
    --border: #1f2b24;
    --border-light: #2a3c32;
    --primary: #128263;
    --primary-light: #18a981;
    --accent: #79f2c3;
    --gold: #e5a43b;
    --gold-light: #ffd27a;
    --danger: #ef4444;
    --text-main: #eef5f1;
    --text-muted: #88a397;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background-color: var(--bg-main);
    color: var(--text-main);
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    min-height: 100vh;
    padding-bottom: 80px;
    -webkit-font-smoothing: antialiased;
  }}

  /* TOP COCKPIT BAR */
  .topbar {{
    background: rgba(18, 25, 21, 0.96);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(14px);
    position: sticky;
    top: 0;
    z-index: 100;
    padding: 12px 20px;
  }}
  .topbar-inner {{
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }}
  .brand-group {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .brand-logo {{
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: linear-gradient(135deg, var(--primary) 0%, #063c2e 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Fraunces', serif;
    font-weight: 700;
    font-size: 20px;
    color: #ffffff;
    border: 1px solid var(--border-light);
    box-shadow: 0 4px 12px rgba(18, 130, 99, 0.25);
  }}
  .brand-text h1 {{
    font-size: 16px;
    font-weight: 800;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .brand-text p {{
    font-size: 11px;
    color: var(--text-muted);
  }}
  .live-pill {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 10.5px;
    font-weight: 700;
    background: rgba(18, 130, 99, 0.2);
    color: #79f2c3;
    padding: 2px 8px;
    border-radius: 12px;
    border: 1px solid rgba(121, 242, 195, 0.3);
  }}
  .live-dot {{
    width: 7px;
    height: 7px;
    background: #79f2c3;
    border-radius: 50%;
    box-shadow: 0 0 8px #79f2c3;
    animation: pulse 1.8s infinite;
  }}
  @keyframes pulse {{
    0%, 100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.4; transform: scale(0.85); }}
  }}

  .top-actions {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }}
  .btn-action {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12.5px;
    font-weight: 700;
    padding: 8px 14px;
    border-radius: 8px;
    border: 1px solid var(--border);
    cursor: pointer;
    text-decoration: none;
    transition: all 0.2s;
  }}
  .btn-crm {{
    background: #18241f;
    color: var(--accent);
    border-color: rgba(121, 242, 195, 0.35);
  }}
  .btn-crm:hover {{
    background: #20312a;
    transform: translateY(-1px);
  }}
  .btn-queue {{
    background: rgba(229, 164, 59, 0.15);
    color: var(--gold-light);
    border-color: rgba(229, 164, 59, 0.4);
  }}
  .btn-queue.paused {{
    background: rgba(239, 68, 68, 0.15);
    color: #fca5a5;
    border-color: rgba(239, 68, 68, 0.4);
  }}

  /* TABS */
  .tabs-bar {{
    max-width: 1400px;
    margin: 16px auto 0 auto;
    padding: 0 20px;
    display: flex;
    gap: 8px;
    border-bottom: 1px solid var(--border);
    overflow-x: auto;
  }}
  .tab-btn {{
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-size: 13.5px;
    font-weight: 700;
    padding: 12px 18px;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 8px;
    white-space: nowrap;
  }}
  .tab-btn:hover {{ color: var(--text-main); }}
  .tab-btn.active {{
    color: var(--accent);
    border-bottom-color: var(--accent);
  }}
  .tab-badge {{
    background: #18231e;
    color: var(--text-muted);
    font-size: 10.5px;
    font-weight: 800;
    padding: 2px 7px;
    border-radius: 10px;
  }}
  .tab-btn.active .tab-badge {{
    background: rgba(18, 130, 99, 0.3);
    color: var(--accent);
  }}

  /* MAIN CONTAINER */
  .container {{
    max-width: 1400px;
    margin: 20px auto;
    padding: 0 20px;
  }}
  .tab-panel {{ display: none; }}
  .tab-panel.active {{ display: block; }}

  /* METRICS ROW */
  .metrics-row {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }}
  .metric-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px 20px;
    position: relative;
    overflow: hidden;
  }}
  .metric-card.gold {{ border-color: rgba(229, 164, 59, 0.35); }}
  .metric-card.accent {{ border-color: rgba(121, 242, 195, 0.35); }}
  .metric-label {{
    font-size: 11.5px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .metric-value {{
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
    margin: 6px 0 2px 0;
    font-family: 'Fraunces', serif;
  }}
  .metric-sub {{
    font-size: 11px;
    color: var(--text-muted);
  }}

  /* QUEUE MONITOR GRID */
  .queue-monitor-grid {{
    display: grid;
    grid-template-columns: 320px 1fr;
    gap: 20px;
    margin-bottom: 24px;
  }}
  @media (max-width: 900px) {{
    .queue-monitor-grid {{ grid-template-columns: 1fr; }}
  }}

  /* RADIAL CARD */
  .radial-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }}
  .radial-circle-box {{
    position: relative;
    width: 170px;
    height: 170px;
    margin: 16px 0;
  }}
  .radial-svg {{
    transform: rotate(-90deg);
    width: 100%;
    height: 100%;
  }}
  .circle-bg {{
    fill: none;
    stroke: #18231e;
    stroke-width: 12;
  }}
  .circle-progress {{
    fill: none;
    stroke: url(#emeraldGradient);
    stroke-width: 12;
    stroke-linecap: round;
    stroke-dasharray: 440;
    stroke-dashoffset: 440;
    transition: stroke-dashoffset 1s ease-in-out;
  }}
  .radial-center-text {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .radial-pct {{
    font-size: 32px;
    font-weight: 800;
    font-family: 'Fraunces', serif;
    color: #ffffff;
  }}
  .radial-sub {{
    font-size: 10.5px;
    color: var(--text-muted);
    font-weight: 600;
  }}

  /* QUEUE CONTROLS & TIMELINE CARD */
  .queue-control-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .countdown-box {{
    background: #0d1511;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 16px;
  }}
  .countdown-info h3 {{
    font-size: 14px;
    font-weight: 800;
    color: #ffffff;
  }}
  .countdown-info p {{
    font-size: 12px;
    color: var(--text-muted);
  }}
  .countdown-timer {{
    font-family: 'Fraunces', monospace;
    font-size: 28px;
    font-weight: 800;
    color: var(--accent);
    background: rgba(18, 130, 99, 0.2);
    padding: 4px 14px;
    border-radius: 8px;
    border: 1px solid rgba(121, 242, 195, 0.3);
  }}
  .btn-skip {{
    background: #17241e;
    color: var(--text-main);
    border: 1px solid var(--border);
    padding: 8px 14px;
    font-size: 12px;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .btn-skip:hover {{
    background: var(--primary);
    color: #ffffff;
    border-color: var(--accent);
  }}

  /* SEGMENTED PROGRESS BAR */
  .segmented-bar-container {{
    margin-bottom: 20px;
  }}
  .seg-bar {{
    display: flex;
    height: 12px;
    border-radius: 6px;
    overflow: hidden;
    background: #16221c;
    margin-top: 8px;
  }}
  .seg-part {{ transition: width 0.6s ease; }}
  .seg-part.sent {{ background: var(--accent); }}
  .seg-part.failed {{ background: var(--danger); }}
  .seg-part.pending {{ background: #26382f; }}

  .seg-legend {{
    display: flex;
    gap: 16px;
    margin-top: 8px;
    font-size: 11.5px;
    color: var(--text-muted);
  }}
  .seg-item {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .seg-color {{
    width: 9px;
    height: 9px;
    border-radius: 3px;
  }}

  /* TICKER */
  .ticker-box {{
    background: #0b110e;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 14px;
    font-size: 12px;
    max-height: 110px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .ticker-item {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: monospace;
    font-size: 11.5px;
  }}

  /* INBOX GRID */
  .inbox-grid {{
    display: grid;
    grid-template-columns: 360px 1fr;
    gap: 20px;
  }}
  @media (max-width: 900px) {{
    .inbox-grid {{ grid-template-columns: 1fr; }}
  }}
  .chat-list-panel {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    height: 720px;
    overflow-y: auto;
  }}
  .chat-item {{
    padding: 14px 16px;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    transition: background 0.15s;
  }}
  .chat-item:hover {{ background: #16231c; }}
  .chat-item.active {{
    background: #182720;
    border-left: 3px solid var(--accent);
  }}
  .chat-item-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 4px;
  }}
  .chat-item-name {{
    font-weight: 700;
    font-size: 13.5px;
    color: #ffffff;
  }}
  .chat-item-time {{
    font-size: 11px;
    color: var(--text-muted);
  }}
  .chat-item-preview {{
    font-size: 12px;
    color: var(--text-muted);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: 1.4;
  }}

  /* CHAT VIEW PANEL */
  .chat-view-panel {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    height: 720px;
  }}
  .chat-view-header {{
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #111a15;
    flex-wrap: wrap;
    gap: 10px;
  }}

  /* LEAD HUD / FICHA RÁPIDA */
  .lead-hud-card {{
    background: #0c1511;
    border-bottom: 1px solid var(--border);
    padding: 12px 18px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .lead-hud-row1 {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
  }}
  .lead-hud-pills {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }}
  .hud-pill {{
    font-size: 11px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }}
  .hud-pill.niche {{
    background: rgba(18, 130, 99, 0.25);
    color: #79f2c3;
    border: 1px solid rgba(121, 242, 195, 0.3);
  }}
  .hud-pill.bairro {{
    background: #18251f;
    color: var(--text-muted);
    border: 1px solid var(--border);
  }}
  .hud-pill.offer {{
    background: rgba(229, 164, 59, 0.2);
    color: #ffd27a;
    border: 1px solid rgba(229, 164, 59, 0.4);
  }}
  .lead-hud-actions {{
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
  }}
  .btn-hud {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 11.5px;
    font-weight: 700;
    padding: 6px 11px;
    border-radius: 6px;
    text-decoration: none;
    transition: all 0.15s ease;
    border: 1px solid transparent;
    cursor: pointer;
  }}
  .btn-hud:hover {{ transform: translateY(-1px); }}
  .btn-hud-maps {{
    background: rgba(66, 133, 244, 0.15);
    color: #8ab4f8;
    border-color: rgba(66, 133, 244, 0.35);
  }}
  .btn-hud-maps:hover {{ background: rgba(66, 133, 244, 0.28); color: #aecbfa; }}
  .btn-hud-insta {{
    background: rgba(225, 48, 108, 0.15);
    color: #ff85a2;
    border-color: rgba(225, 48, 108, 0.35);
  }}
  .btn-hud-insta:hover {{ background: rgba(225, 48, 108, 0.28); color: #ffa3b8; }}
  .btn-hud-wa {{
    background: rgba(37, 211, 102, 0.15);
    color: #48bb78;
    border-color: rgba(37, 211, 102, 0.35);
  }}
  .btn-hud-wa:hover {{ background: rgba(37, 211, 102, 0.28); color: #68d391; }}
  .btn-hud-site {{
    background: #1c2b23;
    color: #c0ded2;
    border-color: var(--border-light);
  }}
  .btn-hud-site:hover {{ background: #24382e; color: #fff; }}

  .lead-hud-row2 {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    font-size: 12px;
    color: var(--text-muted);
    border-top: 1px dashed #1a2720;
    padding-top: 8px;
    flex-wrap: wrap;
  }}
  .lead-hud-detail {{
    display: flex;
    gap: 5px;
    align-items: center;
  }}
  .hud-strong {{
    color: #e2ede8;
    font-weight: 600;
  }}
  .hud-presence-highlight {{
    background: rgba(18, 130, 99, 0.15);
    color: #a3e9ce;
    padding: 3px 8px;
    border-radius: 4px;
    font-style: italic;
    border: 1px solid rgba(18, 130, 99, 0.25);
  }}

  /* CHAT MESSAGES */
  .chat-messages {{
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .chat-bubble {{
    max-width: 80%;
    padding: 12px 16px;
    border-radius: 12px;
    font-size: 13.5px;
    line-height: 1.45;
  }}
  .chat-bubble.inbound {{
    align-self: flex-start;
    background: #1c2722;
    border: 1px solid var(--border);
    color: #e2ede8;
    border-bottom-left-radius: 2px;
  }}
  .chat-bubble.outbound {{
    align-self: flex-end;
    background: #128263;
    color: #ffffff;
    border-bottom-right-radius: 2px;
  }}
  .bubble-meta {{
    font-size: 10.5px;
    opacity: 0.75;
    margin-top: 4px;
    text-align: right;
  }}
  .chat-view-footer {{
    padding: 14px 20px;
    border-top: 1px solid var(--border);
    background: #111a15;
    display: flex;
    gap: 10px;
  }}
  .chat-input {{
    flex: 1;
    background: #0b100e;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 14px;
    color: #ffffff;
    font-size: 13.5px;
    outline: none;
  }}
  .chat-input:focus {{ border-color: var(--accent); }}
  .btn-send {{
    background: var(--primary);
    color: #ffffff;
    font-weight: 700;
    border: none;
    border-radius: 8px;
    padding: 10px 18px;
    cursor: pointer;
  }}

  /* PENDING APPROVAL ALERT */
  .pending-box {{
    margin: 0 0 20px 0;
    background: rgba(229, 164, 59, 0.12);
    border: 1px solid rgba(229, 164, 59, 0.4);
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
  }}
  .pending-text {{
    flex: 1;
    font-size: 13px;
    color: #ffd27a;
    line-height: 1.45;
  }}
  .pending-btn {{
    background: var(--gold);
    color: #000;
    font-weight: 800;
    font-size: 13px;
    padding: 9px 18px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(229, 164, 59, 0.3);
  }}

  /* TABLES */
  .table-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
  }}
  .table-responsive {{ overflow-x: auto; }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }}
  th {{
    background: #111a15;
    color: var(--text-muted);
    font-weight: 700;
    text-align: left;
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
    white-space: nowrap;
  }}
  td {{
    padding: 12px 16px;
    border-bottom: 1px solid #18231e;
    color: var(--text-main);
  }}
  tr:hover {{ background: #16221c; }}

  /* ACTION BUTTONS IN TABLES */
  .btn-tbl {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 8px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
    text-decoration: none;
    border: 1px solid var(--border);
    background: #141f1a;
    color: var(--text-muted);
    transition: all 0.15s;
    cursor: pointer;
  }}
  .btn-tbl:hover {{
    color: #fff;
    border-color: var(--accent);
    background: #1c2b23;
  }}
  .btn-tbl-chat {{
    background: rgba(18, 130, 99, 0.2);
    color: #79f2c3;
    border-color: rgba(121, 242, 195, 0.3);
  }}
  .btn-tbl-chat:hover {{ background: rgba(18, 130, 99, 0.35); color: #fff; }}

  /* BADGES */
  .badge {{
    display: inline-block;
    padding: 4px 9px;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 700;
  }}
  .badge-sent {{ background: rgba(72, 187, 120, 0.2); color: #48bb78; }}
  .badge-failed {{ background: rgba(239, 68, 68, 0.2); color: #ef4444; }}
  .badge-pending {{ background: rgba(229, 164, 59, 0.2); color: var(--gold-light); }}
  .badge-gold {{ background: rgba(229, 164, 59, 0.15); color: #ffd27a; border: 1px solid rgba(229, 164, 59, 0.3); }}

  /* FILTERS */
  .search-input {{
    width: 100%;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    color: #fff;
    font-size: 13.5px;
    outline: none;
    margin-bottom: 14px;
  }}
  .filter-chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 16px;
  }}
  .chip {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 12px;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 20px;
    cursor: pointer;
  }}
  .chip.active {{
    background: var(--primary);
    color: #ffffff;
    border-color: var(--accent);
  }}
</style>
</head>
<body>

<svg width="0" height="0">
  <defs>
    <linearGradient id="emeraldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#128263" />
      <stop offset="100%" stop-color="#79f2c3" />
    </linearGradient>
  </defs>
</svg>

<!-- TOP COCKPIT BAR -->
<div class="topbar">
  <div class="topbar-inner">
    <div class="brand-group">
      <div class="brand-logo">V</div>
      <div class="brand-text">
        <h1>Vocação 2027 · Sub-CRM <span class="live-pill"><span class="live-dot"></span> LIVE DOCKER</span></h1>
        <p>Cockpit de Inteligência Comercial · Jev System One & Automação Ativa</p>
      </div>
    </div>
    <div class="top-actions">
      <button id="queueToggleBtn" class="btn-action btn-queue" onclick="toggleQueue()">
        ⏸️ Pausar Fila
      </button>
      <a href="http://192.168.15.2:3000" target="_blank" class="btn-action btn-crm">
        📊 Abrir Twenty CRM ↗
      </a>
      <button class="btn-action" style="background: #17221d; color: #a4dbc9;" onclick="loadSubCRMData()">
        🔄 Atualizar
      </button>
    </div>
  </div>
</div>

<!-- TABS BAR -->
<div class="tabs-bar">
  <button class="tab-btn" onclick="switchTab('tab-queue', this)">
    🚀 Monitoramento da Fila ao Vivo <span class="tab-badge" id="badgeQueueCount">--</span>
  </button>
  <button class="tab-btn active" onclick="switchTab('tab-inbox', this)">
    💬 Atendimento & Ficha do Lead <span class="tab-badge" id="badgeInboxCount">--</span>
  </button>
  <button class="tab-btn" onclick="switchTab('tab-database', this)">
    🎯 Banco de Leads (100)
  </button>
  <button class="tab-btn" onclick="switchTab('tab-strategy', this)">
    📈 Ofertas Estruturais Jev
  </button>
</div>

<!-- CONTAINER -->
<div class="container">

  <!-- METRICS ROW -->
  <div class="metrics-row">
    <div class="metric-card gold">
      <div class="metric-label">Pipeline Potencial</div>
      <div class="metric-value">R$ 74.060</div>
      <div class="metric-sub">Soma das ofertas de maior fit Jev</div>
    </div>
    <div class="metric-card accent">
      <div class="metric-label">Progresso da Fila Ouro</div>
      <div class="metric-value" id="metricQueueProgress">-- / 30</div>
      <div class="metric-sub">Cadência anti-spam (4 a 5 min)</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Conversas Registradas</div>
      <div class="metric-value" id="metricConversasCount">--</div>
      <div class="metric-sub">Leads com histórico gravado</div>
    </div>
    <div class="metric-card accent">
      <div class="metric-label">Status da Automação</div>
      <div class="metric-value" style="font-size: 19px; color: #79f2c3;" id="metricAutoStatus">🟢 DOCKER ONLINE</div>
      <div class="metric-sub">Twenty CRM + Jev AI + Evolution</div>
    </div>
  </div>

  <!-- PENDING APPROVAL ALERT -->
  <div id="pendingBox" class="pending-box" style="display: none;">
    <div class="pending-text">
      <b>⚡ Sugestão de Resposta da IA Aguardando Sua Aprovação:</b><br>
      <span id="pendingTextSnippet"></span>
    </div>
    <button class="pending-btn" onclick="approvePending()">
      ✅ Disparar Agora (Comando '1')
    </button>
  </div>

  <!-- TAB: MONITORAMENTO DA FILA AO VIVO -->
  <div id="tab-queue" class="tab-panel">
    <div class="queue-monitor-grid">
      <!-- RADIAL PROGRESS CARD -->
      <div class="radial-card">
        <div class="metric-label">Conclusão do Lote Ouro</div>
        <div class="radial-circle-box">
          <svg class="radial-svg" viewBox="0 0 160 160">
            <circle class="circle-bg" cx="80" cy="80" r="70" />
            <circle id="radialProgressCircle" class="circle-progress" cx="80" cy="80" r="70" />
          </svg>
          <div class="radial-center-text">
            <span class="radial-pct" id="radialPercentText">--%</span>
            <span class="radial-sub" id="radialSubText">processados</span>
          </div>
        </div>
        <div style="font-size: 11.5px; color: var(--text-muted);">
          Meta: 30 empresas de Santa Rosália & Brasilândia
        </div>
      </div>

      <!-- QUEUE CONTROLS -->
      <div class="queue-control-card">
        <div>
          <div class="countdown-box">
            <div class="countdown-info">
              <h3>Próximo Disparo em:</h3>
              <p>Cadência inteligente anti-bloqueio da Meta</p>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
              <div class="countdown-timer" id="countdownMinutes">--:--</div>
              <button class="btn-skip" onclick="triggerNextNow()">⚡ Disparar Já</button>
            </div>
          </div>

          <div class="segmented-bar-container">
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700;">
              <span>Distribuição de Entregas</span>
              <span id="cadenceStatusPill" style="color: var(--accent);"><span class="live-dot"></span> ATIVO</span>
            </div>
            <div class="seg-bar">
              <div id="segSent" class="seg-part sent" style="width: 0%;"></div>
              <div id="segFailed" class="seg-part failed" style="width: 0%;"></div>
              <div id="segPending" class="seg-part pending" style="width: 100%;"></div>
            </div>
            <div class="seg-legend">
              <div class="seg-item"><div class="seg-color" style="background:var(--accent);"></div> Entregues (<span id="legendSentCount">0</span>)</div>
              <div class="seg-item"><div class="seg-color" style="background:var(--danger);"></div> Sem WhatsApp (<span id="legendFailedCount">0</span>)</div>
              <div class="seg-item"><div class="seg-color" style="background:#26382f;"></div> Na Fila (<span id="legendPendingCount">30</span>)</div>
            </div>
          </div>

          <!-- EVENT TICKER -->
          <div class="ticker-box" id="tickerBox">
            <div class="ticker-item"><span>Carregando eventos em tempo real...</span></div>
          </div>
        </div>
      </div>
    </div>

    <!-- QUEUE TABLE -->
    <div class="table-card">
      <div style="padding: 16px 20px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center;">
        <h2 style="font-size: 15px; font-weight: 800; color: #fff;">Lista de Leads da Fila Ouro (30)</h2>
        <span style="font-size: 12px; color: var(--text-muted);">Sincronizados com Twenty CRM</span>
      </div>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Status</th>
              <th>Empresa & Categoria</th>
              <th>Bairro</th>
              <th>WhatsApp</th>
              <th>Oferta (Fit)</th>
              <th>Valor</th>
              <th>Hook Personalizado</th>
              <th>Ações Rápidas</th>
            </tr>
          </thead>
          <tbody id="queueTableBody">
            <!-- Renderizado via JS -->
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- TAB: ATENDIMENTO & INBOX -->
  <div id="tab-inbox" class="tab-panel active">
    <div class="inbox-grid">
      <div class="chat-list-panel" id="chatListContainer">
        <!-- Renderizado via JS -->
      </div>
      <div class="chat-view-panel">
        <div class="chat-view-header">
          <div>
            <strong id="activeChatName" style="color: #ffffff; font-size: 16px;">Selecione uma conversa</strong>
            <div id="activeChatPhone" style="font-size: 12px; color: var(--text-muted); font-family: monospace; margin-top: 2px;"></div>
          </div>
          <div style="display: flex; gap: 8px;">
            <a id="activeChatWhatsAppLink" href="#" target="_blank" class="btn-hud btn-hud-wa">
              💬 Abrir no WhatsApp Web ↗
            </a>
          </div>
        </div>

        <!-- FICHA RÁPIDA DO LEAD (HUD) -->
        <div class="lead-hud-card" id="leadHudCard" style="display: none;">
          <div class="lead-hud-row1">
            <div class="lead-hud-pills">
              <span class="hud-pill niche" id="hudNiche">Panificação</span>
              <span class="hud-pill bairro" id="hudBairro">📍 Bairro</span>
              <span class="hud-pill offer" id="hudOffer">⭐ Oferta Jev</span>
            </div>
            <div class="lead-hud-actions">
              <a id="hudLinkMaps" href="#" target="_blank" class="btn-hud btn-hud-maps" title="Ver ficha e avaliações no Google Maps">
                🗺️ Maps ↗
              </a>
              <a id="hudLinkInsta" href="#" target="_blank" class="btn-hud btn-hud-insta" title="Ver perfil ou menções no Instagram">
                📸 Instagram ↗
              </a>
              <a id="hudLinkWa" href="#" target="_blank" class="btn-hud btn-hud-wa" title="Chamar no WhatsApp Direto via wa.me">
                💬 WhatsApp ↗
              </a>
              <a id="hudLinkSite" href="#" target="_blank" class="btn-hud btn-hud-site" title="Buscar site ou informações no Google">
                🌐 Site / Google ↗
              </a>
            </div>
          </div>
          <div class="lead-hud-row2">
            <div class="lead-hud-detail" style="min-width: 200px;">
              <span>🏢</span> <span class="hud-strong" id="hudAddr">Endereço</span>
            </div>
            <div class="lead-hud-detail" style="flex: 1;">
              <span>⚡</span> <span style="color: var(--text-muted);">Diagnóstico / Dor:</span> <span class="hud-presence-highlight" id="hudPresence">Diagnóstico</span>
            </div>
          </div>
        </div>

        <div class="chat-messages" id="chatMessagesContainer">
          <div style="text-align: center; color: var(--text-muted); margin-top: 60px;">
            Clique em um contato ao lado para ver a ficha completa e o histórico de mensagens.
          </div>
        </div>
        <div class="chat-view-footer">
          <input type="text" id="customReplyInput" class="chat-input" placeholder="Digite uma resposta direta e humana..." onkeydown="if(event.key==='Enter') sendCustomMessage()">
          <button class="btn-send" onclick="sendCustomMessage()">Enviar</button>
        </div>
      </div>
    </div>
  </div>

  <!-- TAB: BANCO DE LEADS -->
  <div id="tab-database" class="tab-panel">
    <input type="text" id="searchInput" class="search-input" placeholder="Buscar entre os 100 leads por empresa, nicho ou telefone..." onkeyup="filterDatabaseLeads()">
    <div class="filter-chips">
      <div class="chip active" onclick="setDbFilter('all', this)">Todos (100)</div>
      <div class="chip" style="border-color: #e5a43b; color: #ffd27a;" onclick="setDbFilter('ouro', this)">⭐ Leads Ouro (30)</div>
      <div class="chip" onclick="setDbFilter('sr', this)">Santa Rosália (60)</div>
      <div class="chip" onclick="setDbFilter('br', this)">Jd. Brasilândia (40)</div>
      <div class="chip" onclick="setDbFilter('start', this)">Start (R$ 850)</div>
      <div class="chip" onclick="setDbFilter('tour', this)">Tour 360° (R$ 950)</div>
      <div class="chip" onclick="setDbFilter('update', this)">Update (R$ 980)</div>
    </div>
    <div class="table-card">
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Empresa & Categoria</th>
              <th>Bairro & Endereço</th>
              <th>Telefone</th>
              <th>Oferta Jev</th>
              <th>Interesse Vendedor</th>
              <th>Ações Rápidas</th>
            </tr>
          </thead>
          <tbody id="dbTableBody">
            <!-- Renderizado via JS -->
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- TAB: ESTRATÉGIA -->
  <div id="tab-strategy" class="tab-panel">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
      <div class="metric-card">
        <h3 style="color: #79f2c3; font-size: 16px; margin-bottom: 8px;">🚀 Vocação Start</h3>
        <p style="font-size: 22px; font-weight: 800; color: #fff;">R$ 850,00</p>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 8px; line-height: 1.45;">
          Ficha Google Maps blindada + Vitrine Mobile One-Page ultra rápida com botão WhatsApp direto.
        </p>
      </div>
      <div class="metric-card gold">
        <h3 style="color: #ffd27a; font-size: 16px; margin-bottom: 8px;">📸 Combo Maps + Tour 360°</h3>
        <p style="font-size: 22px; font-weight: 800; color: #fff;">R$ 950,00</p>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 8px; line-height: 1.45;">
          Fotos imersivas 360° com GoPro Max publicadas no Google Street View para clínicas, academias e gastronomia.
        </p>
      </div>
      <div class="metric-card accent">
        <h3 style="color: #79f2c3; font-size: 16px; margin-bottom: 8px;">⚡ Vocação Update</h3>
        <p style="font-size: 22px; font-weight: 800; color: #fff;">R$ 980,00</p>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 8px; line-height: 1.45;">
          Reforma mobile-first completa de páginas antigas ou lentas no celular.
        </p>
      </div>
      <div class="metric-card">
        <h3 style="color: #88a397; font-size: 16px; margin-bottom: 8px;">🗺️ Blindagem Maps</h3>
        <p style="font-size: 22px; font-weight: 800; color: #fff;">R$ 450,00</p>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 8px; line-height: 1.45;">
          Reivindicação, otimização de categorias e blindagem de horário no Google Maps.
        </p>
      </div>
    </div>
  </div>

</div>

<script>
const LEADS_100 = {json.dumps(leads_100, ensure_ascii=False)};
let CURRENT_DATA = null;
let SELECTED_CHAT_PHONE = null;
let DB_ACTIVE_FILTER = 'all';
let LOCAL_COUNTDOWN = 0;

function switchTab(tabId, el) {{
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  if (el) el.classList.add('active');
}}

function loadSubCRMData() {{
  fetch('/api/subcrm-data')
    .then(r => r.json())
    .then(data => {{
      CURRENT_DATA = data;
      renderSubCRM(data);
    }})
    .catch(err => console.log('Erro ao buscar dados:', err));
}}

function renderSubCRM(data) {{
  const q = data.queue || {{}};
  const stats = data.stats || {{}};
  const chats = data.chats || [];
  const pending = data.pending;

  const sentCount = (q.sent || []).length;
  const failedCount = (q.failed || []).length;
  const totalQueue = q.total || 30;
  const processed = sentCount + failedCount;
  const pendingCount = Math.max(0, totalQueue - processed);

  // Radial progress
  const pct = Math.round((processed / totalQueue) * 100);
  document.getElementById('radialPercentText').innerText = `${{pct}}%`;
  document.getElementById('radialSubText').innerText = `${{processed}} de ${{totalQueue}} processados`;

  // SVG ring stroke-dashoffset (440 is full circle)
  const circle = document.getElementById('radialProgressCircle');
  const offset = 440 - (440 * (pct / 100));
  circle.style.strokeDashoffset = offset;

  // Segmented bar
  const sentPct = (sentCount / totalQueue) * 100;
  const failedPct = (failedCount / totalQueue) * 100;
  const pendPct = (pendingCount / totalQueue) * 100;
  document.getElementById('segSent').style.width = `${{sentPct}}%`;
  document.getElementById('segFailed').style.width = `${{failedPct}}%`;
  document.getElementById('segPending').style.width = `${{pendPct}}%`;

  document.getElementById('legendSentCount').innerText = sentCount;
  document.getElementById('legendFailedCount').innerText = failedCount;
  document.getElementById('legendPendingCount').innerText = pendingCount;

  // KPIs
  document.getElementById('metricQueueProgress').innerText = `${{processed}} / ${{totalQueue}}`;
  document.getElementById('badgeQueueCount').innerText = `${{processed}}/${{totalQueue}}`;
  document.getElementById('metricConversasCount').innerText = chats.length;
  document.getElementById('badgeInboxCount').innerText = chats.length;

  // Countdown timer
  LOCAL_COUNTDOWN = q.countdown_seconds || 0;
  updateCountdownDisplay();

  // Fila pausada ou ativa
  const qBtn = document.getElementById('queueToggleBtn');
  const cadencePill = document.getElementById('cadenceStatusPill');
  if (q.is_paused) {{
    qBtn.innerText = '▶️ Retomar Fila';
    qBtn.classList.add('paused');
    cadencePill.innerHTML = '<span class="live-dot" style="background:#ef4444; box-shadow:0 0 8px #ef4444;"></span> PAUSADA';
    cadencePill.style.color = '#ef4444';
  }} else {{
    qBtn.innerText = '⏸️ Pausar Fila';
    qBtn.classList.remove('paused');
    cadencePill.innerHTML = '<span class="live-dot"></span> ATIVO';
    cadencePill.style.color = '#79f2c3';
  }}

  // Ticker Feed
  renderTickerLogs(q.logs || []);

  // Pending Box
  const pendingBox = document.getElementById('pendingBox');
  if (pending && pending.reply) {{
    pendingBox.style.display = 'flex';
    document.getElementById('pendingTextSnippet').innerText = `"${{pending.reply}}" (Para ${{pending.name || pending.phone}})`;
  }} else {{
    pendingBox.style.display = 'none';
  }}

  // Chats & Queue Table
  renderChatList(chats);
  renderQueueTable(q);
}}

function updateCountdownDisplay() {{
  const min = Math.floor(LOCAL_COUNTDOWN / 60);
  const sec = LOCAL_COUNTDOWN % 60;
  const str = `${{String(min).padStart(2, '0')}}:${{String(sec).padStart(2, '0')}}`;
  document.getElementById('countdownMinutes').innerText = LOCAL_COUNTDOWN > 0 ? str : '00:00';
}}

function renderTickerLogs(logs) {{
  const box = document.getElementById('tickerBox');
  if (!logs.length) {{
    box.innerHTML = '<div class="ticker-item"><span style="color:var(--text-muted);">Aguardando próximo ciclo de disparo...</span></div>';
    return;
  }}
  box.innerHTML = logs.slice().reverse().map(l => {{
    const isOk = l.status === 'success';
    const icon = isOk ? '✅' : '❌';
    const color = isOk ? '#79f2c3' : '#ef4444';
    return `<div class="ticker-item"><span style="color:var(--text-muted);">${{l.time}}</span> <span>${{icon}}</span> <strong style="color:${{color}};">${{l.name}}</strong> <span>(${{l.bairro}})</span></div>`;
  }}).join('');
}}

function renderChatList(chats) {{
  const container = document.getElementById('chatListContainer');
  container.innerHTML = '';
  if (!chats.length) {{
    container.innerHTML = '<div style="padding: 20px; color: var(--text-muted); font-size: 13px;">Nenhuma conversa registrada.</div>';
    return;
  }}

  chats.forEach((c, idx) => {{
    const item = document.createElement('div');
    item.className = 'chat-item' + (SELECTED_CHAT_PHONE === c.phone || (!SELECTED_CHAT_PHONE && idx === 0) ? ' active' : '');
    item.onclick = () => selectChat(c.phone);

    const timeStr = c.last_at ? c.last_at.split('T')[1]?.slice(0, 5) : '';
    item.innerHTML = `
      <div class="chat-item-header">
        <span class="chat-item-name">${{c.name}}</span>
        <span class="chat-item-time">${{timeStr}}</span>
      </div>
      <div style="display: flex; gap: 6px; margin: 3px 0 4px 0;">
        <span class="hud-pill niche" style="font-size: 10px; padding: 1px 6px;">${{c.cat || 'Comércio'}}</span>
        <span class="hud-pill bairro" style="font-size: 10px; padding: 1px 6px;">${{c.bairro || 'Sorocaba'}}</span>
      </div>
      <div class="chat-item-preview">${{c.last_msg || 'Sem mensagens'}}</div>
    `;
    container.appendChild(item);
  }});

  if (!SELECTED_CHAT_PHONE && chats.length > 0) {{
    selectChat(chats[0].phone);
  }}
}}

function selectChat(phone) {{
  SELECTED_CHAT_PHONE = phone;
  document.querySelectorAll('.chat-item').forEach(el => el.classList.remove('active'));

  if (!CURRENT_DATA) return;
  const chat = (CURRENT_DATA.chats || []).find(c => c.phone === phone);
  if (!chat) return;

  // Header
  document.getElementById('activeChatName').innerText = chat.name;
  document.getElementById('activeChatPhone').innerText = chat.phone;
  document.getElementById('activeChatWhatsAppLink').href = chat.whatsapp_url || `https://wa.me/${{chat.phone}}`;

  // Ficha Rápida HUD
  const hud = document.getElementById('leadHudCard');
  hud.style.display = 'flex';
  document.getElementById('hudNiche').innerText = chat.cat || 'Comércio / Serviços';
  document.getElementById('hudBairro').innerText = `📍 ${{chat.bairro || 'Sorocaba'}}`;
  document.getElementById('hudOffer').innerText = `⭐ ${{chat.oferta_nome ? chat.oferta_nome.split('(')[0].trim() : 'Vocação Start'}} · R$ ${{(chat.oferta_preco || 850).toFixed(2)}}`;
  document.getElementById('hudAddr').innerText = chat.addr || 'Sorocaba / SP';
  document.getElementById('hudPresence').innerText = chat.presence || 'Presença digital em qualificação';

  // Deep-links
  document.getElementById('hudLinkMaps').href = chat.maps_url || `https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent(chat.name + ' ' + (chat.addr||'') + ' Sorocaba')}}`;
  document.getElementById('hudLinkInsta').href = chat.instagram_url || `https://www.google.com/search?q=${{encodeURIComponent('site:instagram.com ' + chat.name + ' Sorocaba')}}`;
  document.getElementById('hudLinkWa').href = chat.whatsapp_url || `https://wa.me/${{chat.phone}}`;
  document.getElementById('hudLinkSite').href = chat.search_url || `https://www.google.com/search?q=${{encodeURIComponent(chat.name + ' Sorocaba')}}`;

  // Messages
  const msgsContainer = document.getElementById('chatMessagesContainer');
  msgsContainer.innerHTML = '';

  (chat.messages || []).forEach(m => {{
    const isOut = m.role && m.role.includes('Vocação');
    const b = document.createElement('div');
    b.className = 'chat-bubble ' + (isOut ? 'outbound' : 'inbound');
    const timeStr = m.at ? m.at.split('T')[1]?.slice(0, 5) : '';
    b.innerHTML = `
      <div>${{m.text}}</div>
      <div class="bubble-meta">${{isOut ? 'Vocação' : chat.name}} · ${{timeStr}}</div>
    `;
    msgsContainer.appendChild(b);
  }});
  msgsContainer.scrollTop = msgsContainer.scrollHeight;
}}

function openChatByPhone(phone) {{
  switchTab('tab-inbox', document.querySelectorAll('.tab-btn')[1]);
  selectChat(phone);
}}

function sendCustomMessage() {{
  const input = document.getElementById('customReplyInput');
  const text = input.value.trim();
  if (!text || !SELECTED_CHAT_PHONE) return;

  fetch('/api/send-message', {{
    method: 'POST',
    headers: {{ 'Content-Type': 'application/json' }},
    body: JSON.stringify({{ phone: SELECTED_CHAT_PHONE, text: text }})
  }})
  .then(r => r.json())
  .then(() => {{
    input.value = '';
    loadSubCRMData();
  }});
}}

function approvePending() {{
  fetch('/api/approve', {{ method: 'POST' }})
    .then(r => r.json())
    .then(res => {{
      alert(res.message);
      loadSubCRMData();
    }});
}}

function toggleQueue() {{
  fetch('/api/toggle-queue', {{ method: 'POST' }})
    .then(r => r.json())
    .then(() => loadSubCRMData());
}}

function triggerNextNow() {{
  fetch('/api/trigger-next', {{ method: 'POST' }})
    .then(r => r.json())
    .then(() => {{
      LOCAL_COUNTDOWN = 0;
      updateCountdownDisplay();
      setTimeout(loadSubCRMData, 1000);
    }});
}}

function renderQueueTable(queue) {{
  const tbody = document.getElementById('queueTableBody');
  tbody.innerHTML = '';
  const leads = queue.leads || [];
  const sentSet = new Set(queue.sent || []);
  const failedSet = new Set(queue.failed || []);

  leads.forEach(l => {{
    let statusBadge = '<span class="badge badge-pending">⏳ Na Fila</span>';
    if (sentSet.has(l.phone)) {{
      statusBadge = '<span class="badge badge-sent">✅ Entregue</span>';
    }} else if (failedSet.has(l.phone)) {{
      statusBadge = '<span class="badge badge-failed">❌ Sem WhatsApp</span>';
    }}

    const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent(l.name + ' ' + (l.addr||'') + ' Sorocaba')}}`;
    const waUrl = `https://wa.me/${{l.phone}}`;

    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${{statusBadge}}</td>
      <td><strong>${{l.name}}</strong><br><span style="font-size: 11px; color: var(--text-muted);">${{l.cat}}</span></td>
      <td>${{l.bairro}}</td>
      <td style="font-family: monospace;">${{l.phone}}</td>
      <td><span class="badge badge-gold">${{l.oferta_nome.split('(')[0]}}</span></td>
      <td style="font-weight: 700;">R$ ${{l.oferta_preco.toFixed(2)}}</td>
      <td style="font-size: 11.5px; color: var(--text-muted); max-width: 280px;">"${{l.hook_whatsapp.slice(0, 80)}}..."</td>
      <td>
        <div style="display: flex; gap: 4px;">
          <a href="${{mapsUrl}}" target="_blank" class="btn-tbl" title="Abrir Google Maps">🗺️ Maps</a>
          <a href="${{waUrl}}" target="_blank" class="btn-tbl" title="Abrir WhatsApp">💬 WA</a>
          <button onclick="openChatByPhone('${{l.phone}}')" class="btn-tbl btn-tbl-chat" title="Ver Histórico / Chat">Chat ↗</button>
        </div>
      </td>
    `;
    tbody.appendChild(tr);
  }});
}}

function renderDatabaseTable() {{
  const tbody = document.getElementById('dbTableBody');
  tbody.innerHTML = '';
  const term = (document.getElementById('searchInput').value || '').toLowerCase().trim();

  LEADS_100.forEach(l => {{
    const matchesSearch = 
      l.name.toLowerCase().includes(term) ||
      l.cat.toLowerCase().includes(term) ||
      l.addr.toLowerCase().includes(term) ||
      l.phone.includes(term);

    let matchesChip = true;
    if (DB_ACTIVE_FILTER === 'ouro') matchesChip = (l.interesse_vendedor >= 90);
    else if (DB_ACTIVE_FILTER === 'sr') matchesChip = (l.bairro === 'Santa Rosália');
    else if (DB_ACTIVE_FILTER === 'br') matchesChip = (l.bairro === 'Jardim Brasilândia');
    else if (DB_ACTIVE_FILTER === 'start') matchesChip = (l.oferta_key === 'vocacao_start_850');
    else if (DB_ACTIVE_FILTER === 'tour') matchesChip = (l.oferta_key === 'combo_maps_tour360_950');
    else if (DB_ACTIVE_FILTER === 'update') matchesChip = (l.oferta_key === 'vocacao_update_980');

    if (matchesSearch && matchesChip) {{
      const score = l.interesse_vendedor || 75;
      const scoreColor = score >= 90 ? '#48bb78' : (score >= 75 ? '#38b2ac' : '#a0aec0');
      
      const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent(l.name + ' ' + (l.addr||'') + ' Sorocaba')}}`;
      const instaUrl = `https://www.google.com/search?q=${{encodeURIComponent('site:instagram.com ' + l.name + ' Sorocaba')}}`;
      const waUrl = `https://wa.me/${{l.phone}}`;

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${{l.name}}</strong><br><span style="font-size: 11px; color: var(--text-muted);">${{l.cat}}</span></td>
        <td><span class="badge" style="background:#1f2d26; color:#79f2c3;">${{l.bairro}}</span><br><span style="font-size: 11px; color: var(--text-muted);">${{l.addr}}</span></td>
        <td style="font-family: monospace; color: ${{l.phone.includes('9') ? '#79f2c3' : '#cbd5e0'}};">${{l.phone}}</td>
        <td><strong>${{l.oferta_nome.split('(')[0]}}</strong><br><span style="color: #ffd27a; font-weight: bold;">R$ ${{l.oferta_preco.toFixed(2)}}</span></td>
        <td>
          <span style="font-weight: 800; color: ${{scoreColor}}; font-size: 14px;">${{score}}%</span>
          <div style="font-size: 10.5px; color: var(--text-muted);">${{l.interesse_tag || ''}}</div>
        </td>
        <td>
          <div style="display: flex; gap: 4px;">
            <a href="${{mapsUrl}}" target="_blank" class="btn-tbl" title="Abrir Google Maps">🗺️</a>
            <a href="${{instaUrl}}" target="_blank" class="btn-tbl" title="Abrir Instagram">📸</a>
            <a href="${{waUrl}}" target="_blank" class="btn-tbl" title="WhatsApp wa.me">💬</a>
            <button onclick="openChatByPhone('${{l.phone}}')" class="btn-tbl btn-tbl-chat" title="Ver no Sub-CRM">Chat ↗</button>
          </div>
        </td>
      `;
      tbody.appendChild(tr);
    }}
  }});
}}

function setDbFilter(f, el) {{
  DB_ACTIVE_FILTER = f;
  document.querySelectorAll('.filter-chips .chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  renderDatabaseTable();
}}

function filterDatabaseLeads() {{
  renderDatabaseTable();
}}

// Tick a cada 1 segundo no countdown
setInterval(() => {{
  if (LOCAL_COUNTDOWN > 0) {{
    LOCAL_COUNTDOWN--;
    updateCountdownDisplay();
  }}
}}, 1000);

// Inicialização
renderDatabaseTable();
loadSubCRMData();
setInterval(loadSubCRMData, 4000);
</script>

</body>
</html>
'''

    with open('auto_responder_docker/templates/painel.html', 'w', encoding='utf-8') as f:
        f.write(html)

    # Copia para build_ultimate_subcrm.py também para manter sincronizado
    print("Painel UX Premium Sub-CRM gerado com sucesso!")

if __name__ == '__main__':
    generate_subcrm()
