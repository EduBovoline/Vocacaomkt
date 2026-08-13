/* ============================================
   VOCAÇÃO — Motion & Interactions
   ============================================ */

(function(){
  'use strict';

  /* Apply tweakable defaults */
  function applyTweaks(t){
    if (!t) return;
    const root = document.documentElement;
    if (t.accent) {
      // Convert hex to oklch via canvas trick — easier: just set as plain hex
      root.style.setProperty('--accent', t.accent);
    }
    if (t.displayFont) root.style.setProperty('--display', `"${t.displayFont}", serif`);
    if (t.bodyFont) root.style.setProperty('--body', `"${t.bodyFont}", sans-serif`);
    if (t.palette === 'cool') {
      root.style.setProperty('--bg', 'oklch(0.97 0.008 240)');
      root.style.setProperty('--bg-2', 'oklch(0.93 0.012 240)');
      root.style.setProperty('--bg-3', 'oklch(0.20 0.018 250)');
      root.style.setProperty('--ink', 'oklch(0.20 0.018 250)');
    } else if (t.palette === 'mono') {
      root.style.setProperty('--bg', 'oklch(0.97 0 0)');
      root.style.setProperty('--bg-2', 'oklch(0.93 0 0)');
      root.style.setProperty('--bg-3', 'oklch(0.15 0 0)');
      root.style.setProperty('--ink', 'oklch(0.18 0 0)');
    } else {
      root.style.setProperty('--bg', 'oklch(0.975 0.004 260)');
      root.style.setProperty('--bg-2', 'oklch(0.945 0.005 260)');
      root.style.setProperty('--bg-3', 'oklch(0.21 0.045 240)');
      root.style.setProperty('--ink', 'oklch(0.21 0.045 240)');
    }
    document.body.classList.toggle('no-grain', t.grain === false);
  }
  window.__applyTweaks = applyTweaks;
  applyTweaks(window.__TWEAKS__);

  /* ---- Reveal on scroll ---- */
  const reveals = document.querySelectorAll('.reveal');

  // If the page loads while hidden (e.g. background tab, headless capture),
  // browsers freeze CSS transitions — apply no-anim so reveals snap to end state.
  if (document.hidden) document.documentElement.classList.add('no-anim');
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) {
      // Once visible, allow transitions again for subsequent reveals
      document.documentElement.classList.remove('no-anim');
    }
  });

  function showAll(){ reveals.forEach(el => el.classList.add('in')); }

  let io;
  try {
    io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -4% 0px' });
    reveals.forEach(el => io.observe(el));
  } catch (err) {
    showAll();
  }

  // Fallback 1: immediately reveal anything already in the viewport.
  function revealInViewport(){
    const vh = window.innerHeight;
    reveals.forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.top < vh * 0.96 && r.bottom > 0) el.classList.add('in');
    });
  }
  // Run after layout settles.
  requestAnimationFrame(() => requestAnimationFrame(revealInViewport));
  setTimeout(revealInViewport, 250);

  // Fallback 2: safety — if IO never fires within 2s, just show everything.
  setTimeout(() => {
    const stuck = document.querySelectorAll('.reveal:not(.in)');
    // If none in viewport got revealed (IO + manual both failed), force-show
    if (stuck.length > reveals.length * 0.6) showAll();
  }, 2200);

  // Reveal on scroll/resize as a low-cost fallback
  let raf;
  function onAnyScroll(){
    if (raf) return;
    raf = requestAnimationFrame(() => { raf = null; revealInViewport(); });
  }
  window.addEventListener('scroll', onAnyScroll, { passive: true });
  window.addEventListener('resize', onAnyScroll);

  /* ---- Nav scroll state ---- */
  const nav = document.getElementById('nav');
  let lastY = 0;
  function onScroll(){
    const y = window.scrollY;
    if (nav) nav.classList.toggle('scrolled', y > 24);
    lastY = y;
  }
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---- FAQ accordion ---- */
  document.querySelectorAll('.faq-item').forEach(item => {
    const btn = item.querySelector('.faq-q');
    if (!btn) return;
    btn.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(o => o.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });

  /* ---- Cursor halo ---- */
  const halo = document.getElementById('cursorHalo');
  if (halo && matchMedia('(hover: hover) and (pointer: fine)').matches) {
    let mx = window.innerWidth/2, my = window.innerHeight/2;
    let cx = mx, cy = my;
    window.addEventListener('pointermove', e => { mx = e.clientX; my = e.clientY; });
    function tick(){
      cx += (mx - cx) * 0.12;
      cy += (my - cy) * 0.12;
      halo.style.transform = `translate(${cx}px, ${cy}px) translate(-50%,-50%)`;
      requestAnimationFrame(tick);
    }
    tick();
  }

  /* ---- Open first FAQ by default ---- */
  const firstFaq = document.querySelector('.faq-item');
  if (firstFaq) firstFaq.classList.add('open');

  /* ---- Parallax: hero subtle ---- */
  const hero = document.querySelector('.hero h1');
  if (hero && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.addEventListener('scroll', () => {
      const y = Math.min(window.scrollY, 500);
      hero.style.transform = `translateY(${y * 0.04}px)`;
    }, { passive: true });
  }

  /* ---- Step hover sequence ---- */
  document.querySelectorAll('.step').forEach((s, i) => {
    s.addEventListener('mouseenter', () => {
      document.querySelectorAll('.step').forEach((x, j) => {
        x.style.opacity = j === i ? '1' : '0.55';
      });
    });
    s.addEventListener('mouseleave', () => {
      document.querySelectorAll('.step').forEach(x => x.style.opacity = '1');
    });
  });

  /* ---- KINETIC WORD ---- */
  const kinetic = document.getElementById('kinetic');
  if (kinetic) {
    const words = ['parecer', 'transmitir', 'convencer', 'merecer'];
    let idx = 0;
    const span = kinetic.querySelector('.k-word');
    function rotate() {
      idx = (idx + 1) % words.length;
      span.style.transition = 'opacity .4s var(--ease), transform .4s var(--ease)';
      span.style.opacity = '0';
      span.style.transform = 'translateY(-12px)';
      setTimeout(() => {
        span.textContent = words[idx];
        span.style.transform = 'translateY(12px)';
        requestAnimationFrame(() => {
          span.style.opacity = '1';
          span.style.transform = 'translateY(0)';
        });
      }, 400);
    }
    setInterval(rotate, 2600);
  }

  /* ---- SIDE INDEX ACTIVE ---- */
  const sideIndex = document.getElementById('sideIndex');
  if (sideIndex) {
    setTimeout(() => sideIndex.classList.add('in'), 600);
    const dots = Array.from(sideIndex.querySelectorAll('a'));
    const sections = dots.map(d => document.getElementById(d.dataset.section)).filter(Boolean);
    function updateIndex() {
      let active = 0;
      const y = window.scrollY + window.innerHeight * 0.4;
      sections.forEach((s, i) => {
        if (s.offsetTop <= y) active = i;
      });
      dots.forEach((d, i) => d.classList.toggle('active', i === active));
    }
    window.addEventListener('scroll', () => requestAnimationFrame(updateIndex), { passive: true });
    updateIndex();
  }

  /* ---- COUNTER ANIMATIONS ---- */
  function animateCounter(el) {
    const target = parseFloat(el.dataset.count);
    const isFloat = String(target).includes('.');
    const valEl = el.querySelector('.val');
    if (!valEl) return;
    const dur = 1400;
    const start = performance.now();
    function tick(t) {
      const p = Math.min(1, (t - start) / dur);
      const eased = 1 - Math.pow(1 - p, 3);
      const v = target * eased;
      valEl.textContent = isFloat ? v.toFixed(1).replace('.', ',') : Math.round(v).toString();
      if (p < 1) requestAnimationFrame(tick);
      else valEl.textContent = isFloat ? target.toFixed(1).replace('.', ',') : target.toString();
    }
    requestAnimationFrame(tick);
  }
  const countEls = document.querySelectorAll('.n[data-count]');
  if ('IntersectionObserver' in window) {
    const cio = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          animateCounter(e.target);
          cio.unobserve(e.target);
        }
      });
    }, { threshold: 0.3 });
    countEls.forEach(el => cio.observe(el));
  } else {
    countEls.forEach(animateCounter);
  }

  /* ---- MAGNETIC BUTTONS ---- */
  if (matchMedia('(hover: hover) and (pointer: fine)').matches) {
    document.querySelectorAll('.magnet').forEach(btn => {
      const strength = 0.18;
      btn.addEventListener('pointermove', (e) => {
        const r = btn.getBoundingClientRect();
        const x = (e.clientX - r.left - r.width / 2) * strength;
        const y = (e.clientY - r.top - r.height / 2) * strength;
        btn.style.transform = `translate(${x}px, ${y}px)`;
      });
      btn.addEventListener('pointerleave', () => {
        btn.style.transform = '';
      });
    });

    /* Cursor halo "engaged" on interactive elements */
    const halo = document.getElementById('cursorHalo');
    if (halo) {
      document.querySelectorAll('a, button, .btn').forEach(el => {
        el.addEventListener('pointerenter', () => halo.classList.add('engaged'));
        el.addEventListener('pointerleave', () => halo.classList.remove('engaged'));
      });
    }
  }

})();
