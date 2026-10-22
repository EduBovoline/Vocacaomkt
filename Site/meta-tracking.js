/* ============================================
   VOCAÇÃO — Meta Pixel (Facebook/Instagram Ads) Tracking Central
   Segue o mesmo padrão do google-tracking.js:
   enquanto o ID for o de exemplo, NADA é carregado nem enviado.
   ============================================ */

(function () {
  'use strict';

  window.VOCACAO_META_CONFIG = window.VOCACAO_META_CONFIG || {
    // ID do Pixel da Meta (Vocação Pixel PLANO)
    pixelId: '1055819192507297'
  };

  var config = window.VOCACAO_META_CONFIG;
  var ativo = config.pixelId && config.pixelId !== 'XXXXXXXXXXXXXXX';

  if (!ativo) {
    return; // Pixel ainda não configurado: não carrega nada.
  }

  // Código base oficial do Pixel
  !function (f, b, e, v, n, t, s) {
    if (f.fbq) return; n = f.fbq = function () {
      n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
    };
    if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0';
    n.queue = []; t = b.createElement(e); t.async = !0;
    t.src = v; s = b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t, s);
  }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');

  fbq('init', config.pixelId);
  fbq('track', 'PageView');

  // Parâmetros de campanha (reaproveita o que o google-tracking.js já salvou)
  function getCampaignData() {
    try {
      var stored = sessionStorage.getItem('vocacao_utm_data');
      return stored ? JSON.parse(stored) : {};
    } catch (e) {
      return {};
    }
  }

  // Clique em qualquer botão de WhatsApp = evento "Contact" (padrão da Meta para conversa)
  document.addEventListener('click', function (e) {
    var alvo = e.target.closest('a[href*="wa.me"], a[href*="whatsapp.com"]');
    if (!alvo) return;

    var secao = alvo.closest('section') ? alvo.closest('section').id : 'global';
    var dados = getCampaignData();
    dados.content_name = window.location.pathname;
    dados.button_location = secao || 'global';

    fbq('track', 'Contact', dados);
  });

  // Conclusão do diagnóstico (formulário) = evento "Lead"
  window.trackMetaLead = function (leadData) {
    var dados = getCampaignData();
    if (leadData && leadData.segmento) dados.content_category = leadData.segmento;
    fbq('track', 'Lead', dados);
  };
})();
