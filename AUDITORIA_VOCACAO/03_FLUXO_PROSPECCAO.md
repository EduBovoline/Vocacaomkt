# 03 — Fluxo Completo de Prospecção Comercial

## 1. Mapeamento do Percurso Real do Lead

O processo de prospecção da Vocação Comunicação & Marketing foi arquitetado para guiar uma empresa desde o descobrimento no Google Maps até a entrega do diagnóstico e fechamento comercial.

Abaixo está o percurso real implementado, evidenciando as decisões automáticas, humanas e os pontos críticos de falha silenciosa.

```
+-----------------------------------------------------------------------------------+
| 1. ENTRADA / DESCOBERTA                                                          |
| Busca manual no Google Maps / CSVs -> resolve_maps.js -> Obtenção de Coordenadas  |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 2. HIGIENIZAÇÃO & VALIDAÇÃO PRÉVIA (Regra Heurística)                            |
| É celular válido com 9º dígito?                                                   |
| [NÃO] -> Descarta / Marca como Telefone Fixo (Sem WhatsApp)                       |
| [SIM] -> Verifica se é estritamente virgem (historico_absoluto_contatados.json)   |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 3. QUALIFICAÇÃO MATEMÁTICA POR IA (Jev System One)                               |
| Envio do estado do lead para o modelo 'jev-latest'                                |
| Retorna: oferta ideal, urgência (0-2), perda de conversão local (0.0-1.0)         |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 4. MONTAGEM DO KIT DE PROSPECÇÃO (Node.js + Chrome Headless)                      |
| generate_lead.js -> Renderiza HTML padrão Watanabe                                |
| convert_pdf.js  -> Gera PDF do Cliente (3 Páginas A4)                             |
| Gera Dossiê Confidencial Interno (HTML com 8 blocos estratégicos)                 |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 5. PERSISTÊNCIA NO TWENTY CRM (sync_lead_twenty.py)                               |
| Cria Company + Person + Opportunity (BRL)                                         |
| Injeta Dossiê Interno nas Notas em Markdown via SQL direto                        |
| Copia PDF para storage e vincula nas tabelas core.file e attachment               |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 6. DISPARO DO PRIMEIRO TOQUE (Toque 1 — Hook de Curiosidade)                     |
| Validação de Janela de Ouro (10h-11h45 e 14h15-16h45 / Seg a Sex)                |
| NENHUM LINK OU ARQUIVO É ENVIADO NO TOQUE 1                                      |
| Envia texto curto com pergunta de permissão + Cláusula Opt-out LGPD               |
| Timer randômico entre envios (360s a 720s) com pausa a cada 4 leads               |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 7. ESCUTA DE RESPOSTAS (Webhook MESSAGES_UPSERT na Porta 5680)                    |
| Evolution API recebe mensagem e entrega no auto_responder                         |
| Filtros de Whitelist: descarta Meta Bot, mensagens próprias e números pessoais    |
+-----------------------------------------------------------------------------------+
                                         │
            ┌────────────────────────────┼────────────────────────────┐
            ▼                            ▼                            ▼
+───────────────────────+   +───────────────────────+   +───────────────────────+
| 8A. PEDIDO DE OPTOUT  |   | 8B. BOT DE RECEPÇÃO   |   | 8C. RESPOSTA POSITIVA |
| Ex: 'PARAR', 'NÃO'    |   | Ex: 'Como posso ajudar|   | Ex: 'sim', 'pode'     |
| • Envia confirmação   |   | • Resposta de bypass  |   | • Envia PDF com       |
| • Salva optout_leads  |   |   com identificação   |   |   legenda oficial     |
| • Atualiza CRM        |   | • 1 único envio       |   | • Atualiza CRM        |
| • Notifica gestor     |   | • Alerta gestor       |   | • Notifica gestor     |
+───────────────────────+   +───────────────────────+   +───────────────────────+
                                                                      │
                                         ┌────────────────────────────┘
                                         ▼
+-----------------------------------------------------------------------------------+
| 9. CONDUÇÃO PÓS-DIAGNÓSTICO & FECHAMENTO (Humano ou Gemini AI)                    |
| Modo Manual Seguro: Sugestões A/B preparadas no Sub-CRM                           |
| Gestor conduz o agendamento de apresentação ou fechamento direto                  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Detalhamento Passo a Passo

### Passo 1: Descoberta e Resolução de Coordenadas
- **Mecanismo:** Script Node.js `resolve_maps.js` recebe a URL curta do Google Maps, faz um `fetch` com redirecionamento habilitado e extrai o nome do local e as coordenadas `latitude, longitude` a partir da URL expandida.
- **Intervenção Humana:** O operador seleciona o nicho e região e insere o link ou importa a planilha.

### Passo 2: Higienização e Checagem de Leads Virgens
- **Mecanismo:**
  1. `is_mobile_phone()`: Verifica se o número tem o 9º dígito obrigatório. Linhas fixas (8 dígitos) são bloqueadas antes do envio.
  2. `is_lead_strictly_virgin()`: Varre `historico_absoluto_contatados.json`, Twenty CRM (`DIRECT_MAP`), `delivered_leads.json`, `optout_leads.json` e o endpoint `/chat/findMessages` da Evolution API.
- **Falha Conhecida:** Nas primeiras versões dos scripts (`disparador_fila_santa_rosalia_brasilandia.py`), essa validação **não existia**, resultando em dezenas de mensagens tentadas contra números fixos.

### Passo 3: Qualificação Semântica com Jev System One
- **Mecanismo:** O script envia o estado do lead para o modelo `jev-latest` da TypeSafe AI via POST HTTP em `https://api.typesafe.ai/v1/systemone`.
- **Decisão:** Totalmente baseada em IA determinística (probabilidades calibradas, sem temperatura de LLM livre). O Jev retorna a oferta oficial da esteira com maior compatibilidade comercial.

### Passo 4: Geração dos Ativos (Kit Watanabe)
- **Mecanismo:** O motor `generate_lead.js` compila:
  - **Relatório do Cliente:** Diagramado em CSS A4 portrait com fontes Fraunces e DM Sans, 4 pilares de análise (Google Maps, Vitrine, Instagram, WhatsApp), tabela comparativa com concorrentes da região e cards de melhoria.
  - **Conversão em PDF:** Executada via `convert_pdf.js` chamando o binário do Google Chrome em modo headless (`--headless=new --print-to-pdf`). O script valida que o PDF gerado possui tamanho superior a 50 KB.
  - **Dossiê Interno:** Arquivo HTML restrito contendo o plano de abordagem, argumentos de autoridade e análise técnica profunda.

### Passo 5: Persistência no Twenty CRM
- **Mecanismo:** O script `sync_lead_twenty.py` conecta diretamente ao container PostgreSQL `twenty-db-1` via comando `docker exec -i twenty-db-1 psql`.
- **Ações:**
  1. Insere ou localiza a empresa na tabela `company`.
  2. Cria o registro de contato na tabela `person`.
  3. Cria a oportunidade com valor em micros (`amountAmountMicros`) na tabela `opportunity`.
  4. Grava o dossiê em Markdown na tabela `note` e associa via `noteTarget`.
  5. Copia o PDF gerado diretamente para o volume interno do Twenty Server (`docker cp`) e registra em `core.file` e `attachment`.

### Passo 6: Disparo do Toque 1 (Curiosidade & Permissão)
- **Mecanismo:** Disparo via Evolution API na rota `/message/sendText/{instance}`.
- **Regras Operacionais:**
  - Janelas de Ouro: 10h00 às 11h45 e 14h15 às 16h45.
  - Intervalos randômicos: 6 a 12 minutos entre disparos. Pausa de 25 a 35 minutos a cada bloco de 4 disparos.
  - Texto estritamente sem link: Solicita apenas autorização de 2 minutos para envio do diagnóstico.
  - Cláusula de opt-out: *"Caso não deseje receber mensagens comerciais, responda PARAR"*.

### Passo 7: Recepção de Respostas & Webhook
- **Mecanismo:** A Evolution API dispara webhook `MESSAGES_UPSERT` para `http://localhost:5680/` (ou `http://vocacao-auto-responder:5680/`).
- **Comportamento por Tipo de Resposta:**
  - **Opt-out:** Descadastra imediatamente, responde com mensagem educada de despedida e notifica o gestor.
  - **Bot de Recepção:** Detecta gatilhos de mensagem automática e envia uma resposta humanizada de bypass se identificando e pedindo para falar com a coordenação.
  - **Indicação de Decisor:** Extrai o número do responsável e agenda abordagem manual.
  - **Autorização Positiva:** Envia o PDF do diagnóstico com legenda persuasiva, avança a oportunidade no CRM para o estágio seguinte e notifica o gestor.
  - **Dúvida / Objeção Aberta:** Bloqueia disparos automáticos e transfere o atendimento para o gestor com sugestões A/B preparadas no painel.

---

## 3. Pontos de Falha Silenciosa Detectados

1. **Tentativa de Disparo em Fila com Container Inativo:**
   - Se o script de auto-responder estiver fora do ar (como está no momento), o primeiro toque pode ser enviado pelos scripts batch, mas nenhuma resposta de lead será processada automaticamente, ficando sem entrega do PDF.

2. **Divergência de Diretórios e Perda de Anexos:**
   - O disparador de e-mail e o auto-responder tentam localizar PDFs em caminhos hardcoded (`C:\Vocação 2027\QG Vocação 2027 do zero\2 Leads`). Se o PDF não estiver nessa pasta exata, o envio é abortado pela trava de integridade ou tenta uma geração sintética sob demanda com dados genéricos.

3. **Sobrecarga de Requisições por Ausência de Heartbeat:**
   - Não há mecanismo de polling ou retry automático para reconectar a Evolution API caso a sessão do WhatsApp caia durante a madrugada.
