# 01 — Resumo Executivo: Auditoria da Máquina de Prospecção Vocação 2027

## 1. Visão Geral da Operação

A **Vocação Comunicação & Marketing** desenvolveu uma máquina híbrida de prospecção comercial B2B voltada para captação de clientes locais (clínicas, odontologia, pilates, terapias, marcenarias e comércios regionais em Sorocaba/SP). O ecossistema foi projetado para operar com foco na esteira oficial de serviços de presença digital:
- **Vocação Start (R$ 850)**: Otimização de Google Maps + Vitrine One-Page mobile em subdomínio seguro em 7 dias úteis.
- **Vocação Update (R$ 980)**: Modernização visual e mobile-first ultra-rápida (<0.5s) de sites legados em 5 dias úteis.
- **Presença Local no Google Maps (R$ 450)**: Blindagem, padronização e ranqueamento local no bairro.
- **Combo Maps + Tour 360° (R$ 950)**: Ficha de Google Maps integrada com fotos esféricas no Google Street View via câmera GoPro Max.

O objetivo do sistema era cobrir todo o ciclo: descoberta de leads, enriquecimento, qualificação por IA (Jev System One e Gemini), geração de relatórios gráficos de auditoria (PDF para o cliente e dossiê interno HTML no padrão Watanabe), abordagem semi-automatizada via WhatsApp (Evolution API) e e-mail B2B (Zoho Mail via SMTP), registro no CRM (Twenty CRM em PostgreSQL) e atendimento de respostas com um auto-responder webhook.

---

## 2. Diagnóstico Geral do Sistema

| Camada | Situação Observada | Diagnóstico Executivo |
| :--- | :--- | :--- |
| **Orquestração Docker** | Parcialmente Ativa / Fragmentada | 10 containers divididos em 2 stacks físicas distintas (`twenty-crm` no workspace e `local_stack` em `D:\Funnel vendas objeção\local_stack`). O container central `vocacao-auto-responder` está **parado (Exit Code 127)** por inconsistência de bind mount. |
| **CRM (Twenty CRM)** | 🟢 Operacional | Instância Twenty CRM (Postgres 16, Redis, Server e Worker) rodando na porta 3000 com dados reais estruturados. |
| **WhatsApp Engine (Evolution API)** | 🟢 Operacional | Evolution API v2 ativa na porta 8080 com banco Postgres e Redis próprios. |
| **Classificação por IA (Jev / Gemini)** | 🟡 Operacional com Divergência | Integração com `jev-latest` (TypeSafe System One) via API REST HTTP funciona, mas existem catálogos de ofertas conflitantes entre versões legadas e recentes. Chamadas Gemini Flash funcionam como fallback no auto-responder. |
| **Geração de Relatórios (HTML/PDF)** | 🟢 Operacional | Scripts Node.js (`generate_lead.js` e `convert_pdf.js`) geram dossiês e relatórios de alta qualidade técnica via Chrome Headless. |
| **Abordagem Comercial & Disparos** | 🔴 Falhas Críticas Conhecidas | Disparadores em lote sofreram com números fixos (sem WhatsApp), mensagens geradas com premissas falsas, jargões proibidos e corrupção de encoding UTF-8 / Windows-1252. |
| **E-mail B2B** | 🟡 Operacional com Alto Bounce | Disparos via Zoho Mail SMTP funcionando, porém com ~50% de bounces em testes com caixas genéricas (`contato@`) sem validação de MX. |

---

## 3. Origem dos Problemas Relatados

A auditoria identificou **5 causas-raiz** para as falhas e informações incorretas geradas pela máquina:

1. **Premissas Alucinadas/Generalizadas em Scripts Estáticos:**
   - Em vez de uma extração dinâmica confirmada para cada lead no momento da abordagem, os scripts de disparo em lote (`disparador_fila_santa_rosalia_brasilandia.py`, `disparador_fila_12leads_marcenarias.py`, etc.) utilizaram textos fixos que afirmavam categoricamente: *"sua empresa não tem fotos atualizadas nem canal direto de WhatsApp"* ou *"seu site usa @gmail.com"*. Quando o lead já possuía fotos ou canal de WhatsApp, a abordagem soava falsa e amadora.

2. **Corrupção de Codificação de Caracteres (Encoding UTF-8 / CP1252):**
   - No ambiente Windows, scripts Python manipulando strings e arquivos JSON sem normalização rígida de codificação geraram caracteres corrompidos gravados no histórico e enviados no WhatsApp (ex.: `Olǭ!`, `vocǦs`, `regiǜo`, `informaǜo`).

3. **Inconsistência de Rotas e Dependências de Caminhos Absolutos:**
   - Arquivos contêm caminhos absolutos legados que não existem no diretório atual (ex.: `C:\Vocação 2027\QG Vocação 2027 do zero\2 Leads`). Isso provocou o colapso do container `vocacao-auto-responder` ao reiniciar no Docker Desktop (Exit Code 127: mount source path not found).

4. **Falta de Filtragem Prévia de Telefonia Fixa:**
   - Dezenas de leads extraídos do Google Maps continham números fixos de 8 dígitos (ex.: DDD 15 + 3233-XXXX). Os disparadores tentavam enviar WhatsApp para linhas fixas, acumulando falhas na Evolution API.

5. **Divergência entre Regras de Negócio e Scripts Operacionais:**
   - O manual operacional proíbe categoricamente disparos no horário de almoço (11h45 às 14h15) e exige intervalos de 6 a 12 minutos. No entanto, scripts reais dispararam em intervalos de 30 segundos exatamente às 13:00, gerando alto risco de flag operacional.

---

## 4. Oportunidade de Reaproveitamento

O sistema **não necessita de reconstrução do zero**. As fundações técnicas essenciais são sólidas e de alto nível:
- O layout gráfico e o motor de geração de PDFs (`generate_lead.js` e `convert_pdf.js`) são visualmente impecáveis e geram relatórios de alto valor percebido.
- O pipeline de inserção no Twenty CRM via SQL (`sync_lead_twenty.py`) é completo, indexando notas, arquivos e oportunidades vinculadas.
- O classificador semântico Jev System One é extremamente ágil e determinístico.
- A stack Evolution API + Twenty CRM está ativa e funcional.
