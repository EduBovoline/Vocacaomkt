/* ============================================
   VOCAÇÃO — Google Analytics 4 & Google Ads Tracking Central
   ============================================ */

(function () {
  'use strict';

  // Configurações do Google (Substitua pelos seus IDs reais quando disponíveis)
  window.VOCACAO_TRACKING_CONFIG = window.VOCACAO_TRACKING_CONFIG || {
    // ID do Google Analytics 4 (Ex: 'G-XXXXXXXXXX')
    ga4Id: 'G-XXXXXXXXXX',

    // ID de Conversão do Google Ads (Ex: 'AW-XXXXXXXXXX')
    googleAdsId: 'AW-XXXXXXXXXX',

    // Rótulo da Conversão de WhatsApp no Google Ads (Ex: 'AW-123456789/WhatsAppClickLabel')
    whatsappConversionLabel: '',

    // Rótulo da Conversão do Diagnóstico (Lead) no Google Ads (Ex: 'AW-123456789/LeadFormLabel')
    leadConversionLabel: ''
  };

  const config = window.VOCACAO_TRACKING_CONFIG;

  // Inicializa dataLayer e gtag
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = gtag;

  gtag('js', new Date());

  // Configura GA4 se informado ID válido
  if (config.ga4Id && config.ga4Id !== 'G-XXXXXXXXXX') {
    const scriptGA4 = document.createElement('script');
    scriptGA4.async = true;
    scriptGA4.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(config.ga4Id);
    document.head.appendChild(scriptGA4);

    gtag('config', config.ga4Id, {
      send_page_view: true,
      anonymize_ip: true
    });
  }

  // Configura Google Ads se informado ID válido
  if (config.googleAdsId && config.googleAdsId !== 'AW-XXXXXXXXXX') {
    if (!config.ga4Id || config.ga4Id === 'G-XXXXXXXXXX') {
      const scriptAds = document.createElement('script');
      scriptAds.async = true;
      scriptAds.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(config.googleAdsId);
      document.head.appendChild(scriptAds);
    }
    gtag('config', config.googleAdsId);
  }

  // Captura Parâmetros de UTM e GCLID da URL para persistência
  function captureCampaignParams() {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const paramsToSave = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'wbraid', 'gbraid'];
      const campaignData = {};

      paramsToSave.forEach(param => {
        if (urlParams.has(param)) {
          campaignData[param] = urlParams.get(param);
        }
      });

      if (Object.keys(campaignData).length > 0) {
        sessionStorage.setItem('vocacao_utm_data', JSON.stringify(campaignData));
      }
    } catch (e) {
      console.warn('[Vocação Tracking] Erro ao capturar parâmetros de campanha:', e);
    }
  }

  captureCampaignParams();

  // Função utilitária para obter parâmetros salvos
  function getCampaignData() {
    try {
      const stored = sessionStorage.getItem('vocacao_utm_data');
      return stored ? JSON.parse(stored) : {};
    } catch (e) {
      return {};
    }
  }

  // Tracking de Clique no WhatsApp
  window.trackWhatsAppClick = function (locationLabel) {
    const label = locationLabel || window.location.pathname;
    const campaignData = getCampaignData();

    // Evento GA4
    gtag('event', 'click_whatsapp', {
      event_category: 'Engagement',
      event_label: label,
      page_path: window.location.pathname,
      ...campaignData
    });

    // Conversão Google Ads
    if (config.whatsappConversionLabel) {
      gtag('event', 'conversion', {
        send_to: config.whatsappConversionLabel,
        value: 1.0,
        currency: 'BRL'
      });
    }

    console.log('[Vocação Tracking] WhatsApp click enviado:', label);
  };

  // Tracking de Conclusão do Diagnóstico (Lead Form)
  window.trackDiagnosticConversion = function (leadData) {
    const campaignData = getCampaignData();

    // Evento GA4
    gtag('event', 'generate_lead', {
      event_category: 'Diagnostic',
      event_label: leadData ? leadData.empresa || 'Empresa Sem Nome' : 'Diagnóstico Concluído',
      setor: leadData ? leadData.segmento : undefined,
      gargalo: leadData ? leadData.gargalo : undefined,
      page_path: window.location.pathname,
      ...campaignData
    });

    // Conversão Google Ads
    if (config.leadConversionLabel) {
      gtag('event', 'conversion', {
        send_to: config.leadConversionLabel,
        value: 5.0,
        currency: 'BRL'
      });
    }

    console.log('[Vocação Tracking] Diagnóstico concluído e enviado:', leadData);
  };

  // Intercepta cliques em botões do WhatsApp automaticamente em toda a página
  document.addEventListener('click', function (e) {
    const target = e.target.closest('a[href*="wa.me"], a[href*="whatsapp.com"]');
    if (target) {
      const section = target.closest('section') ? target.closest('section').id : 'global';
      window.trackWhatsAppClick(section || target.textContent.trim());
    }
  });

})();
