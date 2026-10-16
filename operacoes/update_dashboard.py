import json

def update():
    with open('leads_100_santa_rosalia_brasilandia.json', 'r', encoding='utf-8') as f:
        leads = json.load(f)

    with open('Painel-PreSelecao-100Leads-SantaRosalia-Brasilandia.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Substitui o JSON
    start_marker = 'const LEADS_DATA = '
    end_marker = ';\nlet selectedLeads = new Set('
    p1 = html.find(start_marker)
    p2 = html.find(end_marker, p1)

    if p1 != -1 and p2 != -1:
        new_json_str = json.dumps(leads, ensure_ascii=False)
        html = html[:p1 + len(start_marker)] + new_json_str + html[p2:]
        print('JSON substituído com sucesso.')

    # 2. Cabeçalho da coluna
    html = html.replace('<th>Perda Estimada</th>', '<th>Interesse Vendedor Vocação</th>')

    # 3. Métricas do topo
    old_metrics = '''    <div class="metric-card accent">
      <div class="metric-label">Urgência Crítica Jev</div>
      <div class="metric-val">48</div>
      <div class="metric-sub">Leads com perda local > 80%</div>
    </div>
    <div class="metric-card warning">
      <div class="metric-label">Perda Média no Bairro</div>
      <div class="metric-val">78%</div>
      <div class="metric-sub">Tráfego orgânico não captado</div>
    </div>'''

    new_metrics = '''    <div class="metric-card accent">
      <div class="metric-label">⭐ Leads Ouro (WhatsApp Direto)</div>
      <div class="metric-val">30</div>
      <div class="metric-sub">Alta comissão + celular no Maps</div>
    </div>
    <div class="metric-card success">
      <div class="metric-label">Interesse Médio Vendedor</div>
      <div class="metric-val">77%</div>
      <div class="metric-sub">Score comercial e fit Vocação</div>
    </div>'''

    html = html.replace(old_metrics, new_metrics)

    # 4. Chips de filtro
    old_chips = '''    <div class="chip" onclick="setChipFilter('tour', this)">Tour 360° (32)</div>
    <div class="chip" onclick="setChipFilter('update', this)">Update Mobile (4)</div>
    <div class="chip" onclick="setChipFilter('maps', this)">Maps Blindagem (18)</div>'''

    new_chips = '''    <div class="chip" style="border-color: #e5a43b; color: #ffd27a;" onclick="setChipFilter('ouro', this)">⭐ Ouro / WhatsApp Direto (30)</div>
    <div class="chip" onclick="setChipFilter('tour', this)">Tour 360° (32)</div>
    <div class="chip" onclick="setChipFilter('update', this)">Update Mobile (4)</div>
    <div class="chip" onclick="setChipFilter('maps', this)">Maps Blindagem (18)</div>'''

    html = html.replace(old_chips, new_chips)

    # 5. Renderização da célula com barra de interesse do vendedor
    old_render_loss = '''      const lossPercent = Math.round(lead.perda_conversao_local * 100);

      row.innerHTML = `
        <td>
          <input type="checkbox" onchange="toggleSelectLead('${lead.name.replace(/'/g, "\\'") }', this.checked)" ${isChecked ? 'checked' : ''}>
        </td>
        <td>
          <strong style="color: #ffffff; font-size: 14px;">${lead.name}</strong>
          <div style="font-size: 11.5px; color: var(--text-muted);">${lead.cat}</div>
          <a class="hook-toggle" onclick="toggleHook(this)">Ver Hook WhatsApp</a>
          <div class="hook-box">
            <b>Hook:</b> "${lead.hook_whatsapp}"
          </div>
        </td>
        <td>
          ${bairroBadge}
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;">${lead.addr}</div>
        </td>
        <td>
          <span style="font-family: monospace; font-size: 12.5px; color: #a4dbc9;">${lead.phone}</span>
          <div style="font-size: 11px; color: var(--text-muted);">${lead.presence}</div>
        </td>
        <td>
          <span class="badge badge-oferta">${lead.oferta_nome.split('(')[0]}</span>
          <div style="font-weight: 700; color: #ffffff; font-size: 12.5px; margin-top: 2px;">R$ ${lead.oferta_preco.toFixed(2)}</div>
        </td>
        <td>
          ${urgBadge}
        </td>
        <td>
          <div class="loss-container">
            <span style="font-size: 12px; font-weight: bold; color: ${lossPercent >= 80 ? '#ff6b6b' : '#e5a43b'};">${lossPercent}%</span>
            <div class="loss-bar">
              <div class="loss-fill" style="width: ${lossPercent}%;"></div>
            </div>
          </div>
        </td>
      `;'''

    new_render_loss = '''      const scoreVendedor = lead.interesse_vendedor || 75;
      const scoreColor = scoreVendedor >= 90 ? '#48bb78' : (scoreVendedor >= 75 ? '#38b2ac' : '#a0aec0');
      const scoreTag = lead.interesse_tag || '';

      row.innerHTML = `
        <td>
          <input type="checkbox" onchange="toggleSelectLead('${lead.name.replace(/'/g, "\\'") }', this.checked)" ${isChecked ? 'checked' : ''}>
        </td>
        <td>
          <strong style="color: #ffffff; font-size: 14px;">${lead.name}</strong>
          <div style="font-size: 11.5px; color: var(--text-muted);">${lead.cat}</div>
          <a class="hook-toggle" onclick="toggleHook(this)">Ver Hook WhatsApp</a>
          <div class="hook-box">
            <b>Hook de Abordagem:</b> "${lead.hook_whatsapp}"
          </div>
        </td>
        <td>
          ${bairroBadge}
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;">${lead.addr}</div>
        </td>
        <td>
          <span style="font-family: monospace; font-size: 12.5px; color: ${lead.phone.includes('9') ? '#79f2c3' : '#cbd5e0'};">${lead.phone}</span>
          <div style="font-size: 11px; color: var(--text-muted);">${lead.presence}</div>
        </td>
        <td>
          <span class="badge badge-oferta">${lead.oferta_nome.split('(')[0]}</span>
          <div style="font-weight: 700; color: #ffffff; font-size: 12.5px; margin-top: 2px;">R$ ${lead.oferta_preco.toFixed(2)}</div>
        </td>
        <td>
          ${urgBadge}
        </td>
        <td>
          <div class="loss-container">
            <span style="font-size: 13px; font-weight: 800; color: ${scoreColor};">${scoreVendedor}%</span>
            <div class="loss-bar">
              <div class="loss-fill" style="width: ${scoreVendedor}%; background: linear-gradient(90deg, #128263 0%, ${scoreColor} 100%);"></div>
            </div>
          </div>
          <div style="font-size: 10px; color: var(--text-muted); margin-top: 3px;">${scoreTag}</div>
        </td>
      `;'''

    html = html.replace(old_render_loss, new_render_loss)

    # 6. Atualiza lógica de filtros do chip
    old_chip_logic = '''    if (activeFilter === 'sr') matchesChip = (lead.bairro === 'Santa Rosália');
    else if (activeFilter === 'br') matchesChip = (lead.bairro === 'Jardim Brasilândia');
    else if (activeFilter === 'crit') matchesChip = (lead.urgencia_score === 2);'''

    new_chip_logic = '''    if (activeFilter === 'sr') matchesChip = (lead.bairro === 'Santa Rosália');
    else if (activeFilter === 'br') matchesChip = (lead.bairro === 'Jardim Brasilândia');
    else if (activeFilter === 'crit') matchesChip = (lead.urgencia_score === 2);
    else if (activeFilter === 'ouro') matchesChip = ((lead.interesse_vendedor || 0) >= 90);'''

    html = html.replace(old_chip_logic, new_chip_logic)

    with open('Painel-PreSelecao-100Leads-SantaRosalia-Brasilandia.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print('Dashboard HTML atualizado com sucesso!')

if __name__ == '__main__':
    update()
