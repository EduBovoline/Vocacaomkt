# 06 — WhatsApp, E-mail e Mecanismos de Cadência

## 1. Módulo WhatsApp: Evolution API

### Arquitetura e Integração
- **Tecnologia:** Evolution API v2 (open-source WhatsApp integration baseada em Node.js e Baileys).
- **Container:** `vocacao-evolution-api` rodando na porta 8080.
- **Persistência:** PostgreSQL dedicado (`vocacao-postgres-evolution`) e Redis (`vocacao-redis-evolution`) para sessões e mensagens.
- **Tipo de Conexão:** Não-oficial (emulação de cliente web via QR Code).
- **Instância Comercial:** `vocacao_comercial`.
- **Autenticação:** Header HTTP `apikey: [REDACTED_API_KEY]` na rota `http://localhost:8080` (ou `http://vocacao-evolution-api:8080` dentro da rede Docker).

### Política Oficial vs. Comportamento Real dos Disparos

| Parâmetro | Regra Oficial no Manual (`CONFIG_MOTOR...`) | Prática Observada nos Scripts |
| :--- | :--- | :--- |
| **Teto Diário por Linha** | 15 disparos/dia (warm-up) e teto de 20 | Scripts rodaram lotes de até 100 leads na fila |
| **Intervalo entre Envios** | Randômico de 6 a 12 minutos (360 a 720 segundos) | Registros em `dispatch_logs.json` mostram envios a cada **30 a 60 segundos** |
| **Pausa de Bloco** | 25 a 35 minutos a cada 4 envios | Ausente na maioria dos scripts batch simples |
| **Janelas Estratégicas** | Manhã (10h-11h45) e Tarde (14h15-16h45) | Disparos reais registrados às **13:01 a 13:05** (Horário de Almoço / Blackout) |
| **Bloqueio em Fim de Semana**| 100% congelado | Respeitado via `is_within_commercial_window()` |

### Prevenção de Bloqueio Meta e Circuit Breaker
- **Regra Teórica:** Se qualquer mensagem falhar por erro de entrega ou receber aviso de spam, o motor congela e trava 100% dos disparos.
- **Implementação Real:** Não há circuito automático de desligamento da Evolution API em caso de ban temporário; a trava é dependente da interrupção do loop no Python.

### Mecanismos de Opt-out e LGPD no WhatsApp
- Todas as mensagens oficiais incluem a cláusula: *"Se preferir não receber mensagens comerciais, responda PARAR"*.
- O auto-responder monitora termos de cancelamento (`PARAR`, `DESCADASTRAR`, `NÃO QUERO`, `CANCELAR`).
- Ao detectar o gatilho, responde educadamente confirmando a exclusão, grava o número em `optout_leads.json` e atualiza a nota da empresa no Twenty CRM.

---

## 2. Módulo E-mail: Zoho Mail SMTP

### Infraestrutura e Configuração
- **Provedor:** Zoho Mail Corporativo.
- **Servidor SMTP:** `smtp.zoho.com` na porta `465` (SSL/TLS).
- **Conta Remetente:** `contato@vocacao.digital` (Eduardo Bovoline).
- **Script Responsável:** `operacoes/enviar_email_zoho.py` e `operacoes/disparador_email_b2b.py`.

### Regras de Envio e Cadência
- **Volume Planejado:** 30 a 50 e-mails por dia.
- **Intervalo:** Randômico de 20 a 45 segundos por envio.
- **Formato:** HTML responsivo com cabeçalho limpo, dados do negócio e rodapé de conformidade com o Art. 7º, IX da LGPD (Legítimo Interesse B2B).
- **Trava de Integridade de Anexo:** O sistema bloqueia expressamente o envio caso o arquivo PDF de diagnóstico não exista em disco, evitando prometer um anexo que não foi gerado.

### Desempenho e Taxa de Rejeição (Bounce Rate)
- **Evidência em Disco:** Arquivo `operacoes/bounced_emails.json` e `operacoes/delivered_emails.json`.
- **Diagnóstico:** Em uma bateria de teste com 10 garagens e lojas de seminovos, **5 e-mails sofreram bounce** (`contato@allusveiculos.com.br`, `contato@omegaveiculos.net`, `contato@nexmotors.com.br`, `contato@gcveiculos.com.br`, `contato@ksmotors.com.br`).
- **Causa:** Uso de e-mails sintéticos ou obsoletos sem validação prévia de registros MX e caixa postal ativa. Uma taxa de bounce de 50% coloca o domínio `vocacao.digital` sob alto risco de inclusão em listas negras de spam (Spamhaus, Barracuda).

---

## 3. Gestão de Contatos e Controle de Duplicidade

O sistema possui uma camada anti-duplicidade em 4 níveis (implementada em `auto_responder_docker/main.py`, função `is_lead_strictly_virgin()`):
1. **Histórico Consolidado:** Consulta `historico_absoluto_contatados.json` por nome e pelos últimos 8 dígitos do telefone.
2. **Twenty CRM & Mapeamento Direto:** Verifica se o número consta no banco Postgres ou no dicionário `DIRECT_MAP`.
3. **Listas de Estado:** Verifica se já foi entregue (`delivered_leads.json`), rejeitado (`optout_leads.json`) ou contatado na fila atual (`fila_ouro_progresso.json`).
4. **Verificação na Evolution API:** Consulta o endpoint `/chat/findMessages` da Evolution API para certificar-se de que não existem mensagens prévias trocadas no WhatsApp com o número nos últimos dias.
