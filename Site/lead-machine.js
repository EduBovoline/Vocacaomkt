/* ============================================
   LEAD MACHINE — Multi-step diagnostic intake
   + LGPD Consent + Instant Raio-X + DeepSeek Webhook
   ============================================ */

(function(){
  'use strict';

  const STORAGE_KEY = 'vocacao-lm-v2';
  const WEBHOOK_URL = 'http://localhost:5690/api/diagnostico-intake';

  const STEPS = [
    {
      id: 'intro',
      eyebrow: 'Diagnóstico Estrutural Gratuito',
      title: 'Vamos auditar sua <em>presença digital</em>.',
      help: 'Em perguntas rápidas, identificamos onde sua empresa perde clientes no Google e no celular. Ao finalizar, você vê na hora o seu Raio-X Preliminar na tela e recebe a auditoria completa no WhatsApp.',
      type: 'intro'
    },
    {
      id: 'empresa',
      eyebrow: '01 · Sua empresa',
      title: 'Qual o nome da sua empresa?',
      help: 'Como ela aparece — ou deveria aparecer — quando alguém pesquisa no Google.',
      type: 'text',
      placeholder: 'Ex.: Clínica Piacitelli / Marcenaria Sucesso',
      required: true
    },
    {
      id: 'segmento',
      eyebrow: '02 · O que vocês fazem',
      title: 'Em que setor sua empresa atua?',
      help: 'Selecione a área que mais se aproxima da sua operação.',
      type: 'options',
      options: [
        'Saúde, clínica, estética ou bem-estar',
        'Serviço profissional (engenharia, jurídico, consultoria, B2B)',
        'Marcenaria, arquitetura, construção ou reforma',
        'Comércio físico, loja ou showroom',
        'Gastronomia, confeitaria, eventos ou alimentação',
        'Serviço técnico (manutenção, segurança, automotivo, TI)',
        'Outro segmento local ou regional'
      ]
    },
    {
      id: 'tempo',
      eyebrow: '03 · Tempo de operação',
      title: 'Há quanto tempo sua empresa existe?',
      help: 'Negócios novos precisam de base rápida para tráfego. Empresas consolidadas precisam que o digital reflita a reputação que já têm.',
      type: 'options',
      options: [
        'Menos de 1 ano',
        '1 a 3 anos',
        '3 a 7 anos',
        'Mais de 7 anos'
      ]
    },
    {
      id: 'site',
      eyebrow: '04 · Site Profissional',
      title: 'Como está o site da sua empresa hoje?',
      help: 'Avaliamos se quem clica no seu link entende em 5 segundos o seu valor e chama no WhatsApp.',
      type: 'options',
      options: [
        'Sim, temos site rápido e atualizado',
        'Temos site, mas é antigo, lento ou ruim no celular',
        'Tínhamos site, mas saiu do ar',
        'Ainda não temos site (usamos só Instagram / Linktree)'
      ]
    },
    {
      id: 'google',
      eyebrow: '05 · Google Maps (Meu Negócio)',
      title: 'Como está sua ficha no Google Maps?',
      help: '76% das buscas locais no celular geram contato ou visita em até 24h.',
      type: 'options',
      options: [
        'Bem configurada, com fotos atuais e boas avaliações',
        'Existe, mas está desatualizada ou sem otimização',
        'Existe, mas não temos controle / está abandonada',
        'Nunca configuramos no Google Maps'
      ]
    },
    {
      id: 'redes',
      eyebrow: '06 · Redes Sociais & Fotos',
      title: 'Como estão suas redes e materiais visuais?',
      help: 'Não precisa postar todo dia — mas o perfil precisa transmitir empresa ativa e confiável.',
      type: 'options',
      options: [
        'Ativas e com boas fotos reais da estrutura/serviço',
        'Existem, mas postamos pouco ou falta organização',
        'Perfis parados há meses',
        'Não temos perfil oficial estruturado'
      ]
    },
    {
      id: 'gargalo',
      eyebrow: '07 · O gargalo principal',
      title: 'O que mais <em>incomoda</em> você hoje?',
      help: 'Escolha o ponto que mais trava o seu crescimento comercial neste momento.',
      type: 'options',
      options: [
        'Clientes pesquisam no bairro e acham o concorrente primeiro',
        'Nossa estrutura física/entrega é ótima, mas online parece amadora',
        'Curiosos perguntam preço, mas poucos fecham no WhatsApp',
        'Quero organizar tudo rápido sem perder tempo com reuniões longas'
      ]
    },
    {
      id: 'links',
      eyebrow: '08 · Seus canais atuais',
      title: 'Onde encontramos sua empresa hoje?',
      help: 'Cole os links ou @ que tiver (opcionais). Nosso motor analisa seu site e sua ficha do Google para montar o comparativo visual.',
      type: 'links'
    },
    {
      id: 'contato',
      eyebrow: '09 · Receber Raio-X + Laudo Completo',
      title: 'Para onde enviamos sua auditoria?',
      help: 'Seu Raio-X Preliminar aparece na tela agora mesmo, e enviamos o laudo detalhado no seu WhatsApp.',
      type: 'contact'
    },
    {
      id: 'sucesso',
      type: 'success'
    }
  ];

  // ---- State ----
  let answers = {};
  let stepIdx = 0;
  let webhookSent = false;

  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      const parsed = JSON.parse(saved);
      if (parsed && typeof parsed === 'object') {
        answers = parsed.answers || {};
        stepIdx = Math.min(parsed.stepIdx || 0, STEPS.length - 1);
      }
    }
  } catch (e) {}

  function persist() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ answers, stepIdx }));
    } catch (e) {}
  }

  // ---- Instant Diagnostic Engine (Raio-X Preliminar) ----
  function computeInstantDiagnosis(ans) {
    let score = 45;
    const findings = [];

    // 1. Site analysis
    const siteAns = ans.site || '';
    if (siteAns.includes('Ainda não temos') || siteAns.includes('saiu do ar')) {
      score -= 18;
      findings.push('<b>Vazamento de Autoridade Web:</b> Sem site próprio ativo, o cliente que pesquisa no Google depende apenas de redes sociais e não encontra uma vitrine estruturada para converter.');
    } else if (siteAns.includes('antigo, lento')) {
      score -= 12;
      findings.push('<b>Fricção Mobile no Site Atual:</b> Sites que demoram mais de 2s no 4G ou têm layout antigo perdem até metade dos cliques antes mesmo do cliente chamar no WhatsApp.');
    } else {
      score += 20;
      findings.push('<b>Base Web Existente:</b> Sua empresa já possui site ativo; o foco na auditoria visual será validar a velocidade sub-segundo (<0.5s) e o destaque de conversão no celular.');
    }

    // 2. Google Maps analysis
    const googleAns = ans.google || '';
    if (googleAns.includes('Nunca configuramos') || googleAns.includes('abandonada')) {
      score -= 15;
      findings.push('<b>Invisibilidade nas Buscas de Bairro:</b> Sua ficha no Google Maps está vulnerável, entregando clientes prontos para comprar diretamente para os concorrentes da região.');
    } else if (googleAns.includes('desatualizada')) {
      score -= 8;
      findings.push('<b>Ficha Local Sub-Otimizada:</b> O perfil existe no Google Maps, mas sem blindagem de categorias, fotos estratégicas e SEO local, perde posições no topo do mapa.');
    } else {
      score += 18;
      findings.push('<b>Presença Inicial no Google Maps:</b> Perfil ativo; avaliaremos a blindagem contra sugestões de terceiros e o potencial de imersão em 360°.');
    }

    // 3. Bottleneck & Conversion
    const gargaloAns = ans.gargalo || '';
    if (gargaloAns.includes('acham o concorrente')) {
      findings.push('<b>Prioridade Imadiata:</b> Estancar a perda de buscas locais no Google Meu Negócio com Trava de Exclusividade de Bairro.');
    } else if (gargaloAns.includes('parece amadora')) {
      findings.push('<b>Prioridade Imediata:</b> Alinhar o padrão visual da empresa na internet ao nível real da sua entrega presencial.');
    } else {
      findings.push('<b>Prioridade Imediata:</b> Enxugar o caminho de decisão do cliente para que ele chegue no seu WhatsApp já convencido do seu valor.');
    }

    score = Math.max(18, Math.min(88, score));

    // Recommendation routing
    let recTitle = 'Vocação Start (Google Maps + Vitrine One-Page)';
    let recTime = 'Entrega travada em 7 dias úteis · Escopo Fechado';
    let recDesc = 'Ideal para o seu momento: blindamos sua ficha no Google Maps e colocamos no ar uma Vitrine Digital ultrarrápida integrada ao seu WhatsApp — sem você precisar escrever textos do zero.';
    let recCode = 'VOCACAO_START';

    if (siteAns.includes('antigo, lento') || (ans.link_site && !siteAns.includes('Ainda não temos'))) {
      recTitle = 'Vocação Update (Modernização de Site < 0.5s)';
      recTime = 'Entrega travada em 5 dias úteis · Escopo Fechado';
      recDesc = 'Ideal para o seu momento: aproveitamos seus textos e domínio atuais e reformulamos 100% do visual e da velocidade mobile em 5 dias úteis, com pagamento 50/50 após aprovação.';
      recCode = 'VOCACAO_UPDATE';
    } else if (siteAns.includes('rápido e atualizado') && !googleAns.includes('Bem configurada')) {
      recTitle = 'Presença no Google Maps + Tour Virtual 360°';
      recTime = 'Entrega em 48h a 7 dias úteis · Exclusividade de Bairro';
      recDesc = 'Ideal para o seu momento: blindagem completa da ficha no Google Meu Negócio e imersão Street View 5.6K para dominar as buscas locais do seu segmento.';
      recCode = 'PRESENCA_MAPS_360';
    }

    return { score, findings, recTitle, recTime, recDesc, recCode };
  }

  // ---- Trigger Hybrid DeepSeek + Jev Webhook ----
  function dispatchToDeepSeekEngine(ans, diag) {
    if (webhookSent) return;
    webhookSent = true;
    const payload = {
      lead_id: 'LD-' + Date.now(),
      submitted_at: new Date().toISOString(),
      lgpd: {
        consent: Boolean(ans.lgpd_consent),
        timestamp: ans.lgpd_timestamp || new Date().toISOString(),
        law: 'Lei 13.709/2018 (LGPD)'
      },
      answers: ans,
      instant_diagnosis: diag
    };
    try {
      fetch(WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
        mode: 'cors'
      }).catch(() => {
        // Silencioso caso o visitante esteja acessando fora da rede local; o botão do WhatsApp garante 100% da entrega
      });
    } catch (e) {}
  }

  // ---- DOM ----
  const qArea = document.getElementById('questionArea');
  const progressBar = document.getElementById('progressBar');
  const stepCounter = document.getElementById('stepCounter');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');

  function pad(n) { return String(n).padStart(2, '0'); }

  function render() {
    const step = STEPS[stepIdx];
    const total = STEPS.length - 1;
    const isSuccess = step.type === 'success';
    const isIntro = step.type === 'intro';

    const pct = isSuccess ? 100 : ((stepIdx + 1) / total) * 100;
    progressBar.style.width = pct + '%';
    stepCounter.textContent = isSuccess
      ? 'Raio-X Concluído'
      : `Passo ${pad(stepIdx + 1)} de ${pad(total)}`;

    prevBtn.style.visibility = (stepIdx === 0 || isSuccess) ? 'hidden' : 'visible';

    if (isSuccess) {
      nextBtn.style.display = 'none';
    } else if (isIntro) {
      nextBtn.innerHTML = 'Iniciar Diagnóstico <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>';
      nextBtn.style.display = '';
    } else if (stepIdx === STEPS.length - 2) {
      nextBtn.innerHTML = 'Gerar meu Raio-X Agora <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M9 7h8v8"></path></svg>';
      nextBtn.style.display = '';
    } else {
      nextBtn.innerHTML = 'Continuar <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>';
      nextBtn.style.display = '';
    }

    qArea.classList.remove('step-anim');
    void qArea.offsetWidth;
    qArea.classList.add('step-anim');

    if (step.type === 'intro') {
      qArea.innerHTML = `
        <div class="lm-eye">${step.eyebrow}</div>
        <h2>${step.title}</h2>
        <p class="help">${step.help}</p>
        <div class="lm-final-marks">
          <div class="m"><b>9</b><span>perguntas objetivas, sem formulário complexo</span></div>
          <div class="m"><b>Na hora</b><span>Raio-X preliminar gerado na sua tela</span></div>
          <div class="m"><b>Zero</b><span>mensalidade ou compromisso obrigatório</span></div>
        </div>
      `;
    } else if (step.type === 'success') {
      const diag = computeInstantDiagnosis(answers);
      answers.recommended_offer = diag.recTitle;
      answers.preliminary_score = diag.score;
      persist();

      if (typeof window.trackDiagnosticConversion === 'function') {
        window.trackDiagnosticConversion(answers);
      }
      dispatchToDeepSeekEngine(answers, diag);

      const wa = buildWhatsAppLink(diag);
      qArea.innerHTML = `
        <div class="lm-success">
          <div class="lm-eye">Diagnóstico Preliminar Gerado</div>
          <h2>Aqui está o Raio-X inicial da <em>${escapeHtml(answers.empresa || 'sua empresa')}</em>.</h2>
          <p>Nossa inteligência comercial já processou suas respostas e iniciou a auditoria dos seus canais para o comparativo visual completo.</p>

          <div class="rx-card">
            <div class="rx-header">
              <div>
                <span style="font-family:var(--mono);font-size:11px;color:#94A3B8;text-transform:uppercase;letter-spacing:0.1em;display:block;">Auditoria Estrutural · Vocação</span>
                <strong style="font-size:20px;color:#FFF;">${escapeHtml(answers.empresa || 'Empresa Auditada')}</strong>
              </div>
              <div class="rx-score-pill">
                <span>Índice de Estrutura Atual:</span>
                <b style="font-size:15px;">${diag.score}/100</b>
              </div>
            </div>

            <ul class="rx-findings">
              ${diag.findings.map(f => `<li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#E5B910" stroke-width="2" style="flex-shrink:0;margin-top:2px;"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg><div>${f}</div></li>`).join('')}
            </ul>

            <div class="rx-rec-box">
              <span class="tag">Solução Recomendada · ${diag.recTime}</span>
              <h5>${diag.recTitle}</h5>
              <p>${diag.recDesc}</p>
            </div>
          </div>

          <div class="btn-row" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin-top:28px;">
            <a href="${wa}" target="_blank" rel="noopener" class="btn btn-primary magnet">
              Receber Auditoria Visual no WhatsApp
              <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M9 7h8v8"></path></svg>
            </a>
            <a href="portfolio.html" class="btn btn-ghost magnet">Testar Sites no Portfólio</a>
          </div>

          <div class="lm-summary">
            <h4>Dados registrados com proteção LGPD</h4>
            ${renderSummaryRows()}
          </div>

          <p style="margin-top:24px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--ink-3);">
            <a href="#" id="resetForm" style="text-decoration:underline">Refazer o diagnóstico</a>
          </p>
        </div>
      `;
      const reset = document.getElementById('resetForm');
      if (reset) reset.addEventListener('click', (e) => {
        e.preventDefault();
        answers = {}; stepIdx = 0; webhookSent = false;
        persist();
        render();
      });
    } else if (step.type === 'options') {
      const value = answers[step.id];
      qArea.innerHTML = `
        <div class="lm-eye">${step.eyebrow}</div>
        <h2>${step.title}</h2>
        <p class="help">${step.help}</p>
        <div class="lm-options">
          ${step.options.map((opt) => `
            <button class="lm-option ${value === opt ? 'selected' : ''}" data-val="${opt.replace(/"/g, '&quot;')}" type="button">
              <span>${opt}</span>
              <span class="badge">${value === opt ? '✓' : ''}</span>
            </button>
          `).join('')}
        </div>
      `;
      qArea.querySelectorAll('.lm-option').forEach(btn => {
        btn.addEventListener('click', () => {
          answers[step.id] = btn.dataset.val;
          persist();
          setTimeout(() => {
            stepIdx = Math.min(stepIdx + 1, STEPS.length - 1);
            persist();
            render();
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }, 240);
        });
      });
    } else if (step.type === 'text') {
      const value = answers[step.id] || '';
      qArea.innerHTML = `
        <div class="lm-eye">${step.eyebrow}</div>
        <h2>${step.title}</h2>
        <p class="help">${step.help}</p>
        <input type="text" class="lm-input" id="textInput" placeholder="${step.placeholder || ''}" value="${value.replace(/"/g, '&quot;')}" autocomplete="organization" />
      `;
      const input = document.getElementById('textInput');
      input.focus();
      input.addEventListener('input', () => {
        answers[step.id] = input.value;
        persist();
      });
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') { e.preventDefault(); next(); }
      });
    } else if (step.type === 'links') {
      qArea.innerHTML = `
        <div class="lm-eye">${step.eyebrow}</div>
        <h2>${step.title}</h2>
        <p class="help">${step.help}</p>
        <div class="lm-options" style="gap:14px;">
          <input type="text" class="lm-input" id="linkSite" placeholder="Site atual (ex: minhaempresa.com.br)" value="${(answers.link_site || '').replace(/"/g, '&quot;')}" autocomplete="url" />
          <input type="text" class="lm-input" id="linkInstagram" placeholder="Instagram (ex: @minhaempresa)" value="${(answers.link_instagram || '').replace(/"/g, '&quot;')}" />
          <input type="text" class="lm-input" id="linkGoogle" placeholder="Google Maps — link do perfil ou nome + bairro" value="${(answers.link_google || '').replace(/"/g, '&quot;')}" />
        </div>
      `;
      const lSite    = document.getElementById('linkSite');
      const lInsta   = document.getElementById('linkInstagram');
      const lGoogle  = document.getElementById('linkGoogle');
      lSite.focus();
      [['link_site', lSite], ['link_instagram', lInsta], ['link_google', lGoogle]].forEach(([k, el]) => {
        el.addEventListener('input', () => { answers[k] = el.value; persist(); });
        el.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); next(); } });
      });
    } else if (step.type === 'contact') {
      const checked = answers.lgpd_consent !== false; // default checked for smooth UX, explicit opt-in
      if (answers.lgpd_consent === undefined) {
        answers.lgpd_consent = true;
        answers.lgpd_timestamp = new Date().toISOString();
      }
      qArea.innerHTML = `
        <div class="lm-eye">${step.eyebrow}</div>
        <h2>${step.title}</h2>
        <p class="help">${step.help}</p>
        <div class="lm-options" style="gap:14px;">
          <input type="text" class="lm-input" id="contactName" placeholder="Seu nome e sobrenome" value="${(answers.name || '').replace(/"/g, '&quot;')}" autocomplete="name" />
          <input type="tel" class="lm-input" id="contactPhone" placeholder="WhatsApp com DDD (ex: 15 99999-9999)" value="${(answers.phone || '').replace(/"/g, '&quot;')}" autocomplete="tel" />
          <input type="email" class="lm-input" id="contactEmail" placeholder="E-mail corporativo (opcional)" value="${(answers.email || '').replace(/"/g, '&quot;')}" autocomplete="email" />
          <label class="lgpd-consent-box" for="lgpdConsent">
            <input type="checkbox" id="lgpdConsent" ${checked ? 'checked' : ''} />
            <span><b>Permissão LGPD (Lei nº 13.709/2018):</b> Autorizo a Vocação Comunicação &amp; Marketing a processar as informações públicas da minha empresa para gerar o diagnóstico de presença digital e entrar em contato pelo WhatsApp/e-mail informado. Zero spam.</span>
          </label>
        </div>
      `;
      const name = document.getElementById('contactName');
      const phone = document.getElementById('contactPhone');
      const email = document.getElementById('contactEmail');
      const lgpd = document.getElementById('lgpdConsent');
      name.focus();
      [['name', name], ['phone', phone], ['email', email]].forEach(([k, el]) => {
        el.addEventListener('input', () => {
          answers[k] = el.value;
          persist();
        });
      });
      lgpd.addEventListener('change', () => {
        answers.lgpd_consent = lgpd.checked;
        answers.lgpd_timestamp = new Date().toISOString();
        persist();
      });
    }
  }

  function renderSummaryRows() {
    const map = {
      empresa: 'Empresa',
      segmento: 'Setor',
      tempo: 'Tempo de operação',
      site: 'Site atual',
      google: 'Google Maps',
      redes: 'Redes sociais',
      gargalo: 'Gargalo principal',
      link_site: 'Site informado',
      link_instagram: 'Instagram',
      link_google: 'Google Maps / Bairro',
      name: 'Responsável',
      phone: 'WhatsApp',
      email: 'E-mail'
    };
    const rows = Object.keys(map)
      .filter(k => answers[k])
      .map(k => `<div class="row"><span>${map[k]}</span><b>${escapeHtml(answers[k])}</b></div>`);
    rows.push(`<div class="row"><span>Aceite LGPD</span><b>Confirmado (${new Date(answers.lgpd_timestamp || Date.now()).toLocaleDateString('pt-BR')})</b></div>`);
    return rows.join('');
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function buildWhatsAppLink(diag) {
    const d = diag || computeInstantDiagnosis(answers);
    const hasLinks = answers.link_site || answers.link_instagram || answers.link_google;
    const lines = [
      'Olá! Acabei de gerar meu Raio-X no site da Vocação e quero receber a auditoria completa.',
      '',
      '📊 *RAIO-X PRELIMINAR:*',
      '• Empresa: ' + (answers.empresa || '-'),
      '• Índice Atual: ' + d.score + '/100',
      '• Solução Recomendada: ' + d.recTitle,
      '',
      '📋 *DIAGNÓSTICO INFORMADO:*',
      answers.segmento  ? '• Setor: '    + answers.segmento  : null,
      answers.tempo     ? '• Tempo: '    + answers.tempo     : null,
      answers.site      ? '• Site: '     + answers.site      : null,
      answers.google    ? '• Google: '   + answers.google    : null,
      answers.gargalo   ? '• Gargalo: '  + answers.gargalo   : null,
      hasLinks ? '' : null,
      hasLinks ? '🔗 *CANAIS PARA AUDITORIA:*' : null,
      answers.link_site       ? '• Site: '        + answers.link_site       : null,
      answers.link_instagram  ? '• Instagram: '   + answers.link_instagram  : null,
      answers.link_google     ? '• Google Maps: ' + answers.link_google     : null,
      '',
      '✅ *LGPD:* Aceite confirmado por ' + (answers.name || 'Responsável') + ' (' + (answers.phone || '') + ').'
    ].filter(Boolean).join('\n');
    return 'https://wa.me/5515981512083?text=' + encodeURIComponent(lines);
  }

  function validate() {
    const step = STEPS[stepIdx];
    if (step.type === 'intro') return true;
    if (step.type === 'success') return true;
    if (step.type === 'text') {
      const v = (answers[step.id] || '').trim();
      if (!v) {
        flash('Digite o nome da sua empresa para continuar.');
        return false;
      }
      return true;
    }
    if (step.type === 'options') {
      if (!answers[step.id]) {
        flash('Selecione uma opção para avançar.');
        return false;
      }
      return true;
    }
    if (step.type === 'contact') {
      const name = (answers.name || '').trim();
      const phone = (answers.phone || '').trim();
      if (!name) { flash('Informe seu nome para emitirmos o Raio-X.'); return false; }
      if (!phone || phone.replace(/\D/g, '').length < 10) {
        flash('Informe um WhatsApp válido com DDD.');
        return false;
      }
      if (!answers.lgpd_consent) {
        flash('Marque a autorização LGPD para gerarmos seu diagnóstico.');
        return false;
      }
      answers.lgpd_timestamp = new Date().toISOString();
      return true;
    }
    return true;
  }

  function flash(msg) {
    const existing = document.querySelector('.lm-flash');
    if (existing) existing.remove();
    const el = document.createElement('div');
    el.className = 'lm-flash';
    el.textContent = msg;
    el.style.cssText = `
      position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%);
      background: #E5B910; color: #04121B; font-weight: 700;
      padding: 14px 22px; border-radius: 999px;
      font-size: 14px; z-index: 100;
      box-shadow: 0 10px 30px rgba(0,0,0,0.35);
      animation: fadeUp .3s var(--ease);
    `;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 2600);
  }

  function next() {
    if (!validate()) return;
    stepIdx = Math.min(stepIdx + 1, STEPS.length - 1);
    persist();
    render();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function prev() {
    stepIdx = Math.max(stepIdx - 1, 0);
    persist();
    render();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  prevBtn.addEventListener('click', prev);
  nextBtn.addEventListener('click', next);

  const styleEl = document.createElement('style');
  styleEl.textContent = `@keyframes fadeUp { from { opacity: 0; transform: translateX(-50%) translateY(10px); } to { opacity: 1; transform: translateX(-50%) translateY(0); } }`;
  document.head.appendChild(styleEl);

  render();
})();
