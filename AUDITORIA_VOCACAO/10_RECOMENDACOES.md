# 10 — Recomendações Técnicas e Operacionais (Para o ChatGPT)

## 1. Diretrizes Estratégicas para a Próxima Fase

O objetivo desta auditoria é fornecer ao assistente de IA (ChatGPT) insumos claros para solucionar os gargalos da Máquina de Prospecção sem reinventar a roda.

As recomendações estão ordenadas por **Impacto no Negócio** e **Risco Operacional**:

---

## 2. Recomendações Prioritárias

### Prioridade 1 (Crítica / Urgente): Correção da Montagem do Container Auto-Responder
- **Diagnóstico:** O container `vocacao-auto-responder` falha com Exit Code 127 porque aponta para o diretório antigo `c/Vocação 2027/QG Vocação 2027 do zero/...`.
- **Ação Recomendada:**
  1. No arquivo `operacoes/auto_responder_docker/docker-compose.yml`, substituir os caminhos relativos ou atualizar para o caminho canônico do repositório atual.
  2. Ajustar `operacoes/INICIAR_TODAS_FERRAMENTAS.bat` para referenciar os diretórios corretos a partir da raiz (`cd /d "%~dp0.."`).
- **Impacto:** Restaura o processamento de webhooks e o painel Sub-CRM na porta 5680.

---

### Prioridade 2 (Crítica / Qualidade Comercial): Eliminação de Premissas Alucinadas nas Mensagens
- **Diagnóstico:** Os scripts cold outreach afirmam categoricamente que o cliente "não tem fotos atualizadas", "não tem canal WhatsApp" ou "usa @gmail.com", gerando atrito com leads que já possuem esses itens.
- **Ação Recomendada:**
  1. Modificar a copy do primeiro toque para uma abordagem neutra e baseada em oportunidade local, sem acusações técnicas não confirmadas:
     > *"Olá [Nome], tudo bem? Edu aqui da Vocação em Sorocaba. Estava mapeando as clínicas e espaços de saúde aqui na região do [Bairro] e preparei uma análise visual rápida de 2 minutos sobre como novos moradores do bairro encontram e escolhem vocês no Google Maps pelo smartphone. Posso te enviar por aqui para você dar uma olhada? Abraço!"*
  2. Remover todas as ocorrências do jargão banido *"se fizer sentido"*, substituindo por perguntas diretas e limpas (*"Posso te mandar por aqui?"*).
- **Impacto:** Elimina o constrangimento comercial e eleva a taxa de resposta positiva.

---

### Prioridade 3 (Alta / Integridade Técnica): Padronização Rígida de Encoding UTF-8
- **Diagnóstico:** Strings acentuadas foram salvas corrompidas no Windows (`Olǭ!`, `vocǦs`), chegando defeituosas ao WhatsApp.
- **Ação Recomendada:**
  1. Em todos os scripts Python (`main.py`, `disparador_*.py`), adicionar no topo:
     ```python
     import sys
     if hasattr(sys.stdout, 'reconfigure'):
         sys.stdout.reconfigure(encoding='utf-8', errors='replace')
     ```
  2. Garantir que todas as chamadas `open(..., encoding='utf-8')` e `json.dump(..., ensure_ascii=False)` estejam estritamente parametrizadas.
- **Impacto:** Garante que toda comunicação externa seja enviada com ortografia impecável.

---

### Prioridade 4 (Alta / Entregabilidade): Verificação Prévia de Telefonia e Validação MX
- **Diagnóstico:** Disparos para telefones fixos (descarte de leads) e 50% de bounce em e-mails B2B.
- **Ação Recomendada:**
  1. Integrar a função `is_mobile_phone()` como filtro obrigatório antes de qualquer inserção na fila de disparo.
  2. Para o canal de e-mail, implementar validação simples de registros DNS MX (`dnspython`) e checagem de sintaxe antes de submeter requisições ao Zoho Mail.
- **Impacto:** Protege a reputação do chip WhatsApp e do domínio `vocacao.digital`.

---

### Prioridade 5 (Média / Alinhamento de Produto): Unificação dos Catálogos do Jev
- **Diagnóstico:** `jev_classifier.py` referencia a esteira antiga (Vitrines de R$ 150 a R$ 980), enquanto `jev_engine.py` referencia a esteira oficial atual (Vocação Start R$ 850, Vocação Update R$ 980, Combo Maps R$ 950, Presença Maps R$ 450).
- **Ação Recomendada:**
  1. Padronizar o catálogo de critérios do Jev em um único arquivo de referência (`matriz-ofertas-niveis.md`), importado uniformemente em todos os scripts.
- **Impacto:** Garante que a precificação e o nome da oferta sejam 100% coerentes entre CRM, PDFs e mensagens.

---

## 3. O Que NÃO Fazer

1. **Não reescrever o motor de PDF:** A diagramação de `generate_lead.js` e a conversão de `convert_pdf.js` funcionam perfeitamente.
2. **Não substituir o Twenty CRM:** O banco relacional Postgres 16 e o pipeline de `sync_lead_twenty.py` estão saudáveis e estáveis.
3. **Não trocar a Evolution API por bibliotecas não testadas:** A stack v2 conteinerizada é robusta e bem configurada.
