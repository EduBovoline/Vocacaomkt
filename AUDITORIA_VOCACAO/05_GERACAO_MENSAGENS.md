# 05 — Auditoria das Mensagens Comerciais & Análise de Erros

## 1. Importância desta Auditoria

O sistema da Vocação já operou disparos reais e interagiu com leads comerciais. Durante esses ciclos, **ocorreram falhas graves na geração de abordagens**, gerando mensagens com premissas inverídicas, perguntas excessivas que afastaram decisores e corrupção de caracteres.

Esta seção detalha onde as mensagens são geradas, quais modelos e templates são usados, como os erros se manifestaram e documenta casos reais com evidências do repositório.

---

## 2. Onde as Mensagens São Geradas

Existem **três pontos de origem** de mensagens no ecossistema:

1. **Hooks de Primeiro Toque (Cold Outreach Batch):**
   - Arquivos: `disparador_fila_santa_rosalia_brasilandia.py`, `disparador_fila_20leads_pilates.py`, `disparador_fila_12leads_marcenarias.py`, `CONFIG_MOTOR_DISPARO_VOCACOES_START.py`.
   - Método: Templates estáticos interpolados com variáveis do lead (`{lead_name}`, `{bairro}`, `{segmento}`).

2. **Geração Sob Demanda de Legendas de Entrega (Auto-Responder):**
   - Arquivo: `operacoes/auto_responder.py` (função `send_pdf()`, linhas 419-426).
   - Método: Texto pré-definido acompanhando o envio do documento PDF.

3. **Respostas Conversacionais Consultivas (Auto-Responder com IA):**
   - Arquivo: `operacoes/auto_responder_docker/gemini_classifier.py` (função `analyze_and_generate_reply()`).
   - Método: Chamada à API Google Gemini (`gemini-3.8-flash` e fallback `gemini-flash-lite-latest`) alimentada com o histórico da conversa (`chat_history.json`).

---

## 3. Prompts e Diretrizes Fornecidas aos Modelos

O prompt de geração conversacional está em `gemini_classifier.py` (linhas 21-37):

```text
Você é o Eduardo Bovoline, fundador da Vocação Comunicação & Marketing em Sorocaba/SP.
Você conversa como um profissional de verdade no WhatsApp: direto, humano, respeitoso e consultivo, sem ser rude.

DIRETRIZES DE OURO DA VOCAÇÃO:
1. ESCUTA ATIVA (80% / 20%): NUNCA empurre diagnóstico, oferta, preço ou proposta antes de compreender ao menos 80% do negócio do lead.
2. DIRETO E HUMANO (SEM BAJULAÇÃO): Não use comentários forçados de falsa empatia ou elogios vazios (evite 'Que fantástico!', 'Que maravilha!', 'Compreendo sua dor'). Seja natural, direto e educado.
3. REGRA DA PERGUNTA ÚNICA: NUNCA faça mais de uma pergunta por mensagem. Faça apenas UMA pergunta clara e objetiva para entender a realidade do cliente.
4. LINGUAGEM ÁGIL: Mensagens curtas de 1 a 2 linhas, ideais para leitura rápida no WhatsApp.
5. LGPD: Se pedir para parar/remover, classifique como OPTOUT e encerre com brevidade.

Responda SOMENTE um JSON válido:
{
  "intent": "QUALIFICATION" | "QUESTION" | "OBJECTION" | "POSITIVE" | "OPTOUT",
  "stage": "LISTENING" | "DIAGNOSING" | "READY_TO_OFFER",
  "reasoning": "análise rápida do momento do cliente",
  "suggested_reply": "mensagem curta, direta, humana, com rigorosamente UMA pergunta objetiva pronta para envio"
}
```

---

## 4. Análise dos Problemas Identificados

### Problema 1: Afirmações Falsas Apresentadas como Fatos (Alucinação Heurística)
- **Mecanismo do Erro:** Em `CONFIG_MOTOR_DISPARO_VOCACOES_START.py` (linhas 79-80), a função `generate_compliant_hook` gera:
  > *"Vi que vocês têm um trabalho sério na região, mas a apresentação da empresa no Google ainda não reflete isso — faltam fotos atualizadas e um canal direto para o WhatsApp de atendimento."*
- **Impacto Real:** Essa frase foi enviada indistintamente para dezenas de estabelecimentos. Muitas dessas empresas **já possuíam** canal de WhatsApp no Google Maps ou fotos recentes postadas por clientes. A abordagem foi imediatamente desmascarada como automação genérica, destruindo a autoridade da agência.

### Problema 2: Sobrecarga Cognitiva e Violação da Regra de Pergunta Única
- **Mecanismo do Erro:** Apesar do prompt exigir expressamente "rigorosamente UMA pergunta objetiva", a IA gerou respostas contendo duas ou três perguntas densas e complexas sobre a operação comercial do lead.
- **Evidência Histórica Documentada:** Em `chat_history.json` (registro do lead `5511976035867`, empresa de panificação industrial):
  - **Lead:** *"Legal, mas é padaria industrial, fazemos pão para toda região de sorocaba"*
  - **IA Vocação:** *"Opa Gui, excelente saber! Muda totalmente o cenário: vocês são indústria e distribuição regional B2B. Vocês atendem principalmente supermercados, minimercados, hotéis e restaurantes, ou fornecem também para padarias menores da região? E hoje a abertura de novos pontos e clientes é feita mais no boca a boca/motoristas na rua ou vocês já têm um time comercial ativo?"* (3 perguntas simultâneas em 1 mensagem longa).
  - **Reação do Lead:** *"Ah muita coisa pra responder, não tenho tempo. Falo com você depois m"* (Lead desengajou e perdeu o interesse).

### Problema 3: Diálogo Involuntário com Bots de Atendimento
- **Mecanismo do Erro:** O sistema não possuía nas primeiras versões um classificador eficiente de mensagens automatizadas recebidas de secretárias eletrônicas ou bots de boas-vindas do WhatsApp Business.
- **Evidência Histórica Documentada:** Em `chat_history.json` (registro do lead `5515991767971` — Clínica Paes):
  - **Bot da Clínica Paes:** *"Seja bem vindo a Clínica Paes! Agradecemos por escolher entrar em contato conosco. Você pode me contar um pouco mais sobre o que deseja melhorar ou o que te motivou a buscar nosso atendimento?..."*
  - **IA Vocação:** *"Muito bom, Clínica Paes Pilates & Fisio. Área de saúde exige muita autoridade e confiança. Hoje a maior parte dos seus pacientes chega por indicação ou pelas buscas do Google?"*
  - O sistema respondeu a uma mensagem automática de boas-vindas como se estivesse conversando com o dono da clínica.

### Problema 4: Violação de Diretriz Antijargão ("Faz Sentido")
- **Regra Oficial da Vocação:** No documento soberano de branding (`vocacao-prospeccao/SKILL.md`, linha 72), determina-se:
  > *"PROIBIDO O JARGÃO 'FAZ SENTIDO': É terminantemente proibido usar as expressões 'se fizer sentido', 'se faz sentido pra você' ou qualquer variação de coach/vendedor."*
- **Código em Produção:** Em `operacoes/auto_responder.py` (linha 425):
  > *"Dê uma olhada rápida (leva 2 minutos) e me diga se faz sentido pra vocês!"*
  E em `CONFIG_MOTOR_DISPARO_VOCACOES_START.py` (linha 82):
  > *"Se fizer sentido, te mando aqui pra você dar uma olhada (leva nem 2 minutos). Abraço!"*
  O próprio código oficial violou a diretriz anti-slop central da marca.

### Problema 5: Corrupção Sistemática de Encoding (Mojibake UTF-8 / Windows-1252)
- **Mecanismo do Erro:** Ao salvar arquivos JSON e enviar strings pelo PowerShell e scripts Python no Windows sem forçar `encoding='utf-8'`, caracteres acentuados sofreram conversão incorreta.
- **Exemplo Real Registrado:**
  > *"Olǭ! Analisei a presena digital de vocǦs no Santa Rosǭlia e notei que quem pesquisa pelos seus servios no Google encontra pouca informaǜo institucional independente antes de chamar no WhatsApp..."*
  Essa mensagem foi gravada com esses mesmos caracteres e entregue a contatos reais.

---

## 5. Exemplos Anonimizados de Erros Históricos

| Caso | Lead | Mensagem Gerada | Informação Incorreta / Causa | Consequência |
| :---: | :---: | :--- | :--- | :--- |
| **01** | Padaria B2B | 3 perguntas longas sobre motoristas, atacado e representantes | Violação da regra de mensagem curta e pergunta única | Lead encerrou o contato por falta de tempo |
| **02** | Clínica Médica | Resposta reflexiva a bot de recepção automática | Falta de filtro de mensagem institucional | Conversa robô-contra-robô |
| **03** | Marcenaria | Afirmação de que o site usava `@gmail.com` | Premissa inferida sem verificação em tempo real | Lead desmentiu e questionou seriedade |
| **04** | Base Santa Rosália | Mensagens enviadas com `Olǭ!`, `vocǦs` e `regiǜo` | Corrupção de encoding UTF-8 no Windows | Perda de credibilidade técnica imediata |
| **05** | Base Odonto | Abordagem enviada para telefone fixo de 8 dígitos | Ausência de validação de número móvel celular | Falha e descarte de lead na Evolution API |
