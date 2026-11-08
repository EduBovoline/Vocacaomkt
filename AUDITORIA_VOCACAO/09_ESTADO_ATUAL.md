# 09 — Estado Atual dos Componentes e Recursos Operacionais

## 1. Classificação Rigorosa dos Componentes

Seguindo a taxonomia obrigatória de auditoria:

| Componente | Classificação | Evidência / Localização | Justificativa |
| :--- | :--- | :--- | :--- |
| **Twenty CRM (Server, Worker, DB, Redis)** | 🟢 Operacional e confirmado | Containers `twenty-server-1`, `twenty-worker-1`, `twenty-db-1`, `twenty-redis-1` em execução e saudáveis na porta 3000. | Responde requisições HTTP e comandos PSQL. |
| **Evolution API v2 (WhatsApp Engine)** | 🟢 Operacional e confirmado | Container `vocacao-evolution-api` Up há 3 horas na porta 8080. | Banco Postgres e Redis da Evolution ativos e sincronizados. |
| **Classificador Jev System One** | 🟢 Operacional e confirmado | `jev_engine.py` e `jev_classifier.py` conectando à API TypeSafe System One. | Respostas determinísticas em `choice`, `noul` e `score`. |
| **Motor de Geração de PDFs (Watanabe)** | 🟢 Operacional e confirmado | `generate_lead.js` e `convert_pdf.js`. | Produz relatórios A4 em PDF via Chrome Headless com validação >= 50KB. |
| **Sincronizador Twenty CRM (SQL)** | 🟢 Operacional e confirmado | `sync_lead_twenty.py`. | Cria registros de Company, Person, Opportunity, Note e indexa arquivos em `core.file`. |
| **Envio de E-mail via Zoho SMTP** | 🟢 Operacional e confirmado | `enviar_email_zoho.py`. | Conexão SSL na porta 465 com credenciais configuradas. |
| **Orquestrador n8n** | 🟡 Implementado, mas não testado | Container `vocacao-n8n` Up na porta 5678 com workflow importado. | Não foram disparadas automações n8n ativas nesta auditoria. |
| **SerpBear (Rank Tracker SEO)** | 🟡 Implementado, mas não testado | Container `serpbear-serpbear-1` Up na porta 5000. | Interface operacional, sem consultas ativas submetidas durante a auditoria. |
| **Motor de Cadência Segura com Janelas** | 🟠 Parcialmente implementado | `CONFIG_MOTOR_DISPARO_VOCACOES_START.py`. | As regras foram codificadas, mas os disparadores batch não herdavam a trava de forma uniforme. |
| **Painel Sub-CRM em Tempo Real** | 🔴 Com falha conhecida | `auto_responder_docker/main.py` e porta 5680. | Inacessível porque o container Docker correspondente está em erro de mount (Exit 127). |
| **Disparadores Batch em Lote** | 🔴 Com falha conhecida | `disparador_fila_*.py`. | Falhas documentadas por envio para linhas fixas e corrupção de acentuação no Windows. |
| **Crawler Contínuo de Google Maps** | ⚪ Não localizado | Varredura em todo o repositório por Playwright/Puppeteer/Selenium para scraping contínuo. | As listas foram extraídas pontualmente ou importadas de CSVs estáticos. |
| **OpenSEO** | ⚫ Desativado | `openseo/docker-compose.yml`. | Container não está listado em execução no `docker ps`. |

---

## 2. Recursos Valiosos que Devem Ser Preservados

1. **Design System & Template Visual Watanabe (`generate_lead.js`):**
   - A diagramação editorial com tipografia Fraunces + DM Sans, header curvo em Dark Navy (`#061B28`) e Dourado Solar (`#E5B910`), grid de pilares e cards comparativos possui altíssimo valor percebido e deve ser mantida integralmente.
2. **Pipeline de Injeção Direta no Twenty CRM (`sync_lead_twenty.py`):**
   - A lógica de indexação direta em PostgreSQL contornando APIs lentas é extremamente performática, eficiente e estável.
3. **Julgamento Semântico com Jev (`jev_engine.py`):**
   - A categorização matemática de maturidade digital e cálculo de perda de conversão local elimina alucinações de LLMs tradicionais e consome frações de segundo.
4. **Mecanismo de Renderização PDF Headless (`convert_pdf.js`):**
   - A utilização do Chrome nativo do sistema operacional (`--headless=new --print-to-pdf`) dispensa dependências pesadas de Puppeteer no Node.js.
5. **Tratamento de Opt-Out LGPD:**
   - A captura automática de termos de descadastramento com resposta educada imediata e gravação em lista negra permanente garante conformidade jurídica sólida.
