import json

def generate_subcrm():
    with open('leads_100_santa_rosalia_brasilandia.json', 'r', encoding='utf-8') as f:
        leads_100 = json.load(f)

    html_content = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vocação 2027 · Sub-CRM Executivo & Cockpit Comercial</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg-main: #0b100e;
    --bg-card: #131b17;
    --bg-card-hover: #18241f;
    --border: #213028;
    --border-light: #2d4237;
    --primary: #128263;
    --primary-light: #18a981;
    --accent: #79f2c3;
    --gold: #e5a43b;
    --gold-light: #ffd27a;
    --warning: #f59e0b;
    --danger: #ef4444;
    --text-main: #eef5f1;
    --text-muted: #8ea89d;
    --badge-bg: #1c2722;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background-color: var(--bg-main);
    color: var(--text-main);
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    min-height: 100vh;
    padding-bottom: 90px;
    -webkit-font-smoothing: antialiased;
  }

  /* TOP COCKPIT BAR */
  .topbar {
    background: rgba(19, 27, 23, 0.95);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(12px);
    position: sticky;
    top: 0;
    z-index: 100;
    padding: 12px 20px;
  }
  .topbar-inner {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }
  .brand-group {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .brand-logo {
    width: 38px;
    height: 38px;
    border-radius: 9px;
    background: linear-gradient(135deg, var(--primary) 0%, #084333 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Fraunces', serif;
    font-weight: 700;
    font-size: 20px;
    color: #ffffff;
    border: 1px solid var(--border-light);
  }
  .brand-text h1 {
    font-size: 16px;
    font-weight: 800;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .brand-text p {
    font-size: 11px;
    color: var(--text-muted);
  }
  .top-actions {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .btn-action {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12.5px;
    font-weight: 700;
    padding: 7px 14px;
    border-radius: 8px;
    border: 1px solid var(--border);
    cursor: pointer;
    text-decoration: none;
    transition: all 0.2s;
  }
  .btn-crm {
    background: #1c2722;
    color: var(--accent);
    border-color: rgba(121, 242, 195, 0.3);
  }
  .btn-crm:hover {
    background: #24352e;
  }
  .btn-queue {
    background: rgba(229, 164, 59, 0.15);
    color: var(--gold-light);
    border-color: rgba(229, 164, 59, 0.4);
  }
  .btn-queue.paused {
    background: rgba(239, 68, 68, 0.15);
    color: #fca5a5;
    border-color: rgba(239, 68, 68, 0.4);
  }

  /* NAVIGATION TABS */
  .tabs-bar {
    max-width: 1400px;
    margin: 16px auto 0;
    padding: 0 20px;
    display: flex;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }
  .tab-btn {
    background: none;
    border: none;
    border-bottom: 2px solid transparent;
    color: var(--text-muted);
    font-size: 13.5px;
    font-weight: 700;
    padding: 10px 16px;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .tab-btn:hover {
    color: var(--text-main);
  }
  .tab-btn.active {
    color: var(--accent);
    border-bottom-color: var(--accent);
  }
  .tab-badge {
    background: var(--primary);
    color: #fff;
    font-size: 11px;
    padding: 2px 7px;
    border-radius: 12px;
  }

  /* MAIN CONTAINER */
  .container {
    max-width: 1400px;
    margin: 20px auto 0;
    padding: 0 20px;
  }

  /* METRICS ROW */
  .metrics-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 14px;
    margin-bottom: 22px;
  }
  .metric-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    position: relative;
    overflow: hidden;
  }
  .metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 4px; height: 100%;
    background: var(--primary);
  }
  .metric-card.gold::before { background: var(--gold); }
  .metric-card.accent::before { background: var(--accent); }
  .metric-card.warning::before { background: var(--warning); }
  .metric-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
  }
  .metric-value {
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
    margin-top: 4px;
  }
  .metric-sub {
    font-size: 11.5px;
    color: var(--text-muted);
    margin-top: 2px;
  }

  /* TAB CONTENT PANELS */
  .tab-panel {
    display: none;
  }
  .tab-panel.active {
    display: block;
  }

  /* INBOX / CHAT UI */
  .inbox-grid {
    display: grid;
    grid-template-columns: 340px 1fr;
    gap: 16px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    min-height: 580px;
  }
  @media (max-width: 860px) {
    .inbox-grid { grid-template-columns: 1fr; }
  }
  .chat-list-panel {
    border-right: 1px solid var(--border);
    background: #0f1513;
    overflow-y: auto;
    max-height: 650px;
  }
  .chat-item {
    padding: 14px 16px;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    transition: background 0.15s;
  }
  .chat-item:hover, .chat-item.active {
    background: #17221d;
  }
  .chat-item-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
  }
  .chat-item-name {
    font-weight: 700;
    font-size: 13.5px;
    color: #ffffff;
  }
  .chat-item-time {
    font-size: 11px;
    color: var(--text-muted);
  }
  .chat-item-preview {
    font-size: 12px;
    color: var(--text-muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* CHAT VIEW */
  .chat-view-panel {
    display: flex;
    flex-direction: column;
    height: 650px;
    background: var(--bg-card);
  }
  .chat-view-header {
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #111a15;
  }
  .chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .chat-bubble {
    max-width: 78%;
    padding: 12px 16px;
    border-radius: 12px;
    font-size: 13.5px;
    line-height: 1.45;
  }
  .chat-bubble.inbound {
    align-self: flex-start;
    background: #1c2722;
    border: 1px solid var(--border);
    color: #e2ede8;
    border-bottom-left-radius: 2px;
  }
  .chat-bubble.outbound {
    align-self: flex-end;
    background: #128263;
    color: #ffffff;
    border-bottom-right-radius: 2px;
  }
  .bubble-meta {
    font-size: 10.5px;
    opacity: 0.75;
    margin-top: 4px;
    text-align: right;
  }
  .chat-view-footer {
    padding: 14px 20px;
    border-top: 1px solid var(--border);
    background: #111a15;
    display: flex;
    gap: 10px;
  }
  .chat-input {
    flex: 1;
    background: #0b100e;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 14px;
    color: #ffffff;
    font-size: 13.5px;
    outline: none;
  }
  .chat-input:focus { border-color: var(--accent); }
  .btn-send {
    background: var(--primary);
    color: #ffffff;
    font-weight: 700;
    border: none;
    border-radius: 8px;
    padding: 10px 18px;
    cursor: pointer;
  }

  /* PENDING APPROVAL CARD */
  .pending-box {
    margin: 16px 20px 0;
    background: rgba(229, 164, 59, 0.1);
    border: 1px solid rgba(229, 164, 59, 0.35);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
  }
  .pending-text {
    flex: 1;
    font-size: 13px;
    color: #ffd27a;
    line-height: 1.4;
  }
  .pending-btn {
    background: var(--gold);
    color: #000000;
    font-weight: 800;
    font-size: 13px;
    padding: 8px 16px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
  }

  /* QUEUE TABLE */
  .queue-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
  }
  .table-responsive {
    overflow-x: auto;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }
  th {
    background: #111a15;
    color: var(--text-muted);
    font-weight: 700;
    text-align: left;
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
  }
  td {
    padding: 12px 16px;
    border-bottom: 1px solid #19231e;
    color: var(--text-main);
  }
  tr:hover { background: #16201b; }

  /* BADGES */
  .badge {
    display: inline-block;
    padding: 4px 9px;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 700;
  }
  .badge-sent { background: rgba(72, 187, 120, 0.2); color: #48bb78; }
  .badge-failed { background: rgba(239, 68, 68, 0.2); color: #ef4444; }
  .badge-pending { background: rgba(229, 164, 59, 0.2); color: var(--gold-light); }
  .badge-gold { background: rgba(229, 164, 59, 0.15); color: #ffd27a; border: 1px solid rgba(229, 164, 59, 0.3); }

  /* SEARCH & FILTERS */
  .search-input {
    width: 100%;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    color: #fff;
    font-size: 13.5px;
    outline: none;
    margin-bottom: 14px;
  }
  .filter-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 16px;
  }
  .chip {
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 12px;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 20px;
    cursor: pointer;
    user-select: none;
  }
  .chip.active {
    background: var(--primary);
    color: #ffffff;
    border-color: var(--accent);
  }
</style>
</head>
<body>

<!-- TOP COCKPIT BAR -->
<div class="topbar">
  <div class="topbar-inner">
    <div class="brand-group">
      <div class="brand-logo">V</div>
      <div class="brand-text">
        <h1>Vocação 2027 · Sub-CRM <span style="font-size: 11px; background: rgba(18, 130, 99, 0.3); color: #79f2c3; padding: 2px 8px; border-radius: 6px;">DOCKER LIVE</span></h1>
        <p>Cockpit Comercial · Jev System One & Gestão Ágil</p>
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
  <button class="tab-btn active" onclick="switchTab('tab-inbox', this)">
    💬 Atendimento & Respostas <span class="tab-badge" id="badgeInboxCount">0</span>
  </button>
  <button class="tab-btn" onclick="switchTab('tab-queue', this)">
    🚀 Fila de Disparo (30 Ouro) <span class="tab-badge" id="badgeQueueCount">22/30</span>
  </button>
  <button class="tab-btn" onclick="switchTab('tab-database', this)">
    🎯 Banco de Leads (100)
  </button>
  <button class="tab-btn" onclick="switchTab('tab-strategy', this)">
    📈 Ofertas & Estratégia Jev
  </button>
</div>

<!-- CONTAINER -->
<div class="container">

  <!-- METRICS ROW -->
  <div class="metrics-row">
    <div class="metric-card gold">
      <div class="metric-label">Pipeline Potencial</div>
      <div class="metric-value">R$ 74.060</div>
      <div class="metric-sub">Soma das ofertas de maior fit</div>
    </div>
    <div class="metric-card accent">
      <div class="metric-label">Leads Ouro Processados</div>
      <div class="metric-value" id="metricQueueProgress">-- / 30</div>
      <div class="metric-sub">Cadência anti-spam (4-5 min)</div>
    </div>
    <div class="metric-card warning">
      <div class="metric-label">Conversas no WhatsApp</div>
      <div class="metric-value" id="metricConversasCount">--</div>
      <div class="metric-sub">Leads com histórico ativo</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Status da Automação</div>
      <div class="metric-value" style="font-size: 20px; color: #79f2c3;" id="metricAutoStatus">🟢 DOCKER ATIVO</div>
      <div class="metric-sub">Jev + Gemini 3.8 + Twenty CRM</div>
    </div>
  </div>

  <!-- PENDING APPROVAL ALERT BOX -->
  <div id="pendingBox" class="pending-box" style="display: none; margin: 0 0 20px 0;">
    <div class="pending-text">
      <b>⚡ Resposta da IA Pronta para Aprovação:</b><br>
      <span id="pendingTextSnippet"></span>
    </div>
    <button class="pending-btn" onclick="approvePending()">
      ✅ Disparar Agora (Comando 1)
    </button>
  </div>

  <!-- TAB 1: INBOX & ATENDIMENTO -->
  <div id="tab-inbox" class="tab-panel active">
    <div class="inbox-grid">
      <div class="chat-list-panel" id="chatListContainer">
        <!-- Renderizado via JS -->
      </div>
      <div class="chat-view-panel">
        <div class="chat-view-header">
          <div>
            <strong id="activeChatName" style="color: #ffffff; font-size: 15px;">Selecione uma conversa</strong>
            <div id="activeChatPhone" style="font-size: 12px; color: var(--text-muted); font-family: monospace;"></div>
          </div>
          <div>
            <a id="activeChatWhatsAppLink" href="#" target="_blank" class="btn-action" style="background: #1f2d26; color: #79f2c3; font-size: 11.5px;">
              Abrir no WhatsApp Web ↗
            </a>
          </div>
        </div>
        <div class="chat-messages" id="chatMessagesContainer">
          <div style="text-align: center; color: var(--text-muted); margin-top: 60px;">
            Clique em um contato ao lado para visualizar o histórico de mensagens.
          </div>
        </div>
        <div class="chat-view-footer">
          <input type="text" id="customReplyInput" class="chat-input" placeholder="Digite uma resposta direta em nome da Vocação..." onkeydown="if(event.key==='Enter') sendCustomMessage()">
          <button class="btn-send" onclick="sendCustomMessage()">Enviar</button>
        </div>
      </div>
    </div>
  </div>

  <!-- TAB 2: FILA DE DISPARO (30 OURO) -->
  <div id="tab-queue" class="tab-panel">
    <div class="queue-card">
      <div style="padding: 16px 20px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div>
          <h2 style="font-size: 16px; font-weight: 800; color: #fff;">Fila Segura de Disparos · 30 Leads Ouro</h2>
          <p style="font-size: 12px; color: var(--text-muted);">Intervalo de segurança anti-bloqueio Meta (4 a 6 min por mensagem)</p>
        </div>
        <div>
          <button class="btn-action btn-queue" onclick="toggleQueue()">Pausar / Retomar Fila</button>
        </div>
      </div>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Status</th>
              <th>Empresa</th>
              <th>Bairro</th>
              <th>WhatsApp</th>
              <th>Oferta (Fit)</th>
              <th>Valor</th>
              <th>Hook Disparado</th>
            </tr>
          </thead>
          <tbody id="queueTableBody">
            <!-- Inserido dinamicamente -->
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- TAB 3: BANCO DE LEADS (100) -->
  <div id="tab-database" class="tab-panel">
    <input type="text" id="searchInput" class="search-input" placeholder="Buscar entre os 100 leads por nome, nicho ou telefone..." onkeyup="filterDatabaseLeads()">
    <div class="filter-chips">
      <div class="chip active" onclick="setDbFilter('all', this)">Todos (100)</div>
      <div class="chip" style="border-color: #e5a43b; color: #ffd27a;" onclick="setDbFilter('ouro', this)">⭐ Leads Ouro (30)</div>
      <div class="chip" onclick="setDbFilter('sr', this)">Santa Rosália (60)</div>
      <div class="chip" onclick="setDbFilter('br', this)">Jd. Brasilândia (40)</div>
      <div class="chip" onclick="setDbFilter('start', this)">Start (R$ 850)</div>
      <div class="chip" onclick="setDbFilter('tour', this)">Tour 360° (R$ 950)</div>
      <div class="chip" onclick="setDbFilter('update', this)">Update (R$ 980)</div>
    </div>
    <div class="queue-card">
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Empresa & Categoria</th>
              <th>Bairro & Endereço</th>
              <th>Telefone</th>
              <th>Oferta Jev</th>
              <th>Interesse Vendedor</th>
            </tr>
          </thead>
          <tbody id="dbTableBody">
            <!-- Inserido via JS -->
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- TAB 4: OFERTAS & ESTRATÉGIA -->
  <div id="tab-strategy" class="tab-panel">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
      <div class="metric-card">
        <h3 style="color: #79f2c3; font-size: 16px; margin-bottom: 8px;">🚀 Vocação Start</h3>
        <p style="font-size: 22px; font-weight: 800; color: #fff;">R$ 850,00</p>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 8px; line-height: 1.45;">
          <b>Escopo:</b> Ficha Google Maps blindada + Vitrine Mobile One-Page ultra rápida com botão WhatsApp.<br><br>
          <b>Fit:</b> Empresas sem site ou com ficha não verificada que dependem só do boca a boca.
        </p>
      </div>
      <div class="metric-card gold">
        <h3 style="color: #ffd27a; font-size: 16px; margin-bottom: 8px;">📸 Combo Maps + Tour 360°</h3>
        <p style="font-size: 22px; font-weight: 800; color: #fff;">R$ 950,00</p>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 8px; line-height: 1.45;">
          <b>Escopo:</b> Fotos imersivas 360° com GoPro Max publicadas no Google Street View + Blindagem do perfil.<br><br>
          <b>Fit:</b> Clínicas, consultórios, studios de pilates, escolas e restaurantes com espaço físico atraente.
        </p>
      </div>
      <div class="metric-card accent">
        <h3 style="color: #79f2c3; font-size: 16px; margin-bottom: 8px;">⚡ Vocação Update</h3>
        <p style="font-size: 22px; font-weight: 800; color: #fff;">R$ 980,00</p>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 8px; line-height: 1.45;">
          <b>Escopo:</b> Reforma mobile-first completa de sites antigos, lentos ou não responsivos para celular.<br><br>
          <b>Fit:</b> Empresas tradicionais que já têm site há anos, mas perdem tráfego no celular.
        </p>
      </div>
      <div class="metric-card">
        <h3 style="color: #8ea89d; font-size: 16px; margin-bottom: 8px;">🗺️ Blindagem Maps</h3>
        <p style="font-size: 22px; font-weight: 800; color: #fff;">R$ 450,00</p>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 8px; line-height: 1.45;">
          <b>Escopo:</b> Regularização, reivindicação e blindagem de categoria e horários no Google Maps.<br><br>
          <b>Fit:</b> Empresas locais com ficha abandonada ou com dados incorretos.
        </p>
      </div>
    </div>
  </div>

</div>

<script>
const LEADS_100 = ''' + json.dumps(leads_100, ensure_ascii=False) + ''';
let CURRENT_DATA = null;
let SELECTED_CHAT_PHONE = null;
let DB_ACTIVE_FILTER = 'all';

function switchTab(tabId, el) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  if (el) el.classList.add('active');
}

function loadSubCRMData() {
  fetch('/api/subcrm-data')
    .then(r => r.json())
    .then(data => {
      CURRENT_DATA = data;
      renderSubCRM(data);
    })
    .catch(err => {
      console.log('Erro ao carregar dados:', err);
    });
}

function renderSubCRM(data) {
  const q = data.queue || {};
  const stats = data.stats || {};
  const chats = data.chats || [];
  const pending = data.pending;

  // Atualiza métricas
  const sentCount = (q.sent || []).length;
  const failedCount = (q.failed || []).length;
  const totalQueue = q.total || 30;
  document.getElementById('metricQueueProgress').innerText = `${sentCount + failedCount} / ${totalQueue}`;
  document.getElementById('badgeQueueCount').innerText = `${sentCount + failedCount}/${totalQueue}`;
  document.getElementById('metricConversasCount').innerText = chats.length;
  document.getElementById('badgeInboxCount').innerText = chats.length;

  // Fila pausada ou ativa
  const qBtn = document.getElementById('queueToggleBtn');
  if (q.is_paused) {
    qBtn.innerText = '▶️ Retomar Fila';
    qBtn.classList.add('paused');
  } else {
    qBtn.innerText = '⏸️ Pausar Fila';
    qBtn.classList.remove('paused');
  }

  // Pending box
  const pendingBox = document.getElementById('pendingBox');
  if (pending && pending.reply) {
    pendingBox.style.display = 'flex';
    document.getElementById('pendingTextSnippet').innerText = `"${pending.reply}" (Para ${pending.name || pending.phone})`;
  } else {
    pendingBox.style.display = 'none';
  }

  // Renderiza Chats
  renderChatList(chats);
  renderQueueTable(q);
}

function renderChatList(chats) {
  const container = document.getElementById('chatListContainer');
  container.innerHTML = '';

  if (!chats.length) {
    container.innerHTML = '<div style="padding: 20px; color: var(--text-muted); font-size: 13px;">Nenhuma conversa registrada ainda.</div>';
    return;
  }

  chats.forEach((c, idx) => {
    const item = document.createElement('div');
    item.className = 'chat-item' + (SELECTED_CHAT_PHONE === c.phone || (!SELECTED_CHAT_PHONE && idx === 0) ? ' active' : '');
    item.onclick = () => selectChat(c.phone);

    const timeStr = c.last_at ? c.last_at.split('T')[1]?.slice(0, 5) : '';
    item.innerHTML = `
      <div class="chat-item-header">
        <span class="chat-item-name">${c.name}</span>
        <span class="chat-item-time">${timeStr}</span>
      </div>
      <div class="chat-item-preview">${c.last_msg || 'Sem mensagens'}</div>
    `;
    container.appendChild(item);
  });

  if (!SELECTED_CHAT_PHONE && chats.length > 0) {
    selectChat(chats[0].phone);
  }
}

function selectChat(phone) {
  SELECTED_CHAT_PHONE = phone;
  document.querySelectorAll('.chat-item').forEach(el => el.classList.remove('active'));

  if (!CURRENT_DATA) return;
  const chat = (CURRENT_DATA.chats || []).find(c => c.phone === phone);
  if (!chat) return;

  document.getElementById('activeChatName').innerText = chat.name;
  document.getElementById('activeChatPhone').innerText = chat.phone;
  document.getElementById('activeChatWhatsAppLink').href = `https://wa.me/${chat.phone}`;

  const msgsContainer = document.getElementById('chatMessagesContainer');
  msgsContainer.innerHTML = '';

  (chat.messages || []).forEach(m => {
    const isOut = m.role && m.role.includes('Vocação');
    const b = document.createElement('div');
    b.className = 'chat-bubble ' + (isOut ? 'outbound' : 'inbound');
    const timeStr = m.at ? m.at.split('T')[1]?.slice(0, 5) : '';
    b.innerHTML = `
      <div>${m.text}</div>
      <div class="bubble-meta">${isOut ? 'Vocação' : chat.name} · ${timeStr}</div>
    `;
    msgsContainer.appendChild(b);
  });
  msgsContainer.scrollTop = msgsContainer.scrollHeight;
}

function sendCustomMessage() {
  const input = document.getElementById('customReplyInput');
  const text = input.value.trim();
  if (!text || !SELECTED_CHAT_PHONE) return;

  fetch('/api/send-message', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ phone: SELECTED_CHAT_PHONE, text: text })
  })
  .then(r => r.json())
  .then(res => {
    input.value = '';
    loadSubCRMData();
  });
}

function approvePending() {
  fetch('/api/approve', { method: 'POST' })
    .then(r => r.json())
    .then(res => {
      alert(res.message);
      loadSubCRMData();
    });
}

function toggleQueue() {
  fetch('/api/toggle-queue', { method: 'POST' })
    .then(r => r.json())
    .then(res => {
      loadSubCRMData();
    });
}

function renderQueueTable(queue) {
  const tbody = document.getElementById('queueTableBody');
  tbody.innerHTML = '';

  const leads = queue.leads || [];
  const sentSet = new Set(queue.sent || []);
  const failedSet = new Set(queue.failed || []);

  leads.forEach(l => {
    let statusBadge = '<span class="badge badge-pending">Na Fila</span>';
    if (sentSet.has(l.phone)) {
      statusBadge = '<span class="badge badge-sent">✅ Enviado</span>';
    } else if (failedSet.has(l.phone)) {
      statusBadge = '<span class="badge badge-failed">❌ Sem WhatsApp</span>';
    }

    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${statusBadge}</td>
      <td><strong>${l.name}</strong><br><span style="font-size: 11px; color: var(--text-muted);">${l.cat}</span></td>
      <td>${l.bairro}</td>
      <td style="font-family: monospace;">${l.phone}</td>
      <td><span class="badge badge-gold">${l.oferta_nome.split('(')[0]}</span></td>
      <td style="font-weight: 700;">R$ ${l.oferta_preco.toFixed(2)}</td>
      <td style="font-size: 11.5px; color: var(--text-muted); max-width: 320px;">"${l.hook_whatsapp.slice(0, 90)}..."</td>
    `;
    tbody.appendChild(tr);
  });
}

function renderDatabaseTable() {
  const tbody = document.getElementById('dbTableBody');
  tbody.innerHTML = '';
  const term = (document.getElementById('searchInput').value || '').toLowerCase().trim();

  LEADS_100.forEach(l => {
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

    if (matchesSearch && matchesChip) {
      const score = l.interesse_vendedor || 75;
      const scoreColor = score >= 90 ? '#48bb78' : (score >= 75 ? '#38b2ac' : '#a0aec0');
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${l.name}</strong><br><span style="font-size: 11px; color: var(--text-muted);">${l.cat}</span></td>
        <td><span class="badge" style="background:#1f2d26; color:#79f2c3;">${l.bairro}</span><br><span style="font-size: 11px; color: var(--text-muted);">${l.addr}</span></td>
        <td style="font-family: monospace; color: ${l.phone.includes('9') ? '#79f2c3' : '#cbd5e0'};">${l.phone}</td>
        <td><strong>${l.oferta_nome.split('(')[0]}</strong><br><span style="color: #ffd27a; font-weight: bold;">R$ ${l.oferta_preco.toFixed(2)}</span></td>
        <td>
          <span style="font-weight: 800; color: ${scoreColor}; font-size: 14px;">${score}%</span>
          <div style="font-size: 10.5px; color: var(--text-muted);">${l.interesse_tag || ''}</div>
        </td>
      `;
      tbody.appendChild(tr);
    }
  });
}

function setDbFilter(f, el) {
  DB_ACTIVE_FILTER = f;
  document.querySelectorAll('.filter-chips .chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  renderDatabaseTable();
}

function filterDatabaseLeads() {
  renderDatabaseTable();
}

// Inicialização
renderDatabaseTable();
loadSubCRMData();
setInterval(loadSubCRMData, 5000);
</script>

</body>
</html>
'''

    with open('auto_responder_docker/templates/painel.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Sub-CRM Executivo gerado com sucesso em auto_responder_docker/templates/painel.html!")

if __name__ == '__main__':
    generate_subcrm()
