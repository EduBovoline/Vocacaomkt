/* ============================================================
   Little Kuppers Pie Shop — Vocação Update
   Vanilla JS, sem dependências.
   ============================================================ */
(function () {
  'use strict';

  var WHATSAPP = '5515974078395';
  var STORAGE_KEY = 'lk_pedido_v2';

  /* Horários: minutos desde 00h. Domingo fechado. */
  var HOURS = {
    0: null,
    1: [690, 1260],
    2: [690, 1260],
    3: [690, 1260],
    4: [690, 1260],
    5: [690, 1260],
    6: [720, 1290]
  };
  var DAY_NAMES = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'];

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  var money = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' });
  function brl(v) { return money.format(v || 0); }

  /* ---------- Utilidades de data (fuso de São Paulo) ---------- */
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
      return { open: true, text: 'Aberto agora · fecha às ' + hhmm(today[1]) };
    }
    if (today && now.minutes < today[0]) {
      return { open: false, text: 'Fechado · abre hoje às ' + hhmm(today[0]) };
    }
    for (var i = 1; i <= 7; i++) {
      var d = (now.day + i) % 7;
      var row = HOURS[d];
      if (row) {
        var when = i === 1 ? 'amanhã' : DAY_NAMES[d];
        return { open: false, text: 'Fechado · abre ' + when + ' às ' + hhmm(row[0]) };
      }
    }
    return { open: false, text: 'Fechado' };
  }

  function paintStatus() {
    var s = statusNow();
    var line = $('#statusPill');
    var txt = $('[data-status-text]');
    if (txt) txt.textContent = s.text;
    var dot = line ? $('.dot', line) : null;
    if (dot) dot.classList.toggle('is-closed', !s.open);

    var today = nowInSP().day;
    $$('.hours tr[data-day]').forEach(function (tr) {
      tr.classList.toggle('is-today', Number(tr.dataset.day) === today);
    });
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

  /* ---------- Filtro do cardápio ---------- */
  var chips = $$('.chip');
  var groups = $$('.menu-group');
  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      var filter = chip.dataset.filter;
      chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c === chip)); });
      groups.forEach(function (g) {
        g.hidden = filter !== 'all' && g.dataset.group !== filter;
      });
    });
  });

  /* ---------- Carrinho ---------- */
  var state = { items: [], tipo: 'Retirada', nome: '', obs: '' };

  function load() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      var data = JSON.parse(raw);
      if (data && Array.isArray(data.items)) {
        state.items = data.items.filter(function (i) { return i && i.name && i.qty > 0; });
        state.tipo = data.tipo || 'Retirada';
        state.nome = data.nome || '';
        state.obs = data.obs || '';
      }
    } catch (e) { /* armazenamento indisponível */ }
  }

  function save() {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); } catch (e) {}
  }

  function count() {
    return state.items.reduce(function (n, i) { return n + i.qty; }, 0);
  }

  function total() {
    return state.items.reduce(function (sum, i) { return sum + (i.price || 0) * i.qty; }, 0);
  }

  function addItem(name, price) {
    var found = null;
    state.items.forEach(function (i) { if (i.name === name) found = i; });
    if (found) { found.qty += 1; } else { state.items.push({ name: name, price: Number(price) || 0, qty: 1 }); }
    save();
    render();
    toast(name + ' no pedido');
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

  function render() {
    var qty = count();
    if (cartCount) cartCount.textContent = String(qty);
    if (cartFab) cartFab.classList.toggle('is-visible', qty > 0);
    if (sendBtn) sendBtn.disabled = qty === 0;
    if (cartEmpty) cartEmpty.style.display = qty === 0 ? '' : 'none';
    if (cartTotalEl) cartTotalEl.textContent = brl(total());
    if (!cartLines) return;

    cartLines.innerHTML = '';
    state.items.forEach(function (item) {
      var line = document.createElement('div');
      line.className = 'cart-line';
      line.innerHTML =
        '<div><h3></h3><span class="unit"></span></div>' +
        '<div class="qty">' +
        '<button type="button" data-dec aria-label="Remover um"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/></svg></button>' +
        '<span>' + item.qty + '</span>' +
        '<button type="button" data-inc aria-label="Adicionar um"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>' +
        '</div>';
      $('h3', line).textContent = item.name;
      $('.unit', line).textContent = item.qty + ' × ' + brl(item.price);
      $('[data-dec]', line).addEventListener('click', function () { setQty(item.name, -1); });
      $('[data-inc]', line).addEventListener('click', function () { setQty(item.name, 1); });
      cartLines.appendChild(line);
    });
  }

  /* Delegação: qualquer elemento com data-add */
  document.addEventListener('click', function (ev) {
    var trigger = ev.target.closest ? ev.target.closest('[data-add]') : null;
    if (trigger) {
      ev.preventDefault();
      addItem(trigger.getAttribute('data-add'), trigger.getAttribute('data-price'));
      trigger.classList.add('is-added');
      setTimeout(function () { trigger.classList.remove('is-added'); }, 700);
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
  if (overlay) overlay.addEventListener('click', closeCart);
  var closeBtn = $('#cartClose');
  if (closeBtn) closeBtn.addEventListener('click', closeCart);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('is-open')) closeCart();
  });

  /* Campos */
  var nomeInput = $('#nome');
  var obsInput = $('#obs');
  if (nomeInput) nomeInput.addEventListener('input', function () { state.nome = nomeInput.value; save(); });
  if (obsInput) obsInput.addEventListener('input', function () { state.obs = obsInput.value; save(); });
  $$('input[name="tipo"]').forEach(function (radio) {
    radio.addEventListener('change', function () {
      if (radio.checked) { state.tipo = radio.value; save(); }
    });
  });

  function syncForm() {
    if (nomeInput) nomeInput.value = state.nome;
    if (obsInput) obsInput.value = state.obs;
    $$('input[name="tipo"]').forEach(function (radio) {
      radio.checked = radio.value === state.tipo;
    });
  }

  /* Enviar para o WhatsApp */
  function buildMessage() {
    var lines = [];
    lines.push('Olá! Vim pelo site da Little Kuppers 👋');
    lines.push('*Pedido — ' + state.tipo + '*');
    state.items.forEach(function (i) {
      lines.push('• ' + i.qty + '× ' + i.name + ' — ' + brl(i.price * i.qty));
    });
    lines.push('*Total: ' + brl(total()) + '*');
    if (state.obs.trim()) lines.push('Observação: ' + state.obs.trim());
    if (state.nome.trim()) lines.push('Meu nome: ' + state.nome.trim());
    return lines.join('\n');
  }

  if (sendBtn) {
    sendBtn.addEventListener('click', function () {
      if (!state.items.length) return;
      var url = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(buildMessage());
      window.open(url, '_blank', 'noopener');
    });
  }

  /* ---------- Toast ---------- */
  var toastEl = $('#toast');
  var toastTimer = null;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.classList.add('is-visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove('is-visible'); }, 1900);
  }

  /* ---------- Reveal (só abaixo da dobra; com rede de segurança) ---------- */
  var REVEAL_SEL = '.section__head, .featured, .menu-group, .review, .visit__card, .story__media, .story__text, .reviews__foot';
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
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    alvos.forEach(function (el) { io.observe(el); });

    /* Rede de segurança: se algo visível continuar escondido, revela. */
    setTimeout(function () {
      alvos.forEach(function (el) {
        if (el.classList.contains('in')) return;
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('in');
      });
    }, 2200);
  }


  /* ---------- Scroll world (abertura) ---------- */
  var world = $('#world');
  if (world) {
    var worldVideo = $('#worldVideo');
    var worldBar = $('#worldBar');
    var worldHint = $('#worldHint');
    var steps = $$('.wstep');
    var routeDots = $$('.world__route button');
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var worldTotal = 1;

    function lerp(a, b, t) { return a + (b - a) * t; }

    function loadVideo() {
      if (!worldVideo) return;
      var portrait = window.innerWidth < 780;
      var src = portrait ? 'assets/vid/world-portrait.mp4' : 'assets/vid/world-1280.mp4';
      if (worldVideo.getAttribute('data-src') === src) return;
      worldVideo.setAttribute('data-src', src);
      worldVideo.poster = portrait ? 'assets/img/world-poster-portrait.webp' : 'assets/img/world-poster.webp';
      worldVideo.src = src;
      var pr = worldVideo.play();
      if (pr && pr.catch) pr.catch(function () {});
    }

    function measure() {
      worldTotal = Math.max(1, world.offsetHeight - window.innerHeight);
    }

    var worldStage = $('.world__stage');
    var worldFade = $('#worldFade');

    function paintWorld() {
      var rect = world.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, -rect.top / worldTotal));
      if (worldStage) worldStage.classList.toggle('is-off', rect.bottom <= 2);
      if (worldFade) worldFade.style.opacity = Math.min(1, Math.max(0, (p - 0.9) / 0.1)).toFixed(3);
      if (worldBar) worldBar.style.transform = 'scaleX(' + p + ')';
      if (worldHint) worldHint.classList.toggle('is-hidden', p > 0.015);

      var n = steps.length;
      var lead = 0.92;
      var seg = Math.min(n, (p / lead) * n);
      var active = Math.min(n - 1, Math.max(0, Math.floor(seg)));

      function smooth(x) { x = Math.min(1, Math.max(0, x)); return x * x * (3 - 2 * x); }

      steps.forEach(function (el, i) {
        var t = seg - i;
        var op = 0;
        if (t >= 0 && t <= 1) {
          if (t < 0.12) op = i === 0 ? 1 : smooth(t / 0.12);
          else if (t < 0.9 || i === n - 1) op = 1;
          else op = 1 - smooth((t - 0.9) / 0.1);
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

    loadVideo();
    measure();
    paintWorld();

    window.addEventListener('scroll', paintWorld, { passive: true });
    window.addEventListener('resize', function () {
      measure();
      loadVideo();
      paintWorld();
    });

    routeDots.forEach(function (dot) {
      dot.addEventListener('click', function () {
        var i = Number(dot.getAttribute('data-goto')) || 0;
        var y = world.offsetTop + (i + 0.5) * (worldTotal / steps.length);
        window.scrollTo({ top: y, behavior: reduceMotion ? 'auto' : 'smooth' });
      });
    });

    if ('IntersectionObserver' in window && worldVideo) {
      var vio = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            var pr = worldVideo.play();
            if (pr && pr.catch) pr.catch(function () {});
          } else {
            try { worldVideo.pause(); } catch (err) {}
          }
        });
      }, { threshold: 0.05 });
      vio.observe(world);
    }
  }

  /* ---------- Init ---------- */
  load();
  syncForm();
  render();
  paintStatus();
  setInterval(paintStatus, 60000);
})();
