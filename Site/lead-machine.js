/* ============================================
   LEAD MACHINE — Multi-step diagnostic intake
   ============================================ */

(function(){
  'use strict';

  const STORAGE_KEY = 'vocacao-lm-v1';

  const STEPS = [
    {
      id: 'intro',
      eyebrow: 'Antes de começar',
      title: 'Vamos entender sua <em>presença digital</em>.',
      help: 'Em 10 perguntas rápidas, mapeamos onde sua empresa pode estar perdendo confiança online. No final, você recebe um diagnóstico personalizado — sem proposta empurrada.',
      type: 'intro'
    },
    {
      id: 'empresa',
      eyebrow: '01 · Sua empresa',
      title: 'Qual o nome da sua empresa?',
      help: 'Como ela aparece — ou deveria aparecer — quando alguém procura no Google.',
      type: 'text',
      placeholder: 'Ex.: EZ Bikes Elétricas',
      required: true
    },
    {
      id: 'segmento',
      eyebrow: '02 · O que vocês fazem',
      title: 'Em que setor sua empresa atua?',
      help: 'Selecione a área que mais se aproxima do seu trabalho.',
      type: 'options',
      options: [
        'Serviço profissional (consultoria, jurídico, contábil)',
        'Saúde, estética ou bem-estar',
        'Comércio físico ou loja',
        'Construção, reforma, decoração',
        'Restaurante, café, padaria',
        'Serviço técnico (TI, manutenção, elétrica)',
        'Outro / vários setores'
      ]
    },
    {
      id: 'tempo',
      eyebrow: '03 · Tempo de operação',
      title: 'Há quanto tempo sua empresa existe?',
      help: 'Empresa nova precisa estruturar antes de divulgar. Empresa veterana muitas vezes precisa reorganizar o que já tem.',
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
      eyebrow: '04 · Site',
      title: 'Sua empresa tem site profissional?',
      help: 'Site no nome da empresa, com endereço, serviços e contato — fácil de encontrar e entender.',
      type: 'options',
      options: [
        'Sim, e está atualizado',
        'Tenho, mas está desatualizado ou improvisado',
        'Tinha, mas não está no ar',
        'Nunca tive site'
      ]
    },
    {
      id: 'google',
      eyebrow: '05 · Google',
      title: 'E o Meu Negócio no Google?',
      help: 'O perfil que aparece no mapa, com horário, fotos, avaliações. Hoje, é a primeira coisa que o cliente vê.',
      type: 'options',
      options: [
        'Sim, bem configurado e com avaliações',
        'Tenho, mas com informações desatualizadas',
        'Existe, mas mal feito ou abandonado',
        'Nunca configuramos'
      ]
    },
    {
      id: 'redes',
      eyebrow: '06 · Redes sociais',
      title: 'Como estão as redes sociais?',
      help: 'Instagram, Facebook ou onde sua empresa está presente. Não precisa postar todo dia — só não pode parecer abandonado.',
      type: 'options',
      options: [
        'Atualizadas com frequência',
        'Existem, mas postamos pouco',
        'Perfis abandonados há meses',
        'Não temos perfil oficial'
      ]
    },
    {
      id: 'gargalo',
      eyebrow: '07 · O que você sente',
      title: 'Qual o <em>maior gargalo</em> hoje?',
      help: 'Marque o que mais incomoda. Se for difícil escolher um, vá pelo que aparece mais nas conversas do dia a dia.',
      type: 'options',
      options: [
        'Clientes não me encontram online',
        'Encontram, mas não passam confiança',
        'Recebo contato, mas perco para concorrente',
        'Não sei avaliar o que está faltando'
      ]
    },
    {
      id: 'links',
      eyebrow: '08 · Seus canais online',
      title: 'Quais são os seus canais digitais?',
      help: 'Cole os links que você tiver — site, Instagram, Google Maps, Facebook. Todos opcionais. Quanto mais informação, mais preciso e personalizado será o diagnóstico.',
      type: 'links'
    },
    {
      id: 'contato',
      eyebrow: '09 · Para enviarmos a análise',
      title: 'Como entramos em contato?',
      help: 'Vamos analisar sua presença digital e enviar o diagnóstico em até 1 dia útil. Você recebe direto no canal que preferir.',
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

  // ---- DOM ----
  const qArea = document.getElementById('questionArea');
  const progressBar = document.getElementById('progressBar');
  const stepCounter = document.getElementById('stepCounter');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');

  function pad(n) { return String(n).padStart(2, '0'); }

  function render() {
    const step = STEPS[stepIdx];
    const total = STEPS.length - 1; // exclude success from counter
    const isSuccess = step.type === 'success';
    const isIntro = step.type === 'intro';

    // Progress
    const pct = isSuccess ? 100 : ((stepIdx + 1) / total) * 100;
    progressBar.style.width = pct + '%';
    stepCounter.textContent = isSuccess
      ? 'Concluído'
      : `Passo ${pad(stepIdx + 1)} de ${pad(total)}`;

    // Buttons
    prevBtn.style.visibility = (stepIdx === 0 || isSuccess) ? 'hidden' : 'visible';

    if (isSuccess) {
      nextBtn.style.display = 'none';
    } else if (isIntro) {
      nextBtn.innerHTML = 'Começar agora <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>';
      nextBtn.style.display = '';
    } else if (stepIdx === STEPS.length - 2) {
      // Last real question (contato)
      nextBtn.innerHTML = 'Enviar diagnóstico <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M9 7h8v8"></path></svg>';
      nextBtn.style.display = '';
    } else {
      nextBtn.innerHTML = 'Continuar <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>';
      nextBtn.style.display = '';
    }

    // Re-trigger entry animation
    qArea.classList.remove('step-anim');
    void qArea.offsetWidth;
    qArea.classList.add('step-anim');

    // Render content
    if (step.type === 'intro') {
      qArea.innerHTML = `
        <div class="lm-eye">${step.eyebrow}</div>
        <h2>${step.title}</h2>
        <p class="help">${step.help}</p>
        <div class="lm-final-marks">
          <div class="m"><b>10</b><span>perguntas rápidas, sem formulário gigante</span></div>
          <div class="m"><b>~4 min</b><span>tempo médio para responder</span></div>
          <div class="m"><b>1 dia útil</b><span>para receber o diagnóstico personalizado</span></div>
        </div>
      `;
    } else if (step.type === 'success') {
      const wa = buildWhatsAppLink();
      qArea.innerHTML = `
        <div class="lm-success">
          <div class="lm-eye">Concluído</div>
          <h2>Recebemos suas <em>respostas</em>.</h2>
          <p>Em até 1 dia útil enviamos uma análise honesta do que encontramos. Enquanto isso, dá pra adiantar — fala com a gente no WhatsApp.</p>
          <div class="lm-summary">
            <h4>Resumo do seu diagnóstico</h4>
            ${renderSummaryRows()}
          </div>
          <div class="btn-row" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
            <a href="${wa}" target="_blank" rel="noopener" class="btn btn-primary magnet">
              Continuar no WhatsApp
              <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M9 7h8v8"></path></svg>
            </a>
            <a href="index.html" class="btn btn-ghost magnet">Voltar para o site</a>
          </div>
          <p style="margin-top:30px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--ink-3);">
            <a href="#" id="resetForm" style="text-decoration:underline">Refazer o diagnóstico</a>
          </p>
        </div>
      `;
      const reset = document.getElementById('resetForm');
      if (reset) reset.addEventListener('click', (e) => {
        e.preventDefault();
        answers = {}; stepIdx = 0;
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
          ${step.options.map((opt, i) => `
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
          // Auto-advance for option questions
          setTimeout(() => {
            stepIdx = Math.min(stepIdx + 1, STEPS.length - 1);
            persist();
            render();
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }, 280);
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
          <input type="url" class="lm-input" id="linkSite" placeholder="Site (ex: minhaempresa.com.br)" value="${(answers.link_site || '').replace(/"/g, '&quot;')}" autocomplete="url" />
          <input type="url" class="lm-input" id="linkInstagram" placeholder="Instagram (ex: instagram.com/minhaempresa)" value="${(answers.link_instagram || '').replace(/"/g, '&quot;')}" />
          <input type="url" class="lm-input" id="linkFacebook" placeholder="Facebook (ex: facebook.com/minhaempresa)" value="${(answers.link_facebook || '').replace(/"/g, '&quot;')}" />
          <input type="text" class="lm-input" id="linkGoogle" placeholder="Google Maps — cole o link do perfil ou nome exato" value="${(answers.link_google || '').replace(/"/g, '&quot;')}" />
        </div>
      `;
      const lSite    = document.getElementById('linkSite');
      const lInsta   = document.getElementById('linkInstagram');
      const lFace    = document.getElementById('linkFacebook');
      const lGoogle  = document.getElementById('linkGoogle');
      lSite.focus();
      [['link_site', lSite], ['link_instagram', lInsta], ['link_facebook', lFace], ['link_google', lGoogle]].forEach(([k, el]) => {
        el.addEventListener('input', () => { answers[k] = el.value; persist(); });
        el.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); next(); } });
      });
    } else if (step.type === 'contact') {
      qArea.innerHTML = `
        <div class="lm-eye">${step.eyebrow}</div>
        <h2>${step.title}</h2>
        <p class="help">${step.help}</p>
        <div class="lm-options" style="gap:14px;">
          <input type="text" class="lm-input" id="contactName" placeholder="Seu nome" value="${(answers.name || '').replace(/"/g, '&quot;')}" autocomplete="name" />
          <input type="tel" class="lm-input" id="contactPhone" placeholder="WhatsApp com DDD" value="${(answers.phone || '').replace(/"/g, '&quot;')}" autocomplete="tel" />
          <input type="email" class="lm-input" id="contactEmail" placeholder="E-mail (opcional)" value="${(answers.email || '').replace(/"/g, '&quot;')}" autocomplete="email" />
        </div>
      `;
      const name = document.getElementById('contactName');
      const phone = document.getElementById('contactPhone');
      const email = document.getElementById('contactEmail');
      name.focus();
      [['name', name], ['phone', phone], ['email', email]].forEach(([k, el]) => {
        el.addEventListener('input', () => {
          answers[k] = el.value;
          persist();
        });
      });
    }
  }

  function renderSummaryRows() {
    const map = {
      empresa: 'Empresa',
      segmento: 'Setor',
      tempo: 'Tempo',
      site: 'Site',
      google: 'Google',
      redes: 'Redes',
      gargalo: 'Gargalo principal',
      link_site: '🌐 Link do site',
      link_instagram: '📸 Instagram',
      link_facebook: '👥 Facebook',
      link_google: '🗺️ Google Maps',
      name: 'Contato',
      phone: 'WhatsApp',
      email: 'E-mail'
    };
    return Object.keys(map)
      .filter(k => answers[k])
      .map(k => `<div class="row"><span>${map[k]}</span><b>${escapeHtml(answers[k])}</b></div>`)
      .join('');
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function buildWhatsAppLink() {
    const hasLinks = answers.link_site || answers.link_instagram || answers.link_facebook || answers.link_google;
    const lines = [
      'Olá! Acabei de fazer o diagnóstico no site da Vocação.',
      '',
      '📋 Resumo:',
      answers.empresa   ? '• Empresa: '  + answers.empresa   : null,
      answers.segmento  ? '• Setor: '    + answers.segmento  : null,
      answers.tempo     ? '• Tempo: '    + answers.tempo     : null,
      answers.site      ? '• Site: '     + answers.site      : null,
      answers.google    ? '• Google: '   + answers.google    : null,
      answers.redes     ? '• Redes: '    + answers.redes     : null,
      answers.gargalo   ? '• Gargalo: '  + answers.gargalo   : null,
      hasLinks ? '' : null,
      hasLinks ? '🔗 Links digitais:' : null,
      answers.link_site       ? '• Site: '        + answers.link_site       : null,
      answers.link_instagram  ? '• Instagram: '   + answers.link_instagram  : null,
      answers.link_facebook   ? '• Facebook: '    + answers.link_facebook   : null,
      answers.link_google     ? '• Google Maps: ' + answers.link_google     : null,
      '',
      'Quero falar sobre os próximos passos.'
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
        flash('Digite o nome antes de continuar.');
        return false;
      }
      return true;
    }
    if (step.type === 'options') {
      if (!answers[step.id]) {
        flash('Selecione uma opção.');
        return false;
      }
      return true;
    }
    if (step.type === 'contact') {
      const name = (answers.name || '').trim();
      const phone = (answers.phone || '').trim();
      if (!name) { flash('Coloca seu nome.'); return false; }
      if (!phone || phone.replace(/\D/g, '').length < 10) {
        flash('Coloca um WhatsApp válido (com DDD).');
        return false;
      }
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
      background: var(--ink); color: var(--bg);
      padding: 14px 22px; border-radius: 999px;
      font-size: 14px; z-index: 100;
      box-shadow: 0 10px 30px rgba(0,0,0,0.18);
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

  // Inject flash animation
  const styleEl = document.createElement('style');
  styleEl.textContent = `@keyframes fadeUp { from { opacity: 0; transform: translateX(-50%) translateY(10px); } to { opacity: 1; transform: translateX(-50%) translateY(0); } }`;
  document.head.appendChild(styleEl);

  render();
})();
