import os
import sys

sys.path.append(r"C:\Vocação 2027\QG Vocação 2027 do zero")
from enviar_email_zoho import send_email

BASE_DIR = r"C:\Vocação 2027\QG Vocação 2027 do zero\2 Leads\Jardim Vivo Essencial"
PDF_PROPOSTA = os.path.join(BASE_DIR, "Proposta-Comercial-Jardim-Vivo-Essencial.pdf")

DESTINATARIO = "andrerhandrade@gmail.com"
ASSUNTO = "Proposta — Jardim Vivo Essencial"
LINK_PAGAMENTO = "https://link.infinitepay.io/edu_bovoline/VC1DLUMtUg-r08gVw7sFi-980,00"

EMAIL_HTML = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
</head>
<body style="margin: 0; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 1.6; color: #1a1a1a;">

<p>Fala, André!</p>

<p>Segue a proposta em anexo no PDF (R$ 980, entrega em 5 dias úteis e o site rodando direto na sua Vercel, sem mensalidade).</p>

<p>Como você falou do parcelamento, o link já está liberado em até 12x no cartão:</p>

<p style="margin: 20px 0;">
  👉 <a href="{LINK_PAGAMENTO}" style="color: #0B5E47; font-weight: bold; font-size: 16px; text-decoration: underline;">{LINK_PAGAMENTO}</a>
</p>

<p>Qualquer dúvida me chama no WhatsApp.</p>

<p style="margin-top: 24px;">
  Abraço,<br>
  <b>Eduardo Bovoline</b><br>
  <span style="color: #666; font-size: 13px;">Vocação Comunicação & Marketing</span>
</p>

</body>
</html>
"""

def execute_send():
    if not os.path.exists(PDF_PROPOSTA):
        print(f"[!] Erro: Arquivo PDF não encontrado: {PDF_PROPOSTA}")
        return False

    print(f"📧 Disparando e-mail anti-slop para {DESTINATARIO} com o PDF anexo...")
    success = send_email(
        to_email=DESTINATARIO,
        subject=ASSUNTO,
        body_html=EMAIL_HTML,
        attachment_path=PDF_PROPOSTA,
        sender_name="Eduardo Bovoline | Vocação"
    )
    if success:
        print("[✓] E-mail entregue com sucesso via Zoho Mail!")
    else:
        print("[!] Falha no envio do e-mail.")
    return success

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--send":
        execute_send()
    else:
        print("Script preparado! Para enviar, execute com --send.")
