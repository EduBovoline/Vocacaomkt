# 08 — Histórico de Erros, Falhas Operacionais e Estabilidade

## 1. Classificação Geral dos Problemas

A auditoria separou os problemas documentados no histórico em três categorias cronológicas e operacionais:
1. **Problemas Históricos Já Superados:** Falhas encontradas nas primeiras versões que foram contornadas por revisões posteriores de código.
2. **Problemas Ativos / Abertos:** Defeitos arquiteturais e operacionais que persistem no estado atual dos arquivos.
3. **Riscos Estruturais (Pontos Únicos de Falha):** Vulnerabilidades que ameaçam a continuidade da máquina caso ela seja reativada sem ajustes.

---

## 2. Problemas Históricos Já Corrigidos

| Falha Identificada | Evidência / Módulo | Como foi Contornada no Código |
| :--- | :--- | :--- |
| **Envio para Telefones Fixos** | Registros em `dispatch_logs.json` descartando números como `551532331516` | Criação da função `is_mobile_phone()` em `auto_responder_docker/main.py` (linhas 206-220) para exigir o 9º dígito. |
| **Loop Infinito com Bots de Recepção** | Respostas duplicadas para mensagens de auto-resposta no WhatsApp | Implementação da função `handle_bot_bypass()` com trava `is_already_bypassed()` gravada em `bypassed_leads.json`. |
| **Gatilhos Fracos de Intenção Positiva** | Respostas automáticas enviando PDF quando o cliente dizia apenas "ok" ou "beleza" | Remoção de termos ambíguos de `POSITIVE_TRIGGERS` (permanecendo apenas termos explícitos como "pode mandar", "sim", "quero ver"). |
| **Disparo de E-mail Sem PDF Anexado** | Promessa de diagnóstico por e-mail quando o arquivo ainda não havia sido gerado em disco | Criação da "Trava de Integridade de Anexo" em `auto_responder.py` (linhas 510-520), abortando o disparo se o PDF não for validado fisicamente. |

---

## 3. Problemas Ativos e Abertos no Momento da Auditoria

### A. Queda do Container `vocacao-auto-responder` (Exit 127)
- **Status:** Aberto.
- **Evidência:** `docker ps -a` relata status `Exited (127)` e `docker inspect` indica erro de montagem no caminho antigo `c/Vocação 2027/QG Vocação 2027 do zero/auto_responder_docker/main.py`.
- **Efeito:** Nenhum webhook de resposta do WhatsApp é processado no ambiente conteinerizado.

### B. Caminhos Relativos Incorretos em `INICIAR_TODAS_FERRAMENTAS.bat`
- **Status:** Aberto.
- **Evidência:** Linhas 9, 17 e 19 referenciam `%~dp0twenty-crm`, `%~dp0openseo` e `%~dp0serpbear` dentro da subpasta `operacoes\`.
- **Efeito:** Falha na inicialização integrada pelo arquivo de lote.

### C. Alucinação Heurística em Cópias de Prospecção Fria
- **Status:** Aberto.
- **Evidência:** `CONFIG_MOTOR_DISPARO_VOCACOES_START.py` (linha 79) e `disparador_fila_*.py` geram hooks afirmando falta de fotos ou falta de canal WhatsApp sem verificação prévia dinâmica.
- **Efeito:** Leads que já possuem ficha completa no Maps recebem mensagens com acusações falsas, rejeitando o contato.

### D. Corrupção de Caracteres Acentuados (Encoding)
- **Status:** Aberto.
- **Evidência:** Arquivo `operacoes/auto_responder_docker/data/chat_history.json` contém registros com caracteres `Olǭ!`, `vocǦs`, `regiǜo`.
- **Efeito:** Envio de mensagens com grafia defeituosa para contatos comerciais.

### E. Alta Taxa de Rejeição de E-mails B2B (Bounce de 50%)
- **Status:** Aberto.
- **Evidência:** `operacoes/bounced_emails.json` contém 5 e-mails rejeitados de um lote teste de 10 garagens.
- **Efeito:** Risco iminente de bloqueio do IP/domínio da Vocação no Zoho Mail.

### F. Violação das Janelas de Horário e Cadência de Envio
- **Status:** Aberto nos scripts batch legados.
- **Evidência:** Disparos realizados às 13:01-13:05 com intervalos de 30 segundos em `dispatch_logs.json`.
- **Efeito:** Alto risco de flag de spam pela Meta.

---

## 4. Pontos Únicos de Falha (SPOF)

1. **Linha Única de WhatsApp Comercial (`INSTANCE_NAME = vocacao_comercial`):**
   - Todos os disparos dependem de um único chip. Se o número for temporariamente banido pela Meta, 100% da operação de prospecção e follow-up para.
2. **Dependência de Banco Local Único (Twenty CRM Postgres):**
   - Toda a esteira de estágios de oportunidade e notas históricas reside em volume local sem rotina automatizada de replicação em nuvem ou backup agendado (apenas scripts manuais `backup_vocacao.bat`).
3. **Ausência de Reconexão Automática da Sessão Baileys:**
   - Se o aparelho de celular desconectar da Evolution API, o sistema não emite alerta sonoro nem tenta reconexão automática, necessitando leitura física de novo QR Code.
