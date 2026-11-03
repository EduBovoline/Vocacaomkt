# Correções aplicadas — auditoria de outubro/2026

Este documento registra o que foi corrigido no repositório a partir da
`AUDITORIA_COMPLETA_VOCACAO` (13 arquivos), com o antes/depois de cada item e
como validar. As cinco prioridades da auditoria estão cobertas; o que depende de
ação humana (segredos, execução do Docker) está na seção final.

Arquivo base: `C:\Vocação 2027\QG Vocação 2027 do zero` (mesmo conteúdo do
worktree `audit_prospecting_system_vocacao`, conferido por hash com normalização
de CRLF).

---

## P1 — Container `vocacao-auto-responder` (Exit 127)

**Causa confirmada:** o bind mount `../2 Leads:/app/leads:ro` resolvia para
`operacoes/2 Leads`, diretório que **não existe** (a pasta real é
`<raiz>/2 Leads`). O Docker recusa criar o container quando a origem do bind não
existe. O `esteira_followup_valor.py` também tinha um `DATA_DIR` absoluto
apontando para uma cópia antiga da árvore.

**O que mudou**

| Arquivo | Mudança |
| :--- | :--- |
| `operacoes/auto_responder_docker/docker-compose.yml` | `../2 Leads` → `../../2 Leads`; `LEADS_DIR=/app/leads` explícito; `ZOHO_PASSWORD`, `API_KEY` e `POSTGRES_CRM_PASSWORD` passam a vir do `.env` (`${VAR:-default}`); montagem de `vocacao_seguranca.py` e `ofertas_catalogo.py` |
| `operacoes/auto_responder_docker/esteira_followup_valor.py` | `DATA_DIR` derivado de `__file__` (funciona no host e no container) |
| `operacoes/INICIAR_TODAS_FERRAMENTAS.bat` | raiz corrigida para `%~dp0..`; `twenty-crm`, `openseo` e `serpbear` agora são encontrados; stack da Evolution localizada por wildcard (sem acento no script); o passo 4 sobe o **container** (`docker compose up -d --build`) em vez do `python` solto; checagem de existência de `2 Leads` e do Docker |
| `operacoes/PARAR_TODAS_FERRAMENTAS.bat` | mesmos caminhos corrigidos; derruba o container e o processo host |

**Validação feita:** `docker compose config` resolveu o volume para
`C:\Vocação 2027\QG Vocação 2027 do zero\2 Leads` (pasta existente) e aplicou o
`.env`. O teste de execução do container não foi possível nesta sessão porque o
sandbox bloqueia o pipe do Docker Desktop — rode `INICIAR_TODAS_FERRAMENTAS.bat`
ou `docker compose up -d --build` uma vez para confirmar.

---

## P2 — Copy sem premissas alucinadas

**O que mudou**

- `CONFIG_MOTOR_DISPARO_VOCACOES_START.py`: `generate_compliant_hook` e
  `generate_compliant_followup_hook` reescritos. A abordagem agora **oferece a
  análise** e não afirma que o lead "não tem fotos", "não tem WhatsApp" ou "usa
  @gmail.com". Saiu o jargão "se fizer sentido"; a docstring documenta a regra.
- `disparador_fila_12leads_marcenarias.py`: hook da Marcenaria SHZ (acusação de
  `@gmail.com`) reescrito.
- `disparador_fila_15_curta.py`: hooks que afirmavam ausência de fotos 360 e de
  canal próprio reescritos.
- `disparador_fila_20leads_pilates.py`: hook da Pure Pilates Campolim reescrito.
- `auto_responder_docker/esteira_followup_valor.py`: mensagem D+3 sem o "se
  fizer sentido" e sem o percentual sem fonte.
- `verificar_copy.py` (novo): trava de qualidade. Falha se aparecer "se fizer
  sentido", "faltam fotos", "sem fotos", "@gmail.com", "sem site", "não tem
  WhatsApp" ou promessa de garantia nos `disparador_*.py`.

**Validação feita:** `python verificar_copy.py` → "Copy limpa".

---

## P3 — Encoding UTF-8

**O que mudou**

- `vocacao_seguranca.py` (novo): `forcar_utf8()` reconfigura stdout/stderr e é
  chamado no import; `texto_corrompido()` detecta mojibake (`Olǭ!`, `vocǦs`,
  `regiǜo`, `Ã©`, `�`).
- Bootstrap de UTF-8 adicionado nos scripts que ainda não tinham:
  `atualizar_nature_real.py`, `build_ultimate_subcrm.py`,
  `CONFIG_MOTOR_DISPARO_VOCACOES_START.py`, `create_subcrm_ui.py`,
  `disparador_fila_15_curta.py`, `enriquecer_leads_twenty.py`,
  `generate_subcrm_ui.py`, `importar_30_leads_ouro.py`,
  `importar_leads_twenty.py`, `sincronizar_leads_crm_completos.py`,
  `update_dashboard.py`.
- `auto_responder_docker/enviar_email.py`: reconfigura UTF-8 e importa as
  guardas.
- Todo `open()` de texto no diretório já usava `encoding="utf-8"`; as únicas
  aberturas sem `encoding` são binárias (`"rb"`), o que está correto.
- Como o mojibake real acontecia na **saída** (console cp1252) e não no código,
  a proteção agora é dupla: força UTF-8 e recusa enviar texto corrompido.

---

## P4 — Telefonia, MX e cadência

**O que mudou**

- `vocacao_seguranca.py` (novo):
  - `is_mobile_phone()`: exige DDD válido + 9º dígito + 8 dígitos, rejeita fixo,
    DDD inexistente e assinante repetido;
  - `validar_email_mx()`: sintaxe + MX via `dnspython`, com fallback para
    `nslookup` e, por último, resolução do domínio;
  - `checar_janela()`: usa `is_in_golden_window` do motor oficial (10h–11h45 e
    14h15–16h45, sem fim de semana), com escape consciente por
    `VOCACAO_PERMITIR_FORA_JANELA=1`;
  - `pode_disparar_whatsapp()`: celular → texto íntegro → janela.
- Guarda inserida em `send_whatsapp()` de: `disparador_fase2_lote1.py`,
  `disparador_fila_12leads_marcenarias.py`, `disparador_fila_15_curta.py`,
  `disparador_fila_16leads.py`, `disparador_fila_20leads_pilates.py`,
  `disparador_fila_7min.py`, `disparador_fila_ouro_30.py`,
  `disparador_fila_santa_rosalia_brasilandia.py`, `disparador_trujillo_3leads.py`.
  Mensagens para `ADMIN_WHATSAPP` pulam a trava de janela (aviso operacional).
- `enviar_email_zoho.send_email` e `auto_responder_docker/enviar_email.py`:
  validam MX antes do SMTP.
- `verificar_fila_disparo.py` (novo): pré-voo de qualquer JSON de fila —
  separa fixo/inválido, duplicado, já contatado, e-mail sem MX e sem contato;
  `--strict` sai com código 1; `--json` grava o relatório.

**Validação feita:** autoteste de `is_mobile_phone` (7 casos), MX de
`vocacao.digital` (ok) e de domínio inexistente (bloqueado), pré-voo em
`leads_ouro_fila_disparo.json` (30/30 válidos) e em fila sintética (fixo,
duplicado, MX e sem contato separados corretamente).

---

## P5 — Catálogo único do Jev

**O que mudou**

- `ofertas_catalogo.py` (novo): fonte única com as 5 ofertas oficiais
  (Maps R$ 450, Tour avulso R$ 650, Start R$ 850, Combo R$ 950, Update R$ 980),
  escopo, exclusões, prazo, perfis de maturidade, critérios de urgência e a
  oferta padrão.
- `references/matriz-ofertas-niveis.md` (novo): versão humana do mesmo catálogo,
  com funil, cobrança, trava de bairro e fontes das estatísticas.
- `auto_responder_docker/jev_engine.py`: deixou de ter catálogo embutido; importa
  `criterios_jev()`, `PERFIS_MATURIDADE`, `URGENCIA_CRITERIOS` e `obter()` do
  módulo único. `OFFER_PRICES` continua existindo como espelho, gerado do
  catálogo, para não quebrar imports antigos.
- `docker-compose.yml` monta `ofertas_catalogo.py` em `/app`.
- `verificar_catalogo.py` (novo): compara catálogo × documento × motores e falha
  se um preço sumir, um nome divergir ou um motor voltar a embutir a esteira.
- Cópia do `jev_classifier.py` em `MAQUINA_PROSPECCAO_1ST_TOUCH` alinhada ao
  critério do Combo.

**Validação feita:** `python verificar_catalogo.py` → 5 ofertas conferidas.

---

## Como validar tudo em 1 minuto

```bat
cd "C:\Vocação 2027\QG Vocação 2027 do zero\operacoes"
python vocacao_seguranca.py
python verificar_catalogo.py
python verificar_copy.py
python verificar_fila_disparo.py leads_ouro_fila_disparo.json
cd auto_responder_docker
docker compose config --quiet
```

---

## Pendências que dependem de você

1. **Rotacionar segredos:** `ZOHO_PASSWORD`, `TYPESAFE_API_KEY` e a senha do
   Postgres estão em texto puro no código/`.env` (e estavam no zip da auditoria).
   Troque as senhas e mantenha só no `.env`, que já é lido pelo compose.
2. **Subir o container** uma vez (`INICIAR_TODAS_FERRAMENTAS.bat`) e conferir
   `http://localhost:5680/painel` — não foi possível testar o runtime aqui.
3. **Sincronizar o plugin oficial** `C:\Users\edubo\.gemini\config\plugins\vocacao\skills\vocacao-prospeccao\scripts\jev_classifier.py`
   com o catálogo (a cópia em `MAQUINA_PROSPECCAO_1ST_TOUCH` já foi alinhada).
4. **DNS do domínio:** validar SPF/DKIM/DMARC de `vocacao.digital` antes do
   próximo lote de e-mail (a auditoria deixou como pergunta em aberto).
