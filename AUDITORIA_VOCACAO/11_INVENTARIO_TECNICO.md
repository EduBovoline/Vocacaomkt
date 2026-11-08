# 11 — Inventário Técnico de Arquivos, Serviços e Repositórios

## 1. Diretórios e Repositórios Relacionados

| Localização Física | Papel no Ecossistema | Tecnologias Presentes |
| :--- | :--- | :--- |
| `C:\Users\edubo\.gemini\antigravity\worktrees\QG Vocação 2027 do zero\audit_prospecting_system_vocacao` | Workspace atual e repositório central | Node.js, Python, Docker Compose, HTML/CSS |
| `C:\Users\edubo\.gemini\config\plugins\vocacao\` | Plugin oficial da Vocação no assistente Antigravity | Skills, scripts de automação, referências de brand |
| `D:\Funnel vendas objeção\local_stack\` | Stack Docker da Evolution API, n8n, Postgres e Redis | Docker Compose v5, Baileys, n8n workflows |
| `C:\Antigravity projects\Vocação 2027\` | Repositório legado de assets e histórico | Portfólio, casos e prospects Watanabe originais |

---

## 2. Inventário de Arquivos Chave por Camada

### A. Operações & Scripts (`operacoes/`)
- `auto_responder.py` (45.016 bytes): Webhook HTTP local (porta 5680), parser de intenção positiva, entrega de PDF e envio de e-mails Zoho.
- `CONFIG_MOTOR_DISPARO_VOCACOES_START.py` (5.527 bytes): Regras de negócio, janelas de máxima conversão (Golden Windows) e opt-out LGPD.
- `enviar_email_zoho.py` (2.368 bytes): Módulo SMTP autenticado via Zoho Mail (`smtp.zoho.com:465`).
- `disparador_email_b2b.py` (5.986 bytes): Fila de prospecção fria B2B com intervalo randômico de 20s a 45s.
- `disparador_fila_20leads_pilates.py` (14.559 bytes): Fila dedicada de 20 studios de pilates e clínicas posturais da Zona Sul.
- `disparador_fila_12leads_marcenarias.py` (8.546 bytes): Fila de marcenarias de alto ticket de Sorocaba.
- `disparador_fila_santa_rosalia_brasilandia.py` (61.372 bytes): Fila de 100 estabelecimentos comerciais dos bairros Santa Rosália e Jardim Brasilândia.
- `build_ultimate_subcrm.py` (49.556 bytes): Gerador de interface visual para o Sub-CRM executivo.
- `INICIAR_TODAS_FERRAMENTAS.bat` (1.524 bytes): Script batch de inicialização unificada dos containers e do auto-responder.
- `PARAR_TODAS_FERRAMENTAS.bat` (1.093 bytes): Script batch de congelamento ordenado de todos os serviços.

### B. Módulo Dockerizado do Auto-Responder (`operacoes/auto_responder_docker/`)
- `main.py` (79.271 bytes): Servidor HTTP completo com Sub-CRM web, webhook Evolution API, despacho em background e integração Twenty CRM.
- `docker-compose.yml` (1.060 bytes): Configuração do container `vocacao-auto-responder` com redes `local_stack_default` e `twenty_default`.
- `Dockerfile` (340 bytes): Build Python 3.11 com dependências do auto-responder.
- `jev_engine.py` (5.907 bytes): Cliente HTTP para qualificação semântica via API TypeSafe System One.
- `gemini_classifier.py` (5.317 bytes): Classificador conversacional com modelos Gemini Flash e prompt de escuta ativa.
- `crm_db.py` (7.683 bytes): Funções de consulta e atualização do Twenty CRM PostgreSQL.
- `enviar_email.py` (1.711 bytes): Utilitário de disparo de mensagens por e-mail com anexo.
- `esteira_followup_valor.py` (7.617 bytes): Lógica de follow-up pós-entrega de diagnóstico.

### C. Plugin Vocação (`plugins/vocacao/skills/`)
- `vocacao-prospeccao/scripts/generate_lead.js` (34.020 bytes): Compilador HTML do kit de vendas (Relatório do Cliente e Dossiê Interno Watanabe).
- `vocacao-prospeccao/scripts/convert_pdf.js` (890 bytes): Conversor para PDF via Chrome Headless.
- `vocacao-prospeccao/scripts/sync_lead_twenty.py` (10.020 bytes): Sincronizador PostgreSQL do Twenty CRM.
- `vocacao-prospeccao/scripts/jev_classifier.py` (3.240 bytes): Classificador Jev versão CLI.
- `vocacao-prospeccao/scripts/resolve_maps.js` (1.200 bytes): Expansor de URLs curtas e extrator de geolocalização.

---

## 3. Serviços de Rede e Portas Alocadas

| Porta | Protocolo | Serviço | Host / Container |
| :--- | :--- | :--- | :--- |
| `3000` | HTTP | Twenty CRM (Web UI / API) | `twenty-server-1` |
| `5000` | HTTP | SerpBear (Rank Tracker) | `serpbear-serpbear-1` |
| `5432` | TCP | PostgreSQL 16 (Twenty DB) | `twenty-db-1` |
| `5678` | HTTP | n8n Workflow Automation | `vocacao-n8n` |
| `5680` | HTTP | Auto-Responder / Webhook | Host local ou `vocacao-auto-responder` |
| `6379` | TCP | Redis (Cache Twenty / Evolution) | `twenty-redis-1` / `vocacao-redis-evolution` |
| `8000` | HTTP | Sub-CRM Web Cockpit | `vocacao-auto-responder` |
| `8080` | HTTP | Evolution API (WhatsApp Engine) | `vocacao-evolution-api` |

---

## 4. Variáveis de Ambiente e Configuração (Sanitizadas)

| Variável | Finalidade | Valor de Referência (Sanitizado) |
| :--- | :--- | :--- |
| `EVOLUTION_API_URL` | URL do servidor WhatsApp | `http://localhost:8080` ou `http://vocacao-evolution-api:8080` |
| `INSTANCE_NAME` | Nome da sessão WhatsApp | `vocacao_comercial` |
| `API_KEY` | Chave de segurança Evolution API | `[REDACTED_API_KEY]` |
| `ADMIN_WHATSAPP` | Linha do gestor comercial | `5515981512083` |
| `TYPESAFE_API_KEY` | Autenticação Jev System One | `[REDACTED_TYPESAFE_KEY]` |
| `GEMINI_API_KEY` | Autenticação Google Gemini API | `[REDACTED_GEMINI_KEY]` |
| `ZOHO_USER` | E-mail remetente SMTP | `contato@vocacao.digital` |
| `ZOHO_PASSWORD` | Senha de aplicativo Zoho | `[REDACTED_ZOHO_PASSWORD]` |
| `POSTGRES_CRM_HOST`| Endereço do banco CRM | `twenty-db-1` ou `localhost` |
| `POSTGRES_CRM_USER`| Usuário do banco CRM | `postgres` |
| `POSTGRES_CRM_DB` | Nome do banco Twenty | `twenty` |
| `SCHEMA` | Schema da workspace Twenty | `workspace_2xmx8hech9nybwidia3404k2z` |
