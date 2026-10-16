import os

painel_path = r"c:\Vocação 2027\QG Vocação 2027 do zero\auto_responder_docker\templates\painel.html"

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vocação 2027 · Cockpit Comercial & Fila Gamificada</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg-main: #070d0a;
    --bg-card: #0f1712;
    --bg-card-hover: #142019;
    --border: #1a2a20;
    --border-bright: #2d4636;
    --primary: #10b981;
    --primary-glow: rgba(16, 185, 129, 0.25);
    --accent: #34d399;
    --gold: #f59e0b;
    --gold-glow: rgba(245, 158, 11, 0.2);
    --danger: #ef4444;
    --danger-soft: rgba(239, 68, 68, 0.15);
    --info: #38bdf8;
    --text-main: #f0fdf4;
    --text-muted: #94a3b8;
    --text-dim: #64748b;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background-color: var(--bg-main);
    color: var(--text-main);
    font-family: 'Plus Jakarta Sans', sans-serif;
    min-height: 100vh;
    padding-bottom: 60px;
    -webkit-font-smoothing: antialiased;
  }

  /* TOP COCKPIT */
  .cockpit-header {
    background: rgba(15, 23, 18, 0.95);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(16px);
    position: sticky;
    top: 0;
    z-index: 100;
    padding: 14px 24px;
  }
  .cockpit-inner {
    max-width: 1680px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }
  .brand-area {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .logo-box {
    width: 42px;
    height: 42px;
    background: linear-gradient(135deg, #10b981 0%, #047857 100%);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 20px;
    color: #fff;
    box-shadow: 0 0 20px var(--primary-glow);
  }
  .brand-title {
    font-size: 17px;
    font-weight: 800;
    letter-spacing: -0.3px;
  }
  .brand-sub {
    font-size: 11.5px;
    color: var(--text-muted);
  }

  /* GAMIFICATION BAR */
  .gamification-strip {
    display: flex;
    align-items: center;
    gap: 20px;
    background: #09120c;
    padding: 8px 18px;
    border-radius: 12px;
    border: 1px solid var(--border);
  }
  .rank-badge {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 700;
    font-size: 13px;
    color: var(--gold);
  }
  .xp-box {
    display: flex;
    flex-direction: column;
    gap: 4px;
    width: 140px;
  }
  .xp-label {
    display: flex;
    justify-content: space-between;
    font-size: 10.5px;
    font-weight: 700;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
  }
  .xp-bar {
    height: 6px;
    background: #1a2a20;
    border-radius: 4px;
    overflow: hidden;
  }
  .xp-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--gold) 0%, var(--primary) 100%);
    width: 74%;
    box-shadow: 0 0 10px var(--primary-glow);
  }

  /* CONTROLS AREA */
  .controls-area {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .toggle-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.2s ease;
  }
  .toggle-auto-off {
    background: rgba(239, 68, 68, 0.15);
    color: #fca5a5;
    border-color: rgba(239, 68, 68, 0.4);
  }
  .toggle-auto-on {
    background: rgba(16, 185, 129, 0.2);
    color: #6ee7b7;
    border-color: var(--primary);
    box-shadow: 0 0 15px var(--primary-glow);
  }
  .btn-queue {
    background: #152219;
    color: var(--text-main);
    border: 1px solid var(--border-bright);
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
  }
  .btn-queue:hover { background: #1c3023; }
  .btn-action-primary {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: #fff;
    border: none;
    padding: 8px 16px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 0 15px var(--primary-glow);
  }
  .btn-action-primary:hover { filter: brightness(1.1); }

  /* TABS */
  .tabs-nav {
    max-width: 1680px;
    margin: 20px auto 0;
    padding: 0 24px;
    display: flex;
    gap: 12px;
    border-bottom: 1px solid var(--border);
  }
  .tab-btn {
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-size: 13.5px;
    font-weight: 700;
    padding: 12px 18px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 3px solid transparent;
    transition: all 0.2s;
  }
  .tab-btn.active {
    color: var(--primary);
    border-bottom-color: var(--primary);
  }
  .tab-badge {
    background: #1a2a20;
    color: var(--accent);
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
  }

  /* MAIN WRAPPER */
  .main-wrapper {
    max-width: 1680px;
    margin: 24px auto;
    padding: 0 24px;
  }
  .tab-content { display: none; }
  .tab-content.active { display: block; }

  /* GAMIFIED STATS ROW */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }
  .stat-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .stat-label {
    font-size: 11.5px;
    color: var(--text-muted);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .stat-value {
    font-size: 24px;
    font-weight: 800;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* COCKPIT FILA */
  .queue-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 24px;
  }
  .countdown-box {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #09120c;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 16px;
  }
  .countdown-timer {
    font-family: 'JetBrains Mono', monospace;
    font-size: 28px;
    font-weight: 800;
    color: var(--accent);
  }

  /* CHAT SPLIT VIEW (ATENDIMENTO & A/B) */
  .chat-cockpit {
    display: grid;
    grid-template-columns: 340px 1fr 480px;
    gap: 20px;
    min-height: 640px;
  }
  @media (max-width: 1280px) {
    .chat-cockpit { grid-template-columns: 300px 1fr; }
    .ab-panel { grid-column: span 2; }
  }
  .chat-sidebar {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow-y: auto;
    max-height: 680px;
  }
  .chat-item {
    padding: 14px 16px;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    transition: background 0.15s;
  }
  .chat-item:hover, .chat-item.active { background: var(--bg-card-hover); }
  .chat-item-name { font-weight: 700; font-size: 13.5px; margin-bottom: 4px; display: flex; justify-content: space-between; }
  .chat-item-msg { font-size: 12px; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

  .chat-messages-box {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    max-height: 680px;
  }
  .messages-flow {
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding-right: 6px;
    max-height: 520px;
  }
  .msg-bubble {
    max-width: 80%;
    padding: 12px 16px;
    border-radius: 14px;
    font-size: 13px;
    line-height: 1.45;
  }
  .msg-bubble.lead {
    align-self: flex-start;
    background: #16241c;
    border: 1px solid var(--border-bright);
    color: #e2e8f0;
  }
  .msg-bubble.vocacao {
    align-self: flex-end;
    background: #064e3b;
    color: #ecfdf5;
  }

  /* A/B PROPOSAL BOX */
  .ab-panel {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    max-height: 680px;
    overflow-y: auto;
  }
  .jev-pill-header {
    background: #09120c;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 14px;
    font-size: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .ab-box {
    background: #0a130e;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .ab-box.opt-a { border-left: 4px solid var(--primary); }
  .ab-box.opt-b { border-left: 4px solid var(--gold); }
  .ab-title { font-size: 12px; font-weight: 800; display: flex; justify-content: space-between; }
  .ab-textarea {
    width: 100%;
    height: 90px;
    background: #050a07;
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text-main);
    font-family: inherit;
    font-size: 12px;
    padding: 10px;
    resize: vertical;
  }
  .ab-textarea:focus { outline: none; border-color: var(--primary); }

  /* HIGH TICKET TABLE */
  .table-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 20px;
    overflow-x: auto;
  }
  .filter-bar {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }
  .filter-chip {
    background: #0a130e;
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 12px;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .filter-chip:hover, .filter-chip.active {
    background: var(--primary);
    color: #fff;
    border-color: var(--primary);
  }
  table.lead-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
  }
  table.lead-table th {
    text-align: left;
    padding: 12px 14px;
    background: #09120c;
    color: var(--text-muted);
    font-size: 11px;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.5px;
    border-bottom: 1px solid var(--border);
  }
  table.lead-table td {
    padding: 14px;
    border-bottom: 1px solid var(--border);
    vertical-align: middle;
  }
  table.lead-table tr:hover { background: var(--bg-card-hover); }
  .badge-jev {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    padding: 3px 8px;
    border-radius: 6px;
    font-weight: 700;
    display: inline-block;
  }
  .badge-jev.start { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
  .badge-jev.update { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
  .badge-jev.tour { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }

  .action-btn-group {
    display: flex;
    gap: 6px;
  }
  .btn-link-action {
    background: #142219;
    border: 1px solid var(--border-bright);
    color: var(--text-main);
    padding: 6px 10px;
    border-radius: 8px;
    text-decoration: none;
    font-size: 11.5px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .btn-link-action:hover { background: #1c3224; color: #fff; }
</style>
</head>
<body>

<!-- COCKPIT HEADER -->
<header class="cockpit-header">
  <div class="cockpit-inner">
    <div class="brand-area">
      <div class="logo-box">V</div>
      <div>
        <div class="brand-title">Vocação 2027 · Cockpit Comercial</div>
        <div class="brand-sub">Inteligência Jev System One & Alta Densidade</div>
      </div>
    </div>

    <!-- GAMIFICATION STRIP -->
    <div class="gamification-strip">
      <div class="rank-badge">
        <span>🏆 Nível 4</span>
        <span style="color:var(--text-muted); font-size:11px;">Sniper Alto Ticket</span>
      </div>
      <div class="xp-box">
        <div class="xp-label">
          <span>XP</span>
          <span>1.850 / 2.500</span>
        </div>
        <div class="xp-bar">
          <div class="xp-fill"></div>
        </div>
      </div>
      <div style="font-size:12px; font-weight:700; color:var(--accent);">
        💰 R$ 4.850.000+ <span style="font-size:10px; color:var(--text-muted);">em jogo</span>
      </div>
    </div>

    <!-- CONTROLS -->
    <div class="controls-area">
      <!-- TOGGLE AUTO-RESPONDER -->
      <button id="autoResponderToggle" class="toggle-btn toggle-auto-off" onclick="toggleAutoResponder()">
        <span id="autoResponderDot">🔴</span>
        <span id="autoResponderLabel">Auto-Responder: MANUAL SEGURO</span>
      </button>

      <!-- TOGGLE FILA -->
      <button id="queueToggleBtn" class="btn-queue" onclick="toggleQueue()">
        ⏸️ Pausar Fila
      </button>

      <!-- DISPARAR JÁ -->
      <button class="btn-action-primary" onclick="triggerNextNow()">
        ⚡ Disparar Já
      </button>
    </div>
  </div>
</header>

<!-- TABS NAVIGATION -->
<div class="tabs-nav">
  <button class="tab-btn active" onclick="switchTab('tab-fila', this)">
    ⚡ Fila & Cockpit ao Vivo <span class="tab-badge" id="queueBadge">0</span>
  </button>
  <button class="tab-btn" onclick="switchTab('tab-chat', this)">
    💬 Atendimento & Respostas A/B <span class="tab-badge" id="chatBadge">0</span>
  </button>
  <button class="tab-btn" onclick="switchTab('tab-leads', this)">
    💎 Leads de Alto Ticket Verificados <span class="tab-badge" id="leadsBadge">71</span>
  </button>
</div>

<!-- MAIN WRAPPER -->
<div class="main-wrapper">

  <!-- TAB 1: FILA AO VIVO -->
  <div id="tab-fila" class="tab-content active">
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-label">Pipeline em Jogo</div>
        <div class="stat-value" style="color:var(--accent);">R$ 4.850.000+</div>
        <div style="font-size:11px; color:var(--text-muted);">71 empresas de Alto Padrão de Sorocaba</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Disparos Entregues</div>
        <div class="stat-value" id="statSentCount" style="color:var(--primary);">26</div>
        <div style="font-size:11px; color:var(--text-muted);">Histórico gravado no Twenty CRM</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Taxa de Resposta / Diálogo</div>
        <div class="stat-value" style="color:var(--gold);">19.2%</div>
        <div style="font-size:11px; color:var(--text-muted);">Clínicas e negócios locais em negociação</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Status da Automação</div>
        <div class="stat-value" id="automationStatusPill" style="font-size:16px; color:#fca5a5;">
          🔒 100% MANUAL SEGURO
        </div>
        <div style="font-size:11px; color:var(--text-muted);">Zero risco de disparos acidentais</div>
      </div>
    </div>

    <!-- COCKPIT DE CADÊNCIA -->
    <div class="queue-card">
      <div class="countdown-box">
        <div>
          <h3 style="font-size:15px; margin-bottom:4px;">⏱️ Próximo Disparo em:</h3>
          <p style="font-size:12px; color:var(--text-muted);">Intervalo anti-bloqueio Meta com respeito à janela comercial</p>
        </div>
        <div class="countdown-timer" id="countdownTimer">--:--</div>
      </div>

      <div style="font-size:13px; font-weight:700; margin-bottom:12px;">Fila Ativa de Disparo Frio:</div>
      <div id="queueListContainer" style="display:flex; flex-direction:column; gap:8px;">
        <div style="color:var(--text-muted); font-size:12.5px; padding:12px; background:#09120c; border-radius:8px;">
          Fila pausada e protegida. Selecione leads na aba "Leads de Alto Ticket" para carregar novos disparos.
        </div>
      </div>
    </div>
  </div>

  <!-- TAB 2: ATENDIMENTO & RESPOSTAS A/B -->
  <div id="tab-chat" class="tab-content">
    <div class="chat-cockpit">
      <!-- SIDEBAR LIST -->
      <div class="chat-sidebar" id="chatListSidebar">
        <!-- Rendered via JS -->
      </div>

      <!-- MESSAGES FLOW -->
      <div class="chat-messages-box">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border); padding-bottom:12px; margin-bottom:14px;">
            <div>
              <div id="activeChatName" style="font-weight:800; font-size:15px;">Selecione uma conversa</div>
              <div id="activeChatPhone" style="font-size:11.5px; color:var(--text-muted);">---</div>
            </div>
            <div id="activeChatJev" style="display:flex; gap:6px;"></div>
          </div>
          <div class="messages-flow" id="messagesFlow">
            <div style="color:var(--text-muted); font-size:12.5px; text-align:center; padding:40px;">
              Clique em um lead à esquerda para abrir a conversa.
            </div>
          </div>
        </div>

        <!-- MANUAL INPUT -->
        <div style="margin-top:16px; display:flex; gap:10px;">
          <input type="text" id="manualInputMsg" placeholder="Digitar mensagem manual personalizada..." style="flex:1; background:#09120c; border:1px solid var(--border); border-radius:10px; color:#fff; padding:10px 14px; font-size:12.5px;">
          <button class="btn-action-primary" onclick="sendManualMsg()">Enviar</button>
        </div>
      </div>

      <!-- PAINEL DE SUGESTÕES A/B -->
      <div class="ab-panel">
        <div class="jev-pill-header">
          <span style="font-weight:700;">🧠 Diagnóstico Jev System One</span>
          <span id="jevFitBadge" style="color:var(--accent); font-weight:700;">85% Fit</span>
        </div>

        <div style="font-size:12.5px; font-weight:700; color:var(--text-muted);">
          Escolha ou edite a resposta antes de enviar:
        </div>

        <!-- OPÇÃO A -->
        <div class="ab-box opt-a">
          <div class="ab-title">
            <span style="color:#34d399;">🅰️ OPÇÃO A: Autoridade & Estrutura Técnica</span>
            <span style="font-size:10px; color:var(--text-muted);">85% Jev Match</span>
          </div>
          <textarea id="replyTextA" class="ab-textarea"></textarea>
          <button class="btn-action-primary" style="background:#059669;" onclick="dispatchSuggestion('A')">
            🚀 Disparar Resposta A
          </button>
        </div>

        <!-- OPÇÃO B -->
        <div class="ab-box opt-b">
          <div class="ab-title">
            <span style="color:#fbbf24;">🅱️ OPÇÃO B: Custo de Oportunidade & Concorrência</span>
            <span style="font-size:10px; color:var(--text-muted);">75% Jev Match</span>
          </div>
          <textarea id="replyTextB" class="ab-textarea"></textarea>
          <button class="btn-action-primary" style="background:#d97706;" onclick="dispatchSuggestion('B')">
            🚀 Disparar Resposta B
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- TAB 3: BANCO DE LEADS ALTO TICKET (71) -->
  <div id="tab-leads" class="tab-content">
    <div class="table-card">
      <div class="filter-bar">
        <button class="filter-chip active" onclick="filterCategory('all', this)">Todos (71)</button>
        <button class="filter-chip" onclick="filterCategory('marcenarias', this)">🪵 Marcenarias de Luxo (36)</button>
        <button class="filter-chip" onclick="filterCategory('garagens', this)">🚗 Garagens Seminovos (15)</button>
        <button class="filter-chip" onclick="filterCategory('industrias', this)">🏭 Indústrias B2B (20)</button>
        <span style="margin:0 10px; color:var(--border);">|</span>
        <button class="filter-chip" onclick="filterJev('Update', this)">🎯 Jev: Update R$ 980</button>
        <button class="filter-chip" onclick="filterJev('Combo', this)">🎯 Jev: Combo 360° R$ 950</button>
        <button class="filter-chip" onclick="filterJev('Portal', this)">🎯 Jev: Portal B2B R$ 1.500</button>
        <input type="text" id="leadSearchInput" onkeyup="searchLeads()" placeholder="🔍 Buscar empresa, bairro ou telefone..." style="margin-left:auto; background:#09120c; border:1px solid var(--border); border-radius:10px; color:#fff; padding:6px 12px; font-size:12px; width:260px;">
      </div>

      <table class="lead-table">
        <thead>
          <tr>
            <th>Empresa & Categoria</th>
            <th>Localização / Bairro</th>
            <th>WhatsApp</th>
            <th>Ticket Médio</th>
            <th>Gargalo Identificado</th>
            <th>Oferta Jev</th>
            <th>Ações Rápidas</th>
          </tr>
        </thead>
        <tbody id="leadsTableBody">
          <!-- Rendered via JS -->
        </tbody>
      </table>
    </div>
  </div>

</div>

<script>
let currentData = null;
let activePhone = null;
let allHighTicketLeads = [];
let activeCatFilter = 'all';
let activeJevFilter = 'all';

function switchTab(tabId, btn) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  btn.classList.add('active');
}

async function fetchDashboardData() {
  try {
    const res = await fetch('/api/subcrm-data');
    const data = await res.json();
    currentData = data;
    renderCockpit(data);
  } catch (e) {
    console.error("Erro fetch data:", e);
  }
}

function renderCockpit(data) {
  // 1. Controls
  const autoBtn = document.getElementById('autoResponderToggle');
  const autoDot = document.getElementById('autoResponderDot');
  const autoLabel = document.getElementById('autoResponderLabel');
  if (data.auto_responder_enabled) {
    autoBtn.className = "toggle-btn toggle-auto-on";
    autoDot.innerText = "🟢";
    autoLabel.innerText = "Auto-Responder: ATIVO";
    document.getElementById('automationStatusPill').innerHTML = "🟢 AUTO-RESPONDER ATIVO";
    document.getElementById('automationStatusPill').style.color = "#34d399";
  } else {
    autoBtn.className = "toggle-btn toggle-auto-off";
    autoDot.innerText = "🔴";
    autoLabel.innerText = "Auto-Responder: MANUAL SEGURO";
    document.getElementById('automationStatusPill').innerHTML = "🔒 100% MANUAL SEGURO";
    document.getElementById('automationStatusPill').style.color = "#fca5a5";
  }

  const qBtn = document.getElementById('queueToggleBtn');
  if (data.queue.is_paused) {
    qBtn.innerText = "▶️ Retomar Fila";
    qBtn.style.borderColor = "var(--primary)";
  } else {
    qBtn.innerText = "⏸️ Pausar Fila";
    qBtn.style.borderColor = "var(--border-bright)";
  }

  // Timer
  const secs = data.queue.countdown_seconds || 0;
  const m = Math.floor(secs / 60);
  const s = secs % 60;
  document.getElementById('countdownTimer').innerText = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;

  // Badges
  document.getElementById('queueBadge').innerText = data.queue.total || 0;
  document.getElementById('chatBadge').innerText = data.chats.length || 0;

  // Chats list
  renderChatSidebar(data.chats);

  // Leads
  if (data.high_ticket_leads && data.high_ticket_leads.length > 0 && allHighTicketLeads.length === 0) {
    allHighTicketLeads = data.high_ticket_leads;
    document.getElementById('leadsBadge').innerText = allHighTicketLeads.length;
    renderHighTicketTable();
  }
}

function renderChatSidebar(chats) {
  const container = document.getElementById('chatListSidebar');
  if (!chats || chats.length === 0) {
    container.innerHTML = '<div style="padding:20px; color:var(--text-muted); font-size:12px;">Nenhum atendimento ativo.</div>';
    return;
  }
  container.innerHTML = chats.map(c => `
    <div class="chat-item ${c.phone === activePhone ? 'active' : ''}" onclick="selectChat('${c.phone}')">
      <div class="chat-item-name">
        <span>${c.name}</span>
        <span style="font-size:10px; color:var(--text-dim);">${c.last_at ? c.last_at.slice(11, 16) : ''}</span>
      </div>
      <div class="chat-item-msg">${c.last_msg || 'Sem mensagens'}</div>
    </div>
  `).join('');

  if (!activePhone && chats.length > 0) {
    selectChat(chats[0].phone);
  }
}

function selectChat(phone) {
  activePhone = phone;
  const chat = currentData.chats.find(c => c.phone === phone);
  if (!chat) return;

  document.getElementById('activeChatName').innerText = chat.name;
  document.getElementById('activeChatPhone').innerText = `+${chat.phone} · ${chat.bairro || 'Sorocaba'}`;
  document.getElementById('activeChatJev').innerHTML = `<span class="badge-jev start">${chat.oferta_nome || 'Vocação Start'}</span>`;

  // Render messages
  const flow = document.getElementById('messagesFlow');
  flow.innerHTML = (chat.messages || []).map(m => `
    <div class="msg-bubble ${m.role && m.role.includes('Lead') ? 'lead' : 'vocacao'}">
      <div style="font-size:10.5px; opacity:0.7; margin-bottom:3px;">${m.role}</div>
      <div>${m.text}</div>
    </div>
  `).join('');
  flow.scrollTop = flow.scrollHeight;

  // Default A/B suggestions
  document.getElementById('replyTextA').value = `Olá! Sou o Eduardo, da Vocação Comunicação aqui de Sorocaba. Vi que vocês possuem um trabalho de excelência no ${chat.bairro || 'bairro'}, mas quem pesquisa pelos seus serviços no Google ainda não encontra uma vitrine digital à altura para passar confiança de primeira. O meu trabalho aqui na cidade é justamente estruturar essa autoridade visual no Maps e no celular. Como é um assunto ligado à imagem da empresa, com quem posso falar sobre isso?`;
  document.getElementById('replyTextB').value = `Olá! Sou o Eduardo, da Vocação aqui de Sorocaba. Analisei a busca local do segmento de vocês na nossa região e notei que quem pesquisa pelos seus serviços no Google acaba encontrando opções vizinhas antes de vocês por detalhes de otimização no Maps e ausência de canal direto rápido. Posso te enviar um resumo mostrando como posicionar a empresa como primeira escolha local?`;
}

async function dispatchSuggestion(type) {
  if (!activePhone) return alert("Selecione um lead primeiro.");
  const text = (type === 'A') ? document.getElementById('replyTextA').value : document.getElementById('replyTextB').value;
  if (!text || text.length < 5) return alert("Texto muito curto.");

  try {
    const res = await fetch('/api/send-message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: json.stringify({ phone: activePhone, text: text })
    });
    const d = await res.json();
    if (d.success) {
      alert(`✅ Resposta ${type} disparada com sucesso para o lead!`);
      fetchDashboardData();
    }
  } catch (e) {
    alert("Erro ao disparar: " + e);
  }
}

async function sendManualMsg() {
  if (!activePhone) return alert("Selecione um lead primeiro.");
  const input = document.getElementById('manualInputMsg');
  const text = input.value.trim();
  if (!text) return;

  try {
    const res = await fetch('/api/send-message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ phone: activePhone, text: text })
    });
    const d = await res.json();
    if (d.success) {
      input.value = "";
      fetchDashboardData();
    }
  } catch (e) {
    alert("Erro: " + e);
  }
}

async function toggleAutoResponder() {
  const res = await fetch('/api/toggle-auto-responder', { method: 'POST' });
  const d = await res.json();
  fetchDashboardData();
}

async function toggleQueue() {
  const res = await fetch('/api/toggle-queue', { method: 'POST' });
  fetchDashboardData();
}

async function triggerNextNow() {
  const res = await fetch('/api/trigger-next', { method: 'POST' });
  alert("⚡ Disparo imediato acionado na fila!");
  fetchDashboardData();
}

// HIGH TICKET TABLE FILTERING
function filterCategory(cat, btn) {
  activeCatFilter = cat;
  document.querySelectorAll('.filter-bar .filter-chip').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderHighTicketTable();
}

function filterJev(tag, btn) {
  activeJevFilter = tag;
  renderHighTicketTable();
}

function searchLeads() {
  renderHighTicketTable();
}

function renderHighTicketTable() {
  const tbody = document.getElementById('leadsTableBody');
  const q = document.getElementById('leadSearchInput').value.toLowerCase();

  const filtered = allHighTicketLeads.filter(l => {
    if (activeCatFilter !== 'all' && l.category !== activeCatFilter) return false;
    if (activeJevFilter !== 'all' && !l.jev_oferta.includes(activeJevFilter)) return false;
    if (q) {
      const match = l.name.toLowerCase().includes(q) || l.bairro.toLowerCase().includes(q) || l.phone.includes(q);
      if (!match) return false;
    }
    return true;
  });

  tbody.innerHTML = filtered.map(l => `
    <tr>
      <td>
        <div style="font-weight:700;">${l.name}</div>
        <div style="font-size:11px; color:var(--text-muted);">${l.segment}</div>
      </td>
      <td>
        <div>${l.bairro}</div>
        <div style="font-size:11px; color:var(--text-dim); max-width:240px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${l.address}</div>
      </td>
      <td>
        <span style="font-family:'JetBrains Mono',monospace;">${l.phone || 'Sem telefone'}</span>
      </td>
      <td>
        <span style="color:var(--gold); font-weight:700;">${l.ticket}</span>
      </td>
      <td style="max-width:260px; font-size:11.5px; color:var(--text-muted);">
        ${l.gargalo || 'Presença digital em qualificação'}
      </td>
      <td>
        <span class="badge-jev ${l.jev_oferta.includes('Update') ? 'update' : (l.jev_oferta.includes('Combo') ? 'tour' : 'start')}">
          ${l.jev_oferta}
        </span>
      </td>
      <td>
        <div class="action-btn-group">
          ${l.maps_url ? `<a href="${l.maps_url}" target="_blank" class="btn-link-action" title="Abrir Google Maps Real">📍 Maps</a>` : ''}
          ${l.phone ? `<a href="https://wa.me/${l.phone}" target="_blank" class="btn-link-action" title="Abrir WhatsApp Web">💬 Whats</a>` : ''}
          <button class="btn-link-action" onclick="addLeadToQueue('${l.id}')" title="Adicionar à Fila">➕ Fila</button>
        </div>
      </td>
    </tr>
  `).join('');
}

async function addLeadToQueue(id) {
  const lead = allHighTicketLeads.find(l => l.id === id);
  if (!lead) return;

  const payload = {
    id: lead.id,
    name: lead.name,
    phone: lead.phone,
    bairro: lead.bairro,
    oferta_nome: lead.jev_oferta,
    hook_whatsapp: lead.hook_a || "Olá! Notei a excelente estrutura de vocês no Google..."
  };

  const res = await fetch('/api/add-to-queue', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  const d = await res.json();
  if (d.success) {
    alert(`✅ ${lead.name} adicionado à fila com sucesso! Total na fila: ${d.total}`);
    fetchDashboardData();
  }
}

// Initial poll
fetchDashboardData();
setInterval(fetchDashboardData, 3000);
</script>
</body>
</html>
"""

with open(painel_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Novo painel.html gamificado criado com sucesso!")
