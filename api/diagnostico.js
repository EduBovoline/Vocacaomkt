/**
 * Vercel Serverless Function — /api/diagnostico
 * Recebe os dados do formulário diagnostico.html 24/7 na nuvem,
 * registra o pacote estruturado [VOCACAO-DB-INTAKE] em contato@vocacao.digital (Zoho SMTP TLS)
 * para sincronização automática com o banco local (Twenty CRM Postgres + SQLite + DeepSeek).
 */

const tls = require('tls');

const ZOHO_HOST = 'smtp.zoho.com';
const ZOHO_PORT = 465;
const ZOHO_USER = process.env.ZOHO_USER || 'contato@vocacao.digital';
const ZOHO_PASS = process.env.ZOHO_PASSWORD || 'HGA9SmwGmfhy';

function sendSmtpPacket(subject, htmlBody, jsonPayload) {
  return new Promise((resolve, reject) => {
    const socket = tls.connect(ZOHO_PORT, ZOHO_HOST, { rejectUnauthorized: false });
    let step = 0;
    const b64User = Buffer.from(ZOHO_USER).toString('base64');
    const b64Pass = Buffer.from(ZOHO_PASS).toString('base64');
    const b64Json = Buffer.from(JSON.stringify(jsonPayload), 'utf-8').toString('base64');

    const commands = [
      `EHLO vocacao.digital\r\n`,
      `AUTH LOGIN\r\n`,
      `${b64User}\r\n`,
      `${b64Pass}\r\n`,
      `MAIL FROM:<${ZOHO_USER}>\r\n`,
      `RCPT TO:<${ZOHO_USER}>\r\n`,
      `DATA\r\n`,
      [
        `From: "Vocacao Database Intake" <${ZOHO_USER}>`,
        `To: <${ZOHO_USER}>`,
        `Subject: =?UTF-8?B?${Buffer.from(subject).toString('base64')}?=`,
        `MIME-Version: 1.0`,
        `Content-Type: text/html; charset=UTF-8`,
        `X-Vocacao-Lead-Id: ${jsonPayload.lead_id || 'UNKNOWN'}`,
        ``,
        htmlBody,
        `<hr/><pre id="vocacao-db-payload" style="display:none;">VOCACAO_PAYLOAD_B64:${b64Json}:END_PAYLOAD</pre>`,
        `.\r\n`
      ].join('\r\n'),
      `QUIT\r\n`
    ];

    socket.setTimeout(12000, () => {
      socket.destroy();
      reject(new Error('SMTP timeout'));
    });

    socket.on('data', (data) => {
      const resp = data.toString();
      if (resp.startsWith('4') || resp.startsWith('5')) {
        socket.destroy();
        return reject(new Error('SMTP Error: ' + resp.trim()));
      }
      if (step < commands.length) {
        socket.write(commands[step]);
        step++;
      } else {
        socket.end();
        resolve(true);
      }
    });

    socket.on('error', (err) => reject(err));
  });
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }
  if (req.method !== 'POST') {
    return res.status(405).json({ status: 'error', message: 'Method not allowed' });
  }

  try {
    const payload = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
    const ans = payload.answers || {};
    const diag = payload.instant_diagnosis || {};
    const empresa = ans.empresa || 'Empresa Sem Nome';
    const leadId = payload.lead_id || ('VOC-' + Date.now());

    const subject = `[VOCACAO-DB-INTAKE] ${empresa} (${ans.phone || 'Sem WhatsApp'}) — ${leadId}`;
    const htmlBody = `
      <div style="font-family:sans-serif;max-width:640px;color:#0f172a;">
        <h2 style="color:#061B28;margin-bottom:4px;">Novo Diagnóstico Solicitado no Site</h2>
        <p style="margin-top:0;color:#475569;">Protocolo: <b>${leadId}</b> · Recebido em ${payload.submitted_at || new Date().toISOString()}</p>
        <table style="width:100%;border-collapse:collapse;margin:16px 0;">
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Empresa</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;"><b>${empresa}</b></td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Responsável</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;"><b>${ans.name || '-'}</b></td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">WhatsApp</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;"><b>${ans.phone || '-'}</b></td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">E-mail</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">${ans.email || '-'}</td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Setor / Tempo</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">${ans.segmento || '-'} (${ans.tempo || '-'})</td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Site Atual</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">${ans.site || '-'} (${ans.link_site || 'não informado'})</td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Google Maps</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">${ans.google || '-'} (${ans.link_google || 'não informado'})</td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Instagram</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">${ans.link_instagram || '-'} (${ans.redes || '-'})</td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Gargalo Principal</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;"><b>${ans.gargalo || '-'}</b></td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Oferta Recomendada</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;"><b>${diag.recTitle || '-'} (Score: ${diag.score || '-'}/100)</b></td></tr>
          <tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#64748b;">Consentimento LGPD</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Confirmado em ${payload.lgpd && payload.lgpd.timestamp}</td></tr>
        </table>
      </div>
    `;

    await sendSmtpPacket(subject, htmlBody, payload);
    return res.status(200).json({ status: 'ok', lead_id: leadId });
  } catch (err) {
    return res.status(200).json({ status: 'queued_fallback', error: err.message });
  }
};
