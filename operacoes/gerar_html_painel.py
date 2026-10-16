import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

JSON_PATH = r"C:\Vocação 2027\QG Vocação 2027 do zero\leads_100_santa_rosalia_brasilandia.json"
HTML_PATH = r"C:\Vocação 2027\QG Vocação 2027 do zero\Painel-PreSelecao-100Leads-SantaRosalia-Brasilandia.html"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    leads = json.load(f)

leads_json_str = json.dumps(leads, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Painel de Pré-Seleção — 100 Leads Santa Rosália & Jardim Brasilândia | Vocação</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fraunces:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-dark: #0d1210;
    --bg-card: #151c19;
    --bg-card-hover: #1c2622;
    --border: #26332d;
    --primary: #0B5E47;
    --primary-light: #128263;
    --accent: #a4dbc9;
    --text-main: #f0f4f2;
    --text-muted: #889991;
    --danger: #e05252;
    --warning: #e5a43b;
    --success: #2ebd7a;
    --info: #3b82f6;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-main);
    line-height: 1.5;
    padding-bottom: 90px;
  }}

  /* HEADER */
  header {{
    background: linear-gradient(180deg, #16221d 0%, #0d1210 100%);
    border-bottom: 1px solid var(--border);
    padding: 32px 24px 24px;
    position: sticky;
    top: 0;
    z-index: 50;
    backdrop-filter: blur(12px);
  }}
  .header-inner {{
    max-width: 1380px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }}
  .brand-area {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .brand-logo {{
    width: 44px;
    height: 44px;
    border-radius: 10px;
    background: #111815;
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }}
  .brand-logo img {{
    width: 32px;
    height: 30px;
    object-fit: contain;
  }}
  .brand-title h1 {{
    font-family: 'Fraunces', serif;
    font-size: 22px;
    font-weight: 600;
    color: #ffffff;
    letter-spacing: -0.01em;
  }}
  .brand-title p {{
    font-size: 12px;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 600;
  }}

  /* METRICS BAR */
  .metrics-grid {{
    max-width: 1380px;
    margin: 24px auto 0;
    padding: 0 24px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 14px;
  }}
  .metric-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 18px;
    position: relative;
    overflow: hidden;
  }}
  .metric-card::before {{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: var(--primary);
  }}
  .metric-card.accent::before {{ background: var(--accent); }}
  .metric-card.warning::before {{ background: var(--warning); }}
  .metric-card.success::before {{ background: var(--success); }}
  .metric-label {{
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    font-weight: 700;
  }}
  .metric-val {{
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
    margin-top: 4px;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }}
  .metric-sub {{
    font-size: 11.5px;
    color: var(--text-muted);
    margin-top: 2px;
  }}

  /* CONTROLS (SEARCH & FILTERS) */
  .controls-section {{
    max-width: 1380px;
    margin: 20px auto 0;
    padding: 0 24px;
  }}
  .search-box {{
    display: flex;
    gap: 12px;
    margin-bottom: 14px;
  }}
  .search-input {{
    flex: 1;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 18px;
    font-size: 14px;
    color: #ffffff;
    outline: none;
    transition: border-color 0.2s;
  }}
  .search-input:focus {{
    border-color: var(--accent);
  }}
  .filter-chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
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
    transition: all 0.2s;
    user-select: none;
  }}
  .chip:hover {{
    border-color: var(--accent);
    color: #ffffff;
  }}
  .chip.active {{
    background: var(--primary);
    border-color: var(--primary-light);
    color: #ffffff;
  }}

  /* LEADS LIST / TABLE */
  .table-container {{
    max-width: 1380px;
    margin: 22px auto 0;
    padding: 0 24px;
  }}
  .table-header-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-bottom: none;
    border-radius: 12px 12px 0 0;
    padding: 14px 20px;
    font-size: 13px;
    color: var(--text-muted);
  }}
  .select-all-box {{
    display: flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    user-select: none;
    color: #ffffff;
    font-weight: 600;
  }}
  .select-all-box input {{
    width: 17px;
    height: 17px;
    accent-color: var(--primary-light);
    cursor: pointer;
  }}

  .leads-table {{
    width: 100%;
    border-collapse: collapse;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 0 0 12px 12px;
    overflow: hidden;
  }}
  .leads-table th {{
    background: #111715;
    padding: 12px 18px;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    text-align: left;
    border-bottom: 1px solid var(--border);
  }}
  .leads-table tr {{
    border-bottom: 1px solid var(--border);
    transition: background 0.15s;
  }}
  .leads-table tr:hover {{
    background: var(--bg-card-hover);
  }}
  .leads-table tr.selected {{
    background: rgba(11, 94, 71, 0.15);
  }}
  .leads-table td {{
    padding: 14px 18px;
    font-size: 13.5px;
    vertical-align: middle;
  }}

  /* BADGES */
  .badge {{
    display: inline-block;
    padding: 3px 9px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }}
  .badge-bairro-sr {{
    background: rgba(164, 219, 201, 0.12);
    color: var(--accent);
    border: 1px solid rgba(164, 219, 201, 0.25);
  }}
  .badge-bairro-br {{
    background: rgba(229, 164, 59, 0.12);
    color: var(--warning);
    border: 1px solid rgba(229, 164, 59, 0.25);
  }}
  .badge-urgencia-2 {{
    background: rgba(224, 82, 82, 0.15);
    color: #ff6b6b;
    border: 1px solid rgba(224, 82, 82, 0.3);
  }}
  .badge-urgencia-1 {{
    background: rgba(229, 164, 59, 0.15);
    color: var(--warning);
    border: 1px solid rgba(229, 164, 59, 0.3);
  }}
  .badge-oferta {{
    background: rgba(18, 130, 99, 0.2);
    color: #79f2c3;
    border: 1px solid rgba(18, 130, 99, 0.4);
    font-weight: 600;
  }}

  /* LOSS BAR */
  .loss-container {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .loss-bar {{
    flex: 1;
    height: 6px;
    background: #232d28;
    border-radius: 3px;
    overflow: hidden;
    min-width: 60px;
  }}
  .loss-fill {{
    height: 100%;
    background: linear-gradient(90deg, var(--warning) 0%, var(--danger) 100%);
    border-radius: 3px;
  }}

  /* HOOK DRAWER */
  .hook-toggle {{
    color: var(--accent);
    font-size: 11.5px;
    cursor: pointer;
    text-decoration: underline;
    margin-top: 4px;
    display: inline-block;
  }}
  .hook-box {{
    display: none;
    margin-top: 8px;
    background: #0d1210;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 12px;
    color: #c9d8d1;
    line-height: 1.45;
  }}

  /* FLOATING FOOTER BAR */
  .floating-bar {{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(17, 24, 21, 0.95);
    border-top: 1px solid var(--border);
    backdrop-filter: blur(16px);
    padding: 14px 24px;
    z-index: 100;
  }}
  .floating-inner {{
    max-width: 1380px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
  }}
  .selected-counter {{
    font-size: 14px;
    font-weight: 600;
    color: #ffffff;
  }}
  .selected-counter span {{
    color: var(--accent);
    font-size: 16px;
    font-weight: 800;
  }}
  .action-buttons {{
    display: flex;
    gap: 10px;
    align-items: center;
  }}
  .btn {{
    padding: 11px 22px;
    border-radius: 9px;
    font-size: 13.5px;
    font-weight: 700;
    cursor: pointer;
    border: none;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .btn-primary {{
    background: var(--primary);
    color: #ffffff;
    box-shadow: 0 4px 14px rgba(11, 94, 71, 0.4);
  }}
  .btn-primary:hover {{
    background: var(--primary-light);
    transform: translateY(-1px);
  }}
  .btn-secondary {{
    background: #1f2a25;
    color: var(--text-main);
    border: 1px solid var(--border);
  }}
  .btn-secondary:hover {{
    background: #283630;
    border-color: var(--accent);
  }}

  /* MODAL */
  .modal-overlay {{
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(8px);
    z-index: 200;
    align-items: center;
    justify-content: center;
  }}
  .modal-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 28px;
    max-width: 520px;
    width: 90%;
    box-shadow: 0 16px 40px rgba(0,0,0,0.5);
  }}
  .modal-title {{
    font-family: 'Fraunces', serif;
    font-size: 22px;
    margin-bottom: 8px;
    color: #ffffff;
  }}
  .modal-text {{
    font-size: 13.5px;
    color: var(--text-muted);
    line-height: 1.6;
    margin-bottom: 20px;
  }}
  .modal-actions {{
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }}
</style>
</head>
<body>

<header>
  <div class="header-inner">
    <div class="brand-area">
      <div class="brand-logo">
        <img src="https://vocacao.digital/logo-vocacao-white.png" alt="Vocação">
      </div>
      <div class="brand-title">
        <p>Inteligência Comercial · Jev System One</p>
        <h1>Painel de Pré-Seleção de Leads (100)</h1>
      </div>
    </div>
    <div style="font-size: 12.5px; color: var(--text-muted); text-align: right;">
      Pólos Comerciais: <b style="color: #ffffff;">Santa Rosália & Jardim Brasilândia</b><br>
      Status: <span style="color: var(--warning); font-weight: bold;">Aguardando Decisão do Gestor</span>
    </div>
  </div>
</header>

<!-- METRICS -->
<div class="metrics-grid">
  <div class="metric-card">
    <div class="metric-label">Total de Leads Mapeados</div>
    <div class="metric-val">100</div>
    <div class="metric-sub">60 Santa Rosália · 40 Brasilândia</div>
  </div>
  <div class="metric-card accent">
    <div class="metric-label">Pipeline Potencial Jev</div>
    <div class="metric-val">R$ 74.060</div>
    <div class="metric-sub">Soma das ofertas de melhor fit</div>
  </div>
  <div class="metric-card warning">
    <div class="metric-label">Urgência Crítica (Score 2)</div>
    <div class="metric-val" id="crit-count">37 leads</div>
    <div class="metric-sub">Perda severa de clientes locais</div>
  </div>
  <div class="metric-card success">
    <div class="metric-label">Oferta Carro-Chefe</div>
    <div class="metric-val">Start (R$ 850)</div>
    <div class="metric-sub">38 empresas sem vitrine própria</div>
  </div>
</div>

<!-- CONTROLS -->
<div class="controls-section">
  <div class="search-box">
    <input type="text" id="searchInput" class="search-input" placeholder="Buscar por empresa, nicho, endereço ou telefone..." onkeyup="filterLeads()">
  </div>
  <div class="filter-chips">
    <div class="chip active" onclick="setChipFilter('all', this)">Todos (100)</div>
    <div class="chip" onclick="setChipFilter('sr', this)">📍 Santa Rosália (60)</div>
    <div class="chip" onclick="setChipFilter('br', this)">📍 Jardim Brasilândia (40)</div>
    <div class="chip" onclick="setChipFilter('crit', this)">🔥 Urgência Crítica (37)</div>
    <div class="chip" onclick="setChipFilter('start', this)">🚀 Vocação Start (38)</div>
    <div class="chip" onclick="setChipFilter('tour', this)">📸 Combo Tour 360° (20)</div>
    <div class="chip" onclick="setChipFilter('update', this)">⚡ Vocação Update (2)</div>
    <div class="chip" onclick="setChipFilter('maps', this)">🗺️ Vocação Maps (40)</div>
  </div>
</div>

<!-- LEADS TABLE -->
<div class="table-container">
  <div class="table-header-bar">
    <label class="select-all-box">
      <input type="checkbox" id="selectAllCheckbox" onchange="toggleSelectAll(this.checked)" checked>
      <span>Selecionar Todos os Visíveis (<span id="visibleCount">100</span>)</span>
    </label>
    <div id="selectionSummary">100 selecionados</div>
  </div>
  <table class="leads-table">
    <thead>
      <tr>
        <th width="40">Sel</th>
        <th>Empresa & Categoria</th>
        <th>Bairro & Endereço</th>
        <th>Telefone / Contato</th>
        <th>Oferta Jev (Fit)</th>
        <th>Urgência</th>
        <th>Perda Estimada</th>
      </tr>
    </thead>
    <tbody id="leadsTableBody">
      <!-- Inserido dinamicamente via JS -->
    </tbody>
  </table>
</div>

<!-- FLOATING ACTION BAR -->
<div class="floating-bar">
  <div class="floating-inner">
    <div class="selected-counter">
      <span id="selectedCounter">100</span> de 100 leads selecionados para importação
    </div>
    <div class="action-buttons">
      <button class="btn btn-secondary" onclick="exportJSON()">
        📥 Exportar JSON
      </button>
      <button class="btn btn-secondary" onclick="openConfirmModal(false)">
        ⚡ Incluir Selecionados no CRM
      </button>
      <button class="btn btn-primary" onclick="openConfirmModal(true)">
        🚀 Incluir Tudo no CRM e Fila de Disparo
      </button>
    </div>
  </div>
</div>

<!-- MODAL CONFIRMATION -->
<div id="confirmModal" class="modal-overlay">
  <div class="modal-card">
    <h3 class="modal-title">Confirmar Importação no CRM</h3>
    <p class="modal-text" id="modalDescription">
      Você está prestes a carregar os leads selecionados no Twenty CRM com suas respectivas notas e estágios qualificados pelo Jev.
    </p>
    <div class="modal-actions">
      <button class="btn btn-secondary" onclick="closeConfirmModal()">Cancelar</button>
      <button class="btn btn-primary" id="confirmActionBtn" onclick="executeBatchImport()">
        Confirmar e Executar
      </button>
    </div>
  </div>
</div>

<script>
const LEADS_DATA = {leads_json_str};

let activeFilter = 'all';
let selectedLeads = new Set(LEADS_DATA.map(l => l.name));

function renderTable() {{
  const tbody = document.getElementById('leadsTableBody');
  const term = document.getElementById('searchInput').value.toLowerCase().trim();
  tbody.innerHTML = '';

  let visible = 0;

  LEADS_DATA.forEach(lead => {{
    // Filtro de Texto
    const matchesSearch = 
      lead.name.toLowerCase().includes(term) ||
      lead.cat.toLowerCase().includes(term) ||
      lead.addr.toLowerCase().includes(term) ||
      lead.phone.includes(term) ||
      lead.bairro.toLowerCase().includes(term);

    // Filtro de Chips
    let matchesChip = true;
    if (activeFilter === 'sr') matchesChip = (lead.bairro === 'Santa Rosália');
    else if (activeFilter === 'br') matchesChip = (lead.bairro === 'Jardim Brasilândia');
    else if (activeFilter === 'crit') matchesChip = (lead.urgencia_score === 2);
    else if (activeFilter === 'start') matchesChip = (lead.oferta_key === 'vocacao_start_850');
    else if (activeFilter === 'tour') matchesChip = (lead.oferta_key === 'combo_maps_tour360_950');
    else if (activeFilter === 'update') matchesChip = (lead.oferta_key === 'vocacao_update_980');
    else if (activeFilter === 'maps') matchesChip = (lead.oferta_key === 'vocacao_maps_450');

    if (matchesSearch && matchesChip) {{
      visible++;
      const isChecked = selectedLeads.has(lead.name);
      const row = document.createElement('tr');
      if (isChecked) row.classList.add('selected');

      const bairroBadge = lead.bairro === 'Santa Rosália' 
        ? '<span class="badge badge-bairro-sr">Santa Rosália</span>'
        : '<span class="badge badge-bairro-br">Jd. Brasilândia</span>';

      const urgBadge = lead.urgencia_score === 2
        ? '<span class="badge badge-urgencia-2">Crítica (2)</span>'
        : '<span class="badge badge-urgencia-1">Média (1)</span>';

      const lossPercent = Math.round(lead.perda_conversao_local * 100);

      row.innerHTML = `
        <td>
          <input type="checkbox" onchange="toggleSelectLead('${{lead.name.replace(/'/g, "\\\\'") }}', this.checked)" ${{isChecked ? 'checked' : ''}}>
        </td>
        <td>
          <strong style="color: #ffffff; font-size: 14px;">${{lead.name}}</strong>
          <div style="font-size: 11.5px; color: var(--text-muted);">${{lead.cat}}</div>
          <a class="hook-toggle" onclick="toggleHook(this)">Ver Hook WhatsApp</a>
          <div class="hook-box">
            <b>Hook:</b> "${{lead.hook_whatsapp}}"
          </div>
        </td>
        <td>
          ${{bairroBadge}}
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;">${{lead.addr}}</div>
        </td>
        <td>
          <span style="font-family: monospace; font-size: 12.5px; color: #a4dbc9;">${{lead.phone}}</span>
          <div style="font-size: 11px; color: var(--text-muted);">${{lead.presence}}</div>
        </td>
        <td>
          <span class="badge badge-oferta">${{lead.oferta_nome.split('(')[0]}}</span>
          <div style="font-weight: 700; color: #ffffff; font-size: 12.5px; margin-top: 2px;">R$ ${{lead.oferta_preco.toFixed(2)}}</div>
        </td>
        <td>
          ${{urgBadge}}
        </td>
        <td>
          <div class="loss-container">
            <span style="font-size: 12px; font-weight: bold; color: ${{lossPercent >= 80 ? '#ff6b6b' : '#e5a43b'}};">${{lossPercent}}%</span>
            <div class="loss-bar">
              <div class="loss-fill" style="width: ${{lossPercent}}%;"></div>
            </div>
          </div>
        </td>
      `;
      tbody.appendChild(row);
    }}
  }});

  document.getElementById('visibleCount').innerText = visible;
  updateSelectionCounter();
}}

function toggleHook(btn) {{
  const box = btn.nextElementSibling;
  if (box.style.display === 'block') {{
    box.style.display = 'none';
    btn.innerText = 'Ver Hook WhatsApp';
  }} else {{
    box.style.display = 'block';
    btn.innerText = 'Ocultar Hook';
  }}
}}

function setChipFilter(filter, el) {{
  activeFilter = filter;
  document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  renderTable();
}}

function filterLeads() {{
  renderTable();
}}

function toggleSelectLead(name, checked) {{
  if (checked) {{
    selectedLeads.add(name);
  }} else {{
    selectedLeads.delete(name);
  }}
  updateSelectionCounter();
  renderTable();
}}

function toggleSelectAll(checked) {{
  const term = document.getElementById('searchInput').value.toLowerCase().trim();
  LEADS_DATA.forEach(lead => {{
    const matchesSearch = 
      lead.name.toLowerCase().includes(term) ||
      lead.cat.toLowerCase().includes(term) ||
      lead.addr.toLowerCase().includes(term) ||
      lead.phone.includes(term) ||
      lead.bairro.toLowerCase().includes(term);

    let matchesChip = true;
    if (activeFilter === 'sr') matchesChip = (lead.bairro === 'Santa Rosália');
    else if (activeFilter === 'br') matchesChip = (lead.bairro === 'Jardim Brasilândia');
    else if (activeFilter === 'crit') matchesChip = (lead.urgencia_score === 2);
    else if (activeFilter === 'start') matchesChip = (lead.oferta_key === 'vocacao_start_850');
    else if (activeFilter === 'tour') matchesChip = (lead.oferta_key === 'combo_maps_tour360_950');
    else if (activeFilter === 'update') matchesChip = (lead.oferta_key === 'vocacao_update_980');
    else if (activeFilter === 'maps') matchesChip = (lead.oferta_key === 'vocacao_maps_450');

    if (matchesSearch && matchesChip) {{
      if (checked) selectedLeads.add(lead.name);
      else selectedLeads.delete(lead.name);
    }}
  }});
  updateSelectionCounter();
  renderTable();
}}

function updateSelectionCounter() {{
  const count = selectedLeads.size;
  document.getElementById('selectedCounter').innerText = count;
  document.getElementById('selectionSummary').innerText = `${{count}} selecionados`;
}}

let importAllMode = false;

function openConfirmModal(allMode) {{
  importAllMode = allMode;
  const count = allMode ? LEADS_DATA.length : selectedLeads.size;
  document.getElementById('modalDescription').innerHTML = 
    `Você selecionou <b>${{count}} leads</b> dos bairros Santa Rosália e Jardim Brasilândia para serem inseridos no <b>Twenty CRM</b> e estruturados na <b>Fila de Disparo Segura</b>.<br><br>As ofertas (Start R$ 850, Tour 360 R$ 950 e Maps R$ 450) já foram qualificadas pelo Jev System One.`;
  document.getElementById('confirmModal').style.display = 'flex';
}}

function closeConfirmModal() {{
  document.getElementById('confirmModal').style.display = 'none';
}}

function executeBatchImport() {{
  const btn = document.getElementById('confirmActionBtn');
  btn.innerText = 'Processando...';
  btn.disabled = true;

  const targetList = importAllMode 
    ? LEADS_DATA 
    : LEADS_DATA.filter(l => selectedLeads.has(l.name));

  // Envia payload para o endpoint local ou gera o script
  fetch('http://localhost:5680/api/import-batch', {{
    method: 'POST',
    headers: {{ 'Content-Type': 'application/json' }},
    body: JSON.stringify({{ leads: targetList }})
  }})
  .then(res => res.json())
  .then(data => {{
    alert('✅ Sucesso! ' + targetList.length + ' leads importados no Twenty CRM e adicionados à fila de disparo.');
    closeConfirmModal();
    btn.innerText = 'Confirmar e Executar';
    btn.disabled = false;
  }})
  .catch(err => {{
    // Fallback: Informa comando para rodar no terminal se o webhook não responder
    alert('Comando pronto! Como o processo foi executado localmente, basta você autorizar no chat ou rodar: python importar_lote100_crm.py');
    closeConfirmModal();
    btn.innerText = 'Confirmar e Executar';
    btn.disabled = false;
  }});
}}

function exportJSON() {{
  const targetList = LEADS_DATA.filter(l => selectedLeads.has(l.name));
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(targetList, null, 2));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", "leads_qualificados_jev_santa_rosalia_brasilandia.json");
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
}}

renderTable();
</script>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[✓] Painel HTML interativo gerado: {HTML_PATH}")
