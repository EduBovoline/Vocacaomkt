/* ============================================================
   MMFoods Panificação - O Fabricante das Padarias
   Vocação Update · Vanilla JS, zero dependências de framework
   ============================================================ */
(function () {
  'use strict';

  var WHATSAPP_SP = '551143281092';
  var WHATSAPP_MG = '553133819477';
  var EMAIL_B2B = 'contato@mmfoods.com.br';
  var STORAGE_KEY = 'mmfoods_cotacao_b2b_v1';

  /* Atendimento Comercial B2B: Seg-Sex 07h30-18h00, Sáb 08h00-12h00 */
  var HOURS = {
    0: null,
    1: [450, 1080],
    2: [450, 1080],
    3: [450, 1080],
    4: [450, 1080],
    5: [450, 1080],
    6: [480, 720]
  };
  var DAY_NAMES = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'];

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  function nowInSP() {
    var parts = new Intl.DateTimeFormat('en-US', {
      timeZone: 'America/Sao_Paulo',
      weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false
    }).formatToParts(new Date());
    var map = {};
    parts.forEach(function (p) { map[p.type] = p.value; });
    var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    return {
      day: days[map.weekday],
      minutes: parseInt(map.hour, 10) % 24 * 60 + parseInt(map.minute, 10)
    };
  }

  function hhmm(min) {
    var h = Math.floor(min / 60);
    var m = min % 60;
    return m === 0 ? h + 'h' : h + 'h' + (m < 10 ? '0' + m : m);
  }

  function statusNow() {
    var now = nowInSP();
    var today = HOURS[now.day];
    if (today && now.minutes >= today[0] && now.minutes < today[1]) {
      return { open: true, text: 'Atendimento B2B online · até ' + hhmm(today[1]) };
    }
    return { open: true, text: 'Fábricas SP & MG · Cotação 24h' };
  }

  function paintStatus() {
    var s = statusNow();
    var txt = $('[data-status-text]');
    if (txt) txt.textContent = s.text;
  }

  /* ---------- Header sticky ---------- */
  var header = $('.site-header');
  function onScroll() {
    if (!header) return;
    var lim = 8;
    var w = document.querySelector('.world');
    if (w) lim = Math.max(8, w.offsetHeight - window.innerHeight - 40);
    header.classList.toggle('is-stuck', window.scrollY > lim);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Filtro & Busca do Catálogo B2B ---------- */
  var chips = $$('[data-filter]');
  var groups = $$('.menu-group');
  var cards = $$('.pcard');
  var searchInput = $('#catalogSearch');
  var activeFilter = 'all';

  function applyCatalogFilter() {
    var q = (searchInput ? searchInput.value : '').trim().toLowerCase();
    chips.forEach(function (c) {
      c.setAttribute('aria-pressed', String(c.getAttribute('data-filter') === activeFilter));
    });
    groups.forEach(function (g) {
      var groupSlug = g.getAttribute('data-group');
      var groupMatch = (activeFilter === 'all' || groupSlug === activeFilter);
      if (!groupMatch) {
        g.hidden = true;
        return;
      }
      var visibleInGroup = 0;
      $$('.pcard', g).forEach(function (card) {
        var text = (card.getAttribute('data-search') || '').toLowerCase();
        var match = !q || text.indexOf(q) !== -1;
        card.style.display = match ? '' : 'none';
        if (match) visibleInGroup++;
      });
      g.hidden = visibleInGroup === 0;
    });
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      activeFilter = chip.getAttribute('data-filter') || 'all';
      applyCatalogFilter();
      var catSec = $('#catalogo');
      if (catSec && chip.classList.contains('cat-card')) {
        var controls = $('.catalog-controls');
        if (controls) {
          var y = controls.getBoundingClientRect().top + window.scrollY - 96;
          window.scrollTo({ top: y, behavior: 'smooth' });
        }
      }
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', applyCatalogFilter);
  }

  /* ---------- Cotação B2B (Carrinho de Lotes / Caixas) ---------- */
  var state = {
    items: [],
    modalidade: 'Revenda + Comodato',
    regional: 'SP',
    empresa: '',
    cnpj: '',
    contato: '',
    obs: ''
  };

  function load() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      var data = JSON.parse(raw);
      if (data && Array.isArray(data.items)) {
        state.items = data.items.filter(function (i) { return i && i.name && i.qty > 0; });
        state.modalidade = data.modalidade || 'Revenda + Comodato';
        state.regional = data.regional || 'SP';
        state.empresa = data.empresa || '';
        state.cnpj = data.cnpj || '';
        state.contato = data.contato || '';
        state.obs = data.obs || '';
      }
    } catch (e) {}
  }

  function save() {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); } catch (e) {}
  }

  function countBoxes() {
    return state.items.reduce(function (n, i) { return n + i.qty; }, 0);
  }

  function totalWeightKg() {
    return state.items.reduce(function (sum, i) { return sum + (i.weight || 0) * i.qty; }, 0);
  }

  function formatKg(v) {
    return v.toLocaleString('pt-BR', { minimumFractionDigits: v % 1 ? 1 : 0, maximumFractionDigits: 1 }) + ' Kg';
  }

  function addItem(name, pack, weight, line) {
    var found = null;
    state.items.forEach(function (i) { if (i.name === name) found = i; });
    if (found) {
      found.qty += 1;
    } else {
      state.items.push({
        name: name,
        pack: pack || '5 Kg por embalagem',
        weight: parseFloat(weight) || 5,
        line: line || 'Panificação',
        qty: 1
      });
    }
    save();
    render();
    toast(name + ' adicionado à cotação B2B');
  }

  function setQty(name, delta) {
    state.items.forEach(function (i) { if (i.name === name) i.qty += delta; });
    state.items = state.items.filter(function (i) { return i.qty > 0; });
    save();
    render();
  }

  var cartLines = $('#cartLines');
  var cartEmpty = $('#cartEmpty');
  var cartCount = $('#cartCount');
  var cartFab = $('#cartFab');
  var cartTotalEl = $('#cartTotal');
  var sendBtn = $('#sendOrder');
  var sendEmailBtn = $('#sendOrderEmail');

  function render() {
    var boxes = countBoxes();
    var kg = totalWeightKg();
    if (cartCount) cartCount.textContent = String(boxes);
    if (cartFab) cartFab.classList.toggle('is-visible', boxes > 0);
    if (sendBtn) sendBtn.disabled = boxes === 0;
    if (sendEmailBtn) sendEmailBtn.disabled = boxes === 0;
    if (cartEmpty) cartEmpty.style.display = boxes === 0 ? '' : 'none';
    if (cartTotalEl) cartTotalEl.textContent = boxes + (boxes === 1 ? ' caixa (' : ' caixas (') + formatKg(kg) + ')';
    if (!cartLines) return;

    cartLines.innerHTML = '';
    state.items.forEach(function (item) {
      var line = document.createElement('div');
      line.className = 'cart-line';
      line.innerHTML =
        '<div><h3></h3><span class="unit"></span></div>' +
        '<div class="qty">' +
        '<button type="button" data-dec aria-label="Remover uma caixa"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/></svg></button>' +
        '<span>' + item.qty + '</span>' +
        '<button type="button" data-inc aria-label="Adicionar uma caixa"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>' +
        '</div>';
      $('h3', line).textContent = item.name;
      $('.unit', line).textContent = item.line + ' · ' + item.qty + ' cx × ' + item.pack + ' (' + formatKg(item.qty * item.weight) + ')';
      $('[data-dec]', line).addEventListener('click', function () { setQty(item.name, -1); });
      $('[data-inc]', line).addEventListener('click', function () { setQty(item.name, 1); });
      cartLines.appendChild(line);
    });
  }

  document.addEventListener('click', function (ev) {
    var trigger = ev.target.closest ? ev.target.closest('[data-add]') : null;
    if (trigger) {
      ev.preventDefault();
      addItem(
        trigger.getAttribute('data-add'),
        trigger.getAttribute('data-pack'),
        trigger.getAttribute('data-weight'),
        trigger.getAttribute('data-line')
      );
      trigger.classList.add('is-added');
      setTimeout(function () { trigger.classList.remove('is-added'); }, 750);
    }
  });

  /* ---------- Drawer ---------- */
  var drawer = $('#cartDrawer');
  var overlay = $('#cartOverlay');
  var lastFocus = null;

  function openCart() {
    if (!drawer) return;
    lastFocus = document.activeElement;
    drawer.classList.add('is-open');
    overlay.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.classList.add('is-locked');
    var close = $('#cartClose');
    if (close) close.focus();
  }

  function closeCart() {
    if (!drawer) return;
    drawer.classList.remove('is-open');
    overlay.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('is-locked');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  if (cartFab) cartFab.addEventListener('click', openCart);
  $$('[data-open-cart]').forEach(function (b) { b.addEventListener('click', openCart); });
  if (overlay) overlay.addEventListener('click', closeCart);
  var closeBtn = $('#cartClose');
  if (closeBtn) closeBtn.addEventListener('click', closeCart);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('is-open')) closeCart();
  });

  /* Campos do Drawer */
  var empInput = $('#empresa');
  var cnpjInput = $('#cnpj');
  var contInput = $('#contatoNome');
  var regSelect = $('#regionalSelect');
  var obsInput = $('#obs');

  if (empInput) empInput.addEventListener('input', function () { state.empresa = empInput.value; save(); });
  if (cnpjInput) cnpjInput.addEventListener('input', function () { state.cnpj = cnpjInput.value; save(); });
  if (contInput) contInput.addEventListener('input', function () { state.contato = contInput.value; save(); });
  if (regSelect) regSelect.addEventListener('change', function () { state.regional = regSelect.value; save(); });
  if (obsInput) obsInput.addEventListener('input', function () { state.obs = obsInput.value; save(); });
  $$('input[name="modalidade"]').forEach(function (radio) {
    radio.addEventListener('change', function () {
      if (radio.checked) { state.modalidade = radio.value; save(); }
    });
  });

  function syncForm() {
    if (empInput) empInput.value = state.empresa;
    if (cnpjInput) cnpjInput.value = state.cnpj;
    if (contInput) contInput.value = state.contato;
    if (regSelect) regSelect.value = state.regional;
    if (obsInput) obsInput.value = state.obs;
    $$('input[name="modalidade"]').forEach(function (radio) {
      radio.checked = radio.value === state.modalidade;
    });
  }

  function buildMessage() {
    var lines = [];
    lines.push('Olá! Vim pelo site da *MMFoods - O Fabricante das Padarias*');
    lines.push('*Solicitação de Cotação Comercial B2B*');
    lines.push('Modalidade: *' + state.modalidade + '*');
    lines.push('Unidade de Atendimento: *' + state.regional + '*');
    lines.push('');
    lines.push('*Mix Selecionado:*');
    state.items.forEach(function (i) {
      lines.push('- ' + i.qty + ' cx x ' + i.name + ' (' + i.pack + ') = ' + formatKg(i.qty * i.weight));
    });
    lines.push('');
    lines.push('*Volume Total Estimado: ' + countBoxes() + ' caixas (' + formatKg(totalWeightKg()) + ')*');
    if (state.empresa.trim()) lines.push('Empresa / Loja: ' + state.empresa.trim());
    if (state.cnpj.trim()) lines.push('CNPJ / Cidade: ' + state.cnpj.trim());
    if (state.contato.trim()) lines.push('Responsável: ' + state.contato.trim());
    if (state.obs.trim()) lines.push('Observações: ' + state.obs.trim());
    return lines.join('\n');
  }

  if (sendBtn) {
    sendBtn.addEventListener('click', function () {
      if (!state.items.length) return;
      var targetPhone = state.regional === 'MG' ? WHATSAPP_MG : WHATSAPP_SP;
      var url = 'https://wa.me/' + targetPhone + '?text=' + encodeURIComponent(buildMessage());
      window.open(url, '_blank', 'noopener');
    });
  }

  if (sendEmailBtn) {
    sendEmailBtn.addEventListener('click', function () {
      if (!state.items.length) return;
      var subj = 'Cotação Comercial B2B MMFoods - ' + (state.empresa.trim() || state.modalidade);
      var mailUrl = 'mailto:' + EMAIL_B2B + '?subject=' + encodeURIComponent(subj) + '&body=' + encodeURIComponent(buildMessage());
      window.location.href = mailUrl;
    });
  }

  /* ---------- Formulário de Contato B2B (Seção Contato) ---------- */
  var b2bForm = $('#b2bContactForm');
  if (b2bForm) {
    b2bForm.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var nome = ($('#cfNome') || {}).value || '';
      var empresa = ($('#cfEmpresa') || {}).value || '';
      var email = ($('#cfEmail') || {}).value || '';
      var tel = ($('#cfTel') || {}).value || '';
      var unidade = ($('#cfUnidade') || {}).value || 'Matriz São Paulo (Vila Medeiros)';
      var assunto = ($('#cfAssunto') || {}).value || 'Parceria Comercial & Comodato';
      var msg = ($('#cfMensagem') || {}).value || '';

      var canal = (ev.submitter && ev.submitter.getAttribute('data-channel')) || 'whatsapp';
      var texto = [
        'Olá! Vim pelo site da *MMFoods Panificação* e gostaria de atendimento comercial.',
        '*Assunto:* ' + assunto,
        '*Unidade:* ' + unidade,
        '*Nome:* ' + nome,
        '*Empresa / Padaria / Supermercado:* ' + empresa,
        '*Telefone:* ' + tel,
        '*E-mail:* ' + email,
        msg ? ('*Mensagem:* ' + msg) : ''
      ].filter(Boolean).join('\n');

      if (canal === 'email') {
        window.location.href = 'mailto:' + EMAIL_B2B + '?subject=' + encodeURIComponent('[Site MMFoods] ' + assunto + ' - ' + empresa) + '&body=' + encodeURIComponent(texto);
      } else {
        var phone = unidade.indexOf('Contagem') !== -1 ? WHATSAPP_MG : WHATSAPP_SP;
        window.open('https://wa.me/' + phone + '?text=' + encodeURIComponent(texto), '_blank', 'noopener');
      }
      toast('Abrindo atendimento comercial MMFoods...');
    });
  }

  /* ---------- Modal de Artigos do Blog / Imprensa ---------- */
  var articleModalOverlay = $('#articleModalOverlay');
  var articleModalBody = $('#articleModalBody');
  var articleModalClose = $('#articleModalClose');

  $$('[data-open-article]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var id = btn.getAttribute('data-open-article');
      var tpl = document.getElementById('tpl-article-' + id);
      if (!tpl || !articleModalOverlay || !articleModalBody) return;
      articleModalBody.innerHTML = tpl.innerHTML;
      articleModalOverlay.classList.add('is-open');
      articleModalOverlay.setAttribute('aria-hidden', 'false');
      document.body.classList.add('is-locked');
    });
  });

  function closeArticleModal() {
    if (!articleModalOverlay) return;
    articleModalOverlay.classList.remove('is-open');
    articleModalOverlay.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('is-locked');
  }

  if (articleModalClose) articleModalClose.addEventListener('click', closeArticleModal);
  if (articleModalOverlay) {
    articleModalOverlay.addEventListener('click', function (ev) {
      if (ev.target === articleModalOverlay) closeArticleModal();
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && articleModalOverlay && articleModalOverlay.classList.contains('is-open')) {
      closeArticleModal();
    }
  });

  /* ---------- Toast ---------- */
  var toastEl = $('#toast');
  var toastTimer = null;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.classList.add('is-visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove('is-visible'); }, 2200);
  }

  /* ---------- Reveal ---------- */
  var REVEAL_SEL = '.section__head, .kpis, .pillars, .adv-layout, .cat-showcase, .menu-group, .story__grid, .blog-grid, .units-layout';
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var vh = window.innerHeight || 800;
    var alvos = $$(REVEAL_SEL).filter(function (el) {
      return el.getBoundingClientRect().top > vh * 0.92;
    });
    alvos.forEach(function (el) { el.classList.add('rise'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });
    alvos.forEach(function (el) { io.observe(el); });

    setTimeout(function () {
      alvos.forEach(function (el) {
        if (el.classList.contains('in')) return;
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('in');
      });
    }, 2000);
  }

  /* ---------- Scroll World (Scrubbing real pelo Scroll · Blob URL) ---------- */
  var world = $('#world');
  if (world) {
    var worldVideo = $('#worldVideo');
    var worldBar = $('#worldBar');
    var worldHint = $('#worldHint');
    var steps = $$('.wstep');
    var routeDots = $$('.world__route button');
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var coarsePointer = window.matchMedia('(hover: none) and (pointer: coarse)').matches;
    var worldTotal = 1;

    var videoReady = false;
    var targetProgress = 0;
    var curProgress = 0;
    var userPrimed = false;
    var currentBlobUrl = null;
    var loadedSrc = '';

    function primeMobileVideo() {
      if (userPrimed || !worldVideo) return;
      userPrimed = true;
      if (coarsePointer) {
        try {
          var p = worldVideo.play();
          if (p && p.then) p.then(function () { try { worldVideo.pause(); } catch (e) {} }).catch(function () {});
        } catch (e) {}
      }
    }
    window.addEventListener('pointerdown', primeMobileVideo, { once: true, passive: true });
    window.addEventListener('touchstart', primeMobileVideo, { once: true, passive: true });

    function loadVideo() {
      if (!worldVideo) return;
      var portrait = window.innerWidth < 780;
      var src = portrait ? 'assets/vid/world-portrait.mp4' : 'assets/vid/world-1280.mp4';
      if (loadedSrc === src) return;
      loadedSrc = src;
      worldVideo.poster = portrait ? 'assets/img/world-poster-portrait.webp' : 'assets/img/world-poster.webp';

      if (reduceMotion) {
        worldVideo.src = src;
        return;
      }

      /* Carrega como Blob em memória: garante video.seekable total mesmo sem HTTP Range */
      fetch(src)
        .then(function (r) { return r.ok ? r.blob() : Promise.reject(new Error('video fetch fail')); })
        .then(function (blob) {
          if (currentBlobUrl) URL.revokeObjectURL(currentBlobUrl);
          currentBlobUrl = URL.createObjectURL(blob);
          videoReady = false;
          worldVideo.pause();
          worldVideo.removeAttribute('autoplay');
          worldVideo.removeAttribute('loop');
          worldVideo.muted = true;
          worldVideo.playsInline = true;
          worldVideo.src = currentBlobUrl;
          worldVideo.addEventListener('loadedmetadata', function () {
            videoReady = true;
            try { worldVideo.pause(); } catch (e) {}
            try { worldVideo.currentTime = Math.min(0.995, targetProgress) * (worldVideo.duration || 1); } catch (e) {}
            if (userPrimed && coarsePointer) primeMobileVideo();
          }, { once: true });
        })
        .catch(function () {
          /* Fallback direto caso aberto via file:// */
          worldVideo.src = src;
          worldVideo.addEventListener('loadedmetadata', function () {
            videoReady = true;
            try { worldVideo.pause(); } catch (e) {}
          }, { once: true });
        });
    }

    function measure() {
      worldTotal = Math.max(1, world.offsetHeight - window.innerHeight);
    }

    var worldStage = $('.world__stage');
    var worldFade = $('#worldFade');

    function paintWorld() {
      var rect = world.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, -rect.top / worldTotal));
      targetProgress = p;

      if (worldStage) worldStage.classList.toggle('is-off', rect.bottom <= 2);
      if (worldFade) worldFade.style.opacity = Math.min(1, Math.max(0, (p - 0.9) / 0.1)).toFixed(3);
      if (worldBar) worldBar.style.transform = 'scaleX(' + p + ')';
      if (worldHint) worldHint.classList.toggle('is-hidden', p > 0.015);

      var n = steps.length;
      var lead = 0.94;
      var seg = Math.min(n, (p / lead) * n);
      var active = Math.min(n - 1, Math.max(0, Math.floor(seg)));

      function smooth(x) { x = Math.min(1, Math.max(0, x)); return x * x * (3 - 2 * x); }

      steps.forEach(function (el, i) {
        var t = seg - i;
        var op = 0;
        if (t >= 0 && t <= 1) {
          if (t < 0.12) op = i === 0 ? 1 : smooth(t / 0.12);
          else if (t < 0.88 || i === n - 1) op = 1;
          else op = 1 - smooth((t - 0.88) / 0.12);
        }
        el.classList.toggle('is-active', i === active);
        if (!reduceMotion) {
          el.style.opacity = op;
          el.style.transform = 'translateY(' + ((1 - op) * 22).toFixed(1) + 'px)';
        }
      });

      routeDots.forEach(function (d, i) {
        d.classList.toggle('is-active', i === active);
      });
    }

    function scrubLoop() {
      if (!reduceMotion && videoReady && worldVideo && worldVideo.duration && !worldVideo.seeking) {
        curProgress += (targetProgress - curProgress) * 0.16;
        var dur = worldVideo.duration;
        var desiredTime = Math.min(0.996, Math.max(0, curProgress)) * dur;
        var eps = coarsePointer ? 0.035 : 0.012;
        if (Math.abs(worldVideo.currentTime - desiredTime) > eps) {
          try { worldVideo.currentTime = desiredTime; } catch (e) {}
        }
      }
      requestAnimationFrame(scrubLoop);
    }

    var laidOutW = window.innerWidth;
    loadVideo();
    measure();
    paintWorld();
    requestAnimationFrame(scrubLoop);

    window.addEventListener('scroll', paintWorld, { passive: true });
    window.addEventListener('resize', function () {
      if (coarsePointer && window.innerWidth === laidOutW) return;
      laidOutW = window.innerWidth;
      measure();
      loadVideo();
      paintWorld();
    });

    routeDots.forEach(function (dot) {
      dot.addEventListener('click', function () {
        var i = Number(dot.getAttribute('data-goto')) || 0;
        var y = world.offsetTop + (i + 0.45) * (worldTotal / steps.length);
        window.scrollTo({ top: y, behavior: reduceMotion ? 'auto' : 'smooth' });
      });
    });
  }

  /* ---------- Init ---------- */
  load();
  syncForm();
  render();
  paintStatus();
  setInterval(paintStatus, 60000);
})();
