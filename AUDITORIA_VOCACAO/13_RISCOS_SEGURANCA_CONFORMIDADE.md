# 13 — Análise de Riscos Técnicos, Segurança e Conformidade (LGPD)

## 1. Riscos de Conformidade com a LGPD (Lei 13.709/2018)

### Pontos Fortes Implementados:
- **Base Legal Declarada:** As mensagens de e-mail e WhatsApp fundamentam o contato no Art. 7º, IX da LGPD (Legítimo Interesse Comercial B2B entre pessoas jurídicas).
- **Mecanismo de Opt-Out Simples e Funcional:** A presença da instrução *"responda PARAR"* e o processamento automático via webhook com registro em `optout_leads.json` atende ao princípio de autodeterminação informativa do titular.
- **Origem dos Dados Públicos:** Dados obtidos a partir de perfis manifestamente públicos de empresas (fichas no Google Maps e sites institucionais).

### Riscos de Privacidade Identificados:
- **Armazenamento de Dados em Arquivos de Texto Sem Criptografia:** Números de telefone e nomes de contatos foram gravados em formato JSON em texto claro no disco (`chat_history.json`, `leads_catalog_global.json`, `leads_ouro_fila_disparo.json`).
- **Possibilidade de Contato com Dados Pessoais de Profissionais Liberais:** Médicos, psicólogos e dentistas frequentemente utilizam linhas que misturam pessoa física e jurídica. Contatos com pessoa física exigem maior rigor na comprovação de legítimo interesse ou consentimento prévio.

---

## 2. Riscos de Plataforma e Bloqueio Operacional

### A. Risco Crítico no WhatsApp (Termos de Serviço da Meta):
- **Uso de API Não Oficial (Baileys via Evolution API):**
  - A Meta proíbe o envio não autorizado de mensagens em massa através de bibliotecas de emulação de navegador.
  - **Fatores Agravantes Observados nos Scripts:** Disparos realizados com intervalos reduzidos (30 a 60 segundos) e em horários de pico/almoço geram risco imediato de banimento irreversível da linha telefônica comercial.

### B. Risco no Zoho Mail (Termos de Uso e Reputação de Domínio):
- O envio de e-mails em lote para bases não higienizadas com taxa de bounce de 50% pode resultar em:
  1. Suspensão da conta Zoho Mail por violação da política anti-spam.
  2. Inclusão do domínio `vocacao.digital` em blocklists públicas (DNSBL), impedindo que e-mails legítimos de clientes cheguem à caixa de entrada.

---

## 3. Riscos de Segurança da Informação e Gestão de Credenciais

### A. Credenciais Hardcoded no Código:
- **Evidência Encontrada:** Diversos scripts continham senhas de banco de dados, chaves de API e senhas de e-mail codificadas diretamente no corpo do código Python (`enviar_email_zoho.py`, `jev_engine.py`, `auto_responder_docker/docker-compose.yml`, `D:\Funnel vendas objeção\local_stack\docker-compose.yml`).
- **Recomendação:** Todas as credenciais devem ser migradas estritamente para arquivos `.env` protegidos pelo `.gitignore` e injetadas via variáveis de ambiente de runtime.

### B. Exposição de Portas sem Autenticação Robusta:
- A Evolution API expõe na porta `8080` rotas de leitura de mensagens e envio autenticadas apenas por uma API key estática compartilhada em múltiplos arquivos.
- O Sub-CRM expõe na porta `5680` e `8000` um painel administrativo com botões de disparo sem camada de login/sessão. Caso essas portas fossem expostas além do `localhost`, qualquer usuário da rede local poderia disparar mensagens.

---

## 4. Matriz de Risco Sintética

| Risco | Probabilidade | Impacto | Classificação | Mitigação Obrigatória |
| :--- | :---: | :---: | :---: | :--- |
| **Banimento do chip WhatsApp pela Meta** | Alta | Crítico | 🔴 Extremo | Respeitar rigorosamente timers de 6 a 12 min e usar warm-up multi-chip. |
| **Bloqueio do domínio no Zoho Mail** | Média | Alto | 🔴 Alto | Adicionar validação de DNS MX e suspender listas frias sem checagem. |
| **Vazamento de credenciais em versionamento**| Média | Alto | 🔴 Alto | Eliminar senhas hardcoded e usar sanitização no git. |
| **Processamento nulo de webhooks por queda de container** | Confirmado | Alto | 🟠 Crítico | Corrigir caminhos de bind mount no Docker Compose. |
