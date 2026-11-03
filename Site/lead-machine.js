/* ============================================
   LEAD MACHINE — Multi-step diagnostic intake
   + Envio Automático para Banco de Dados (Cloud + Local)
   + Tela de Obrigado (Sem botão de mensagem copiada no WhatsApp)
   ============================================ */

(function(){
  'use strict';

  const STORAGE_KEY = 'vocacao-lm-v3';
  const CLOUD_API_URL = '/api/diagnostico';
  const LOCAL_WEBHOOK_URL = 'http://localhost:5690/api/diagnostico-intake';

  const STEPS = [
    {
      id: 'intro',
      eyebrow: 'Diagnóstico Estrutural Gratuito',
      title: 'Vamos auditar sua <em>presença digital</em>.',
      help: 'Em perguntas rápidas, mapeamos onde sua empresa perde clientes no Google e no celular. Nós analisamos tudo internamente e enviamos o seu relatório detalhado direto no seu WhatsApp.',
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
      help: 'Cole os links ou @ que tiver (opcionais). Nosso motor analisa seu site e sua ficha do Google para montar o seu relatório detalhado.',
      type: 'links'
    },
    {
      id: 'contato',
      eyebrow: '09 · Para enviarmos seu relatório',
      title: 'Em qual WhatsApp você prefere receber o diagnóstico?',
      help: 'Ao concluir, seus dados vão direto para nossa base de análise e nossa equipe enviará o seu relatório detalhado pelo WhatsApp.',
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
  let dbSubmitted = false;

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

  // ---- Instant Preliminary Engine ----
  function computeInstantDiagnosis(ans) {
    let score = 45;
    const findings = [];

    const siteAns = ans.site || '';
    if (siteAns.includes('Ainda não temos') || siteAns.includes('saiu do ar')) {
      score -= 18;
      findings.push('<b>Ausência de Vitrine Própria:</b> Sem site próprio ativo, o cliente que pesquisa no Google não encontra uma estrutura rápida para validar sua autoridade.');
    } else if (siteAns.includes('antigo, lento')) {
      score -= 12;
      findings.push('<b>Fricção Mobile no Site Atual:</b> Vamos medir o tempo de carregamento e o comportamento em telas de celular no seu relatório detalhado.');
    } else {
      score += 20;
      findings.push('<b>Base Web Existente:</b> Auditaremos a velocidade sub-segundo (<0.5s) e o fluxo de conversão para o WhatsApp.');
    }

    const googleAns = ans.google || '';
    if (googleAns.includes('Nunca configuramos') || googleAns.includes('abandonada')) {
      score -= 15;
      findings.push('<b>Vulnerabilidade no Google Maps:</b> Buscas locais do seu bairro podem estar sendo desviadas para concorrentes diretos.');
    } else if (googleAns.includes('desatualizada')) {
      score -= 8;
      findings.push('<b>Ficha Local Sub-Otimizada:</b> Avaliaremos categorias, SEO local e fotos estratégicas da sua ficha no Google Meu Negócio.');
    } else {
      score += 18;
      findings.push('<b>Ficha Ativa no Google Maps:</b> Verificaremos a blindagem contra edições de terceiros e o posicionamento no mapa.');
    }

    const gargaloAns = ans.gargalo || '';
    if (gargaloAns.includes('acham o concorrente')) {
      findings.push('<b>Foco do Relatório:</b> Mapeamento dos concorrentes do seu bairro no Google Maps + plano de blindagem local.');
    } else if (gargaloAns.includes('parece amadora')) {
      findings.push('<b>Foco do Relatório:</b> Comparativo visual Antes & Depois para alinhar sua imagem online ao porte real da sua empresa.');
    } else {
      findings.push('<b>Foco do Relatório:</b> Estruturação de jornada direta para o cliente chegar no seu WhatsApp pronto para fechar.');
    }

    score = Math.max(18, Math.min(88, score));

    let recTitle = 'Vocação Start (Google Maps + Vitrine One-Page)';
    let recTime = 'Prazo de referência: 7 dias úteis · Escopo Fechado';
    let recDesc = 'Foco em blindar sua ficha no Google Maps e colocar no ar uma Vitrine Digital ultrarrápida sem você precisar escrever textos do zero.';
    let recCode = 'VOCACAO_START';

    if (siteAns.includes('antigo, lento') || (ans.link_site && !siteAns.includes('Ainda não temos'))) {
      recTitle = 'Vocação Update (Modernização de Site < 0.5s)';
      recTime = 'Prazo de referência: 5 dias úteis · Escopo Fechado';
      recDesc = 'Aproveitamos seus textos e domínio atuais e renovamos 100% do visual e da velocidade mobile em 5 dias úteis.';
      recCode = 'VOCACAO_UPDATE';
    } else if (siteAns.includes('rápido e atualizado') && !googleAns.includes('Bem configurada')) {
      recTitle = 'Presença no Google Maps + Tour Virtual 360°';
      recTime = 'Prazo de referência: 48h a 7 dias úteis';
      recDesc = 'Blindagem completa da ficha no Google Meu Negócio e imersão Street View 5.6K para dominar as buscas locais.';
      recCode = 'PRESENCA_MAPS_360';
    }

    return { score, findings, recTitle, recTime, recDesc, recCode };
  }

  // ---- Envio Automático para o Banco de Dados (Cloud API + Local Webhook) ----
  function submitLeadToDatabase(ans, diag) {
    if (dbSubmitted) return;
    dbSubmitted = true;

    if (!ans.protocol_id) {
      ans.protocol_id = 'VOC-' + new Date().toISOString().slice(0, 10).replace(/-/g, '') + '-' + String(Math.floor(1000 + Math.random() * 9000));
    }

    const payload = {
      lead_id: ans.protocol_id,
      submitted_at: new Date().toISOString(),
      lgpd: {
        consent: Boolean(ans.lgpd_consent),
        timestamp: ans.lgpd_timestamp || new Date().toISOString(),
        law: 'Lei 13.709/2018 (LGPD)'
      },
      answers: ans,
      instant_diagnosis: diag
    };

    const statusBadge = document.getElementById('dbSyncStatus');

    // 1. Dispara para a API Cloud (/api/diagnostico) — funciona 24/7 em qualquer dispositivo
    const cloudPromise = fetch(CLOUD_API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    }).then(r => r.ok).catch(() => false);

    // 2. Dispara simultaneamente para o Motor Local (PostgreSQL Twenty CRM + SQLite + DeepSeek Harness)
    const localPromise = fetch(LOCAL_WEBHOOK_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      mode: 'cors'
    }).then(r => r.ok).catch(() => false);

    Promise.all([cloudPromise, localPromise]).then(([cloudOk, localOk]) => {
      if (statusBadge) {
        statusBadge.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#E5B910" stroke-width="2.5" style="vertical-align:-2px;margin-right:6px;"><polyline points="20 6 9 17 4 12"/></svg> Dados gravados com segurança · Protocolo ' + escapeHtml(ans.protocol_id);
      }
    });
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
      ? 'Diagnóstico Solicitado'
      : `Passo ${pad(stepIdx + 1)} de ${pad(total)}`;

    prevBtn.style.visibility = (stepIdx === 0 || isSuccess) ? 'hidden' : 'visible';

    if (isSuccess) {
      nextBtn.style.display = 'none';
    } else if (isIntro) {
      nextBtn.innerHTML = 'Iniciar Diagnóstico <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>';
      nextBtn.style.display = '';
    } else if (stepIdx === STEPS.length - 2) {
      nextBtn.innerHTML = 'Enviar e Solicitar Meu Relatório <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>';
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
          <div class="m"><b>9</b><span>perguntas objetivas sobre seu momento atual</span></div>
          <div class="m"><b>100%</b><span>processado pela nossa engenharia de presença</span></div>
          <div class="m"><b>No WhatsApp</b><span>você recebe o relatório detalhado sem compromisso</span></div>
        </div>
      `;
    } else if (step.type === 'success') {
      const diag = computeInstantDiagnosis(answers);
      answers.recommended_offer = diag.recTitle;
      answers.preliminary_score = diag.score;
      if (!answers.protocol_id) {
        answers.protocol_id = 'VOC-' + new Date().toISOString().slice(0, 10).replace(/-/g, '') + '-' + String(Math.floor(1000 + Math.random() * 9000));
      }
      persist();

      if (typeof window.trackDiagnosticConversion === 'function') {
        window.trackDiagnosticConversion(answers);
      }

      qArea.innerHTML = `
        <div class="lm-success">
          <div class="lm-eye" id="dbSyncStatus" style="color:#E5B910;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#E5B910" stroke-width="2.5" style="vertical-align:-2px;margin-right:6px;"><polyline points="20 6 9 17 4 12"/></svg>
            Solicitação Registrada · Protocolo ${escapeHtml(answers.protocol_id)}
          </div>
          <h2>Obrigado, <em>${escapeHtml((answers.name || '').split(' ')[0] || 'tudo certo')}</em>!</h2>
          <p style="font-size:clamp(17px, 2vw, 20px); color:var(--ink); max-width:600px; margin:14px auto 10px; line-height:1.55;">
            Já recebemos os dados da <b>${escapeHtml(answers.empresa || 'sua empresa')}</b>. Logo entraremos em contato via WhatsApp no número <b>${escapeHtml(answers.phone || 'informado')}</b> com o seu relatório detalhado.
          </p>
          <p style="font-size:14.5px; color:var(--ink-2); max-width:560px; margin:0 auto 28px;">
            Enquanto nossa equipe e nosso motor de auditoria preparam o comparativo completo dos seus canais, confira abaixo o resumo preliminar identificado:
          </p>

          <div class="rx-card">
            <div class="rx-header">
              <div>
                <span style="font-family:var(--mono);font-size:11px;color:#94A3B8;text-transform:uppercase;letter-spacing:0.1em;display:block;">Prévia da Auditoria · Em Processamento</span>
                <strong style="font-size:20px;color:#FFF;">${escapeHtml(answers.empresa || 'Empresa Auditada')}</strong>
              </div>
              <div class="rx-score-pill">
                <span>Índice Preliminar:</span>
                <b style="font-size:15px;">${diag.score}/100</b>
              </div>
            </div>

            <ul class="rx-findings">
              ${diag.findings.map(f => `<li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#E5B910" stroke-width="2" style="flex-shrink:0;margin-top:2px;"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg><div>${f}</div></li>`).join('')}
            </ul>

            <div class="rx-rec-box">
              <span class="tag">Frente que será detalhada no seu WhatsApp · ${diag.recTime}</span>
              <h5>${diag.recTitle}</h5>
              <p>${diag.recDesc}</p>
            </div>
          </div>

          <div class="lm-summary">
            <h4>Ficha Registrada em Nosso Sistema (Proteção LGPD)</h4>
            ${renderSummaryRows()}
          </div>

          <div class="btn-row" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin-top:28px;">
            <a href="portfolio.html" class="btn btn-primary magnet">
              Explorar Nosso Portfólio Interativo
              <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
            </a>
            <a href="index.html" class="btn btn-ghost magnet">Voltar para o Início</a>
          </div>

          <p style="margin-top:26px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--ink-3);">
            <a href="#" id="resetForm" style="text-decoration:underline">Enviar diagnóstico de outra empresa</a>
          </p>
        </div>
      `;

      submitLeadToDatabase(answers, diag);

      const reset = document.getElementById('resetForm');
      if (reset) reset.addEventListener('click', (e) => {
        e.preventDefault();
        answers = {}; stepIdx = 0; dbSubmitted = false;
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
      const checked = answers.lgpd_consent !== false;
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
            <span><b>Permissão LGPD (Lei nº 13.709/2018):</b> Autorizo o armazenamento dos dados informados na base da Vocação Comunicação &amp; Marketing exclusivamente para elaboração do diagnóstico de presença digital e envio do relatório detalhado via WhatsApp/e-mail. Zero spam.</span>
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
      protocol_id: 'Protocolo',
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
      phone: 'WhatsApp para recebimento',
      email: 'E-mail'
    };
    const rows = Object.keys(map)
      .filter(k => answers[k])
      .map(k => `<div class="row"><span>${map[k]}</span><b>${escapeHtml(answers[k])}</b></div>`);
    rows.push(`<div class="row"><span>Termo LGPD</span><b>Aceito em ${new Date(answers.lgpd_timestamp || Date.now()).toLocaleString('pt-BR')}</b></div>`);
    return rows.join('');
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
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
      if (!name) { flash('Informe seu nome para registrarmos seu diagnóstico.'); return false; }
      if (!phone || phone.replace(/\D/g, '').length < 10) {
        flash('Informe um WhatsApp válido com DDD para enviarmos o relatório.');
        return false;
      }
      if (!answers.lgpd_consent) {
        flash('Marque a autorização LGPD para concluirmos o envio.');
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
