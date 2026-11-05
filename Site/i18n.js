/* ============================================================================
   VOCAÇÃO — LOCALIZAÇÃO DINÂMICA (i18n PT | EN | ES + MULTIMOEDA POR MERCADO)
   ----------------------------------------------------------------------------
   MERCADOS ATENDIDOS:
   1. Brasil (BR): BRL (R$) -> R$ 450, R$ 850, R$ 980
   2. Estados Unidos (US) e Canadá: USD ($) -> $450, $850, $980
   3. América Latina (México, etc.): USD ($) -> $450, $850, $980
   4. Europa (Zona do Euro): EUR (€) -> €450, €850, €980
   5. Reino Unido (UK): GBP (£) -> £450, £850, £980

   REGRAS:
   - Seletor visível e elegante: PT | EN | ES
   - Troca de idioma traduz toda a interface de forma consistente.
   - Moeda detectada por fuso/região com fallback configurável.
   ========================================================================== */

(function () {
  'use strict';

  const MARKETS = {
    BRL: { code: 'BRL', symbol: 'R$ ', prefix: true },
    USD: { code: 'USD', symbol: '$', prefix: true },
    EUR: { code: 'EUR', symbol: '€', prefix: true },
    GBP: { code: 'GBP', symbol: '£', prefix: true }
  };

  const BR_TIMEZONES = new Set([
    'America/Sao_Paulo', 'America/Fortaleza', 'America/Recife', 'America/Bahia',
    'America/Belem', 'America/Manaus', 'America/Cuiaba', 'America/Campo_Grande',
    'America/Porto_Velho', 'America/Boa_Vista', 'America/Maceio', 'America/Araguaina',
    'America/Santarem', 'America/Noronha', 'America/Eirunepe', 'America/Rio_Branco'
  ]);

  const UK_TIMEZONES = new Set([
    'Europe/London', 'Europe/Belfast', 'Europe/Guernsey', 'Europe/Isle_of_Man', 'Europe/Jersey'
  ]);

  function detectMarketCurrency() {
    try {
      const params = new URLSearchParams(window.location.search);
      const urlCurr = (params.get('currency') || params.get('moeda') || '').toUpperCase();
      if (MARKETS[urlCurr]) {
        localStorage.setItem('vocacao_currency', urlCurr);
        return urlCurr;
      }
      const saved = localStorage.getItem('vocacao_currency');
      if (saved && MARKETS[saved]) return saved;

      const tz = (Intl.DateTimeFormat().resolvedOptions().timeZone || '').trim();
      if (!tz) return 'BRL';

      if (BR_TIMEZONES.has(tz)) return 'BRL';
      if (UK_TIMEZONES.has(tz)) return 'GBP';
      if (tz.startsWith('Europe/') || tz.startsWith('Atlantic/')) return 'EUR';
      
      // EUA, México, América Latina e demais mercados internacionais
      return 'USD';
    } catch (e) {
      return 'BRL';
    }
  }

  function detectLanguage() {
    try {
      const params = new URLSearchParams(window.location.search);
      const urlLang = (params.get('lang') || '').toLowerCase();
      if (['pt', 'en', 'es'].includes(urlLang)) {
        localStorage.setItem('vocacao_lang', urlLang);
        return urlLang;
      }
      const saved = localStorage.getItem('vocacao_lang');
      if (saved && ['pt', 'en', 'es'].includes(saved)) return saved;

      const navLang = (navigator.language || navigator.userLanguage || 'pt-BR').toLowerCase();
      if (navLang.startsWith('en')) return 'en';
      if (navLang.startsWith('es')) return 'es';
      return 'pt';
    } catch (e) {
      return 'pt';
    }
  }

  let currentLang = detectLanguage();
  let currentCurrency = detectMarketCurrency();

  // Se o visitante está nos EUA/Europa/LatAm, o fuso já definiu a moeda dele (USD, EUR, GBP).
  // O seletor de idioma permite navegar em PT, EN ou ES SEM forçar a moeda para Real.
  // Apenas se o usuário escolher explicitamente a moeda BRL é que vira Real.

  // Dicionário de traduções estruturadas
  const DICT = {
    // Nav
    'Início': { en: 'Home', es: 'Inicio' },
    'Portfólio': { en: 'Portfolio', es: 'Portafolio' },
    'Falar no WhatsApp': { en: 'Chat on WhatsApp', es: 'Hablar por WhatsApp' },
    'Pedir Orçamento no WhatsApp ↗': { en: 'Request Quote on WhatsApp ↗', es: 'Pedir Presupuesto en WhatsApp ↗' },
    'Conhecer as Soluções': { en: 'Explore Solutions', es: 'Ver Soluciones' },
    'Pedir Diagnóstico no WhatsApp': { en: 'Get Audit on WhatsApp', es: 'Pedir Diagnóstico por WhatsApp' },
    'Preencher Diagnóstico Rápido': { en: 'Quick Diagnostic', es: 'Diagnóstico Rápido' },
    'Começar meu diagnóstico': { en: 'Start My Diagnostic', es: 'Comenzar mi diagnóstico' },
    
    // Benefícios e Pilares
    'Benefício 01 · Ser Encontrado': { en: 'Benefit 01 · Get Found', es: 'Beneficio 01 · Ser Encontrado' },
    'Benefício 02 · Transmitir Confiança': { en: 'Benefit 02 · Build Immediate Trust', es: 'Beneficio 02 · Transmitir Confianza' },
    'Benefício 03 · Facilitar o Contato': { en: 'Benefit 03 · Frictionless Contact', es: 'Beneficio 03 · Facilitar el Contacto' },
    'Estrutura antes do marketing': { en: 'Structure before marketing', es: 'Estructura antes del marketing' },
    'Confiança antes do tráfego': { en: 'Trust before traffic', es: 'Confianza antes del tráfico' },
    'Clareza antes da venda': { en: 'Clarity before the sale', es: 'Claridad antes de la venta' },
    'Organização antes da escala': { en: 'Organization before scale', es: 'Organización antes de escalar' },

    // Prazos e Condições
    'Escopo Fechado · Zero Mensalidade': { en: 'Fixed Scope · Zero Monthly Fees', es: 'Alcance Cerrado · Cero Mensualidades' },
    '5 a 7 dias úteis': { en: '5 to 7 business days', es: '5 a 7 días hábiles' },
    '50% entrada · 50% ao aprovar': { en: '50% deposit · 50% upon approval', es: '50% anticipo · 50% al aprobar' },
    'Garantia 50/50': { en: '50/50 Guarantee', es: 'Garantía 50/50' }
  };

  function formatPrice(val, curr) {
    const market = MARKETS[curr] || MARKETS.BRL;
    return market.symbol + val;
  }

  function applyLocalization() {
    document.documentElement.lang = currentLang === 'pt' ? 'pt-BR' : currentLang;

    // 1. Substituição de Preços consistente (R$ 450 -> $450 / €450 / £450)
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        const p = node.parentElement;
        if (!p || p.closest('.voc-i18n-bar') || p.tagName === 'SCRIPT' || p.tagName === 'STYLE') return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    const textNodes = [];
    let n;
    while ((n = walker.nextNode())) textNodes.push(n);

    textNodes.forEach(node => {
      let txt = node.nodeValue;
      
      // Tradução por dicionário
      if (currentLang !== 'pt') {
        const trimmed = txt.trim();
        if (DICT[trimmed] && DICT[trimmed][currentLang]) {
          txt = txt.replace(trimmed, DICT[trimmed][currentLang]);
        }
      }

      // Conversão de moeda dinâmica
      if (currentCurrency !== 'BRL') {
        txt = txt.replace(/R\$\s?(\d{1,3}(?:\.\d{3})*)/g, (match, num) => {
          return formatPrice(num, currentCurrency);
        });
      }

      if (txt !== node.nodeValue) {
        node.nodeValue = txt;
      }
    });

    // 2. Links do WhatsApp com moeda correspondente
    document.querySelectorAll('a[href*="wa.me"]').forEach(a => {
      let href = a.getAttribute('href');
      if (currentCurrency !== 'BRL' && href.includes('R%24')) {
        const sym = encodeURIComponent(MARKETS[currentCurrency].symbol);
        a.setAttribute('href', href.replace(/R%24%20|R%24/g, sym));
      }
    });

    // 3. Atualizar botões ativos no seletor
    document.querySelectorAll('.voc-i18n-btn').forEach(btn => {
      btn.classList.toggle('is-active', btn.getAttribute('data-lang') === currentLang);
    });
  }

  function injectBar() {
    if (document.getElementById('voc-i18n-styles')) return;

    const style = document.createElement('style');
    style.id = 'voc-i18n-styles';
    style.textContent = `
      .voc-i18n-bar {
        display: inline-flex;
        align-items: center;
        gap: 3px;
        background: rgba(4, 18, 27, 0.88);
        border: 1px solid rgba(229, 185, 16, 0.35);
        border-radius: 999px;
        padding: 3px 6px;
        font-family: 'Geist Mono', monospace;
        font-size: 11px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        margin: 0 10px;
        z-index: 1000;
      }
      .voc-i18n-btn {
        background: transparent;
        border: none;
        color: #94a3b8;
        font-family: inherit;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 8px;
        border-radius: 999px;
        cursor: pointer;
        transition: all 0.2s ease;
      }
      .voc-i18n-btn:hover { color: #fff; }
      .voc-i18n-btn.is-active {
        background: #E5B910;
        color: #04121b;
        font-weight: 700;
      }
      .voc-i18n-curr-badge {
        font-size: 10px;
        color: #E5B910;
        padding: 2px 6px;
        border-left: 1px solid rgba(255,255,255,0.15);
        margin-left: 4px;
      }
    `;
    document.head.appendChild(style);

    const bar = document.createElement('div');
    bar.className = 'voc-i18n-bar';
    ['pt', 'en', 'es'].forEach(lg => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'voc-i18n-btn' + (lg === currentLang ? ' is-active' : '');
      b.setAttribute('data-lang', lg);
      b.textContent = lg.toUpperCase();
      b.onclick = () => {
        currentLang = lg;
        localStorage.setItem('vocacao_lang', lg);
        applyLocalization();
      };
      bar.appendChild(b);
    });

    const currBadge = document.createElement('span');
    currBadge.className = 'voc-i18n-curr-badge';
    currBadge.textContent = MARKETS[currentCurrency].code;
    bar.appendChild(currBadge);

    // Inserir na navegação
    const nav = document.querySelector('.nav-inner') || document.querySelector('.pf-nav') || document.querySelector('.sw-topbar');
    if (nav) {
      const cta = nav.querySelector('.btn, .pf-nav-cta, .sw-topcta');
      if (cta) nav.insertBefore(bar, cta);
      else nav.appendChild(bar);
    }
  }

  function init() {
    injectBar();
    applyLocalization();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.VocacaoI18n = {
    setLanguage(l) { currentLang = l; applyLocalization(); },
    setMarket(c) { currentCurrency = c; applyLocalization(); },
    getState() { return { lang: currentLang, currency: currentCurrency }; }
  };
})();
