# Arquitetura Técnica & Estrutura de Custos — Infraestrutura Digital Vocação

**Objetivo:** Padronizar a entrega técnica de Landing Page, Rastreamento Avançado (Meta CAPI) e Automação de Checkout/Pix para aplicar tanto na **Vocação Digital** quanto na proposta comercial do **André (Jardim Vivo Essencial)**.

---

## 1. A Estrutura Técnica Ponta a Ponta (Stack Enxuta)

```
[ Visitante ] ──> [ Domínio Próprio + Cloudflare SSL/DNS ]
                         │
                         ▼
             [ Landing Page Estática / Vercel ]
             (Velocidade 99/100, Custo R$ 0)
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
[ Meta Pixel Web ]               [ Botão Compra / Checkout Hotmart ]
        │                                 │
        │                        (Evento: Iniciação de Checkout / Compra)
        │                                 │
        ▼                                 ▼
[ Hotmart Webhook Nativo ] ──> [ Webhook Receiver / n8n ou Script Python ]
                                          │
                               ┌──────────┴──────────┐
                               ▼                     ▼
                       [ Meta CAPI ]       [ Evolution API (WhatsApp) ]
                   (Conversions API)       - Alerta Pix Pendente (15 min)
                   (Rastreamento 100%)     - Recuperação de Carrinho
```

---

## 2. Componentes Técnicos & Como Funciona

| Componente | Ferramenta Recomendada | Como Funciona na Prática |
| :--- | :--- | :--- |
| **1. Domínio & DNS** | Registro.br + Cloudflare (Free) | Domínio próprio registrado (ex: `jardimvivoessencial.com.br`). Cloudflare provê CDN global, SSL gratuito e proteção DDoS. |
| **2. Hospedagem da LP** | Vercel ou Cloudflare Pages (Free) | Hospedagem estática de ultravelocidade (HTML/Tailwind ou Astro/Next). Carregamento abaixo de 1 segundo (aumenta conversão em 40% vs WordPress lento). Custo: R$ 0. |
| **3. Rastreamento (Pixel + CAPI)** | Hotmart Nativo + Cloudflare Zaraz / Meta CAPI | A própria Hotmart possui integração nativa com o Meta Pixel e API de Conversões (CAPI) para eventos de checkout e compra aprovada, sem necessidade de servidor pago de GTM. |
| **4. Recuperação de Pix & Carrinho** | Webhook Hotmart + Evolution API (WhatsApp) | Quando a Hotmart dispara evento `PURCHASE_OUT_OF_DATE` (Pix expirando) ou `CART_ABANDONMENT`, o script/n8n envia mensagem cordial no WhatsApp do lead com o código Pix e link direto. |

---

## 3. Planilha de Custos Reais da Infraestrutura (Custo Operacional)

### Cenário A: Custos Fixos de Ferramentas (Stack Enxuta Vocação)

| Item | Custo Mensal (R$) | Custo Anual (R$) | Quem Paga? |
| :--- | :--- | :--- | :--- |
| **Domínio .com.br** | R$ 0 | R$ 40,00 | Cliente (André) |
| **Hospedagem LP (Vercel / Cloudflare)** | R$ 0 | R$ 0 (Plano Free cobre até 100k visitas) | Gratuito |
| **DNS / SSL / CDN (Cloudflare)** | R$ 0 | R$ 0 (Plano Free) | Gratuito |
| **Meta CAPI (Via Hotmart Nativa)** | R$ 0 | R$ 0 (Recurso nativo Hotmart) | Gratuito |
| **Evolution API / Automação WhatsApp** | R$ 0 a R$ 30,00/mês | R$ 0 (Se rodar na VPS Vocação já existente) | Vocação |
| **TOTAL DE CUSTO FIXO TÉCNICO** | **~R$ 0 a R$ 30,00/mês** | **R$ 40,00/ano (apenas domínio)** | **Margem de lucro > 95%** |

---

## 4. Estrutura da Proposta Comercial para o André (3 Pilares Solicitados)

Como o custo de infraestrutura é quase nulo utilizando a stack moderna (Cloudflare + Vercel + Hotmart CAPI), o valor cobrado é **puro serviço especializado de alta entrega**.

### Pilar 1: Produção de Conteúdo & Ativos (Setup Único)
- Redação da Copy da nova Landing Page (baseada nas dores reais do quiz: "matei todas as plantas", falta de tempo).
- Design profissional da LP com identidade visual moderna do Jardim Vivo.
- Pacote de 4 criativos estáticos + 2 roteiros de vídeo para anúncios Meta Ads.
- **Faixa de Mercado / Sugestão Vocação:** **R$ 1.500 a R$ 2.200 (Taxa única)**.

### Pilar 2: Gestão da Operação & Infraestrutura (Mensalidade / Retainer)
- Configuração do domínio próprio e hospedagem ultraveloz na Vercel/Cloudflare.
- Parametrização do Meta Pixel + CAPI nativo na Hotmart (rastreamento seguro pós-iOS 14).
- Setup da esteira de recuperação ativa de Pix e Boletos no WhatsApp.
- Gestão e otimização semanal das campanhas de tráfego (Meta Ads).
- **Faixa de Mercado / Sugestão Vocação:** **R$ 1.200 a R$ 1.800/mês**.

### Pilar 3: Verba de Mídia Paga (Meta Ads)
- Paga diretamente pelo André via cartão de crédito na conta de anúncios da Meta dele.
- Sugestão de validação inicial: R$ 20 a R$ 30/dia (R$ 600 a R$ 900/mês).
- **Custo para a Vocação:** R$ 0.

---

## 5. Implementação Imediata na Própria Vocação (Dogfooding)
Para que a Vocação também tenha essa infraestrutura 100% ativa em seu próprio site:
1. **Configurar Cloudflare no `vocacao.digital`** (já hospedado na Vercel).
2. **Ativar o Meta Pixel + CAPI no site da Vocação**.
3. **Conectar os formulários do site diretamente ao Twenty CRM e à Evolution API (WhatsApp)** para recepção instantânea de leads.
