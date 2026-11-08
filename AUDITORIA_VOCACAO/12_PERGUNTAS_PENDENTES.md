# 12 — Perguntas Pendentes e Lacunas de Informação

## 1. O que Não Foi Possível Determinar em Modo Exclusivo de Leitura

Seguindo as regras absolutas da auditoria (não disparar mensagens reais, não modificar o banco de dados e não reiniciar containers), foram mapeadas as seguintes questões em aberto:

---

## 2. Lacunas Mapeadas

### A. Estado Atual da Conexão WhatsApp na Evolution API
- **Pergunta:** A sessão `vocacao_comercial` na Evolution API está autenticada e conectada ao chip físico neste exato momento, ou exige nova leitura de QR Code?
- **Motivo da Incerteza:** O container está `Up`, mas verificar o estado exato da sessão sem consultar endpoints autenticados ou disparar testes ativos não foi executado para evitar instabilidade.

### B. Existência de um Crawler Automatizado de Descoberta Contínua
- **Pergunta:** Existe algum script de extração automática contínua de novas fichas do Google Maps que foi desenvolvido em repositório externo ou arquivo avulso fora da árvore inspecionada?
- **Motivo da Incerteza:** No repositório auditado, há apenas o resolvedor de URLs individuais (`resolve_maps.js`) e planilhas CSV consolidadas. Não foi localizado um script autônomo que receba "todas as marcenarias de Sorocaba" e varra o Google Maps diretamente via Puppeteer/Selenium.

### C. Configuração de DNS (SPF, DKIM, DMARC) de `vocacao.digital`
- **Pergunta:** O domínio `vocacao.digital` possui registros SPF, DKIM e DMARC devidamente alinhados aos servidores do Zoho Mail?
- **Motivo da Incerteza:** Essa verificação exigiria consultas DNS públicas externas ativas. Como 50% dos e-mails sofreram bounce, é fundamental validar se os registros de autenticação estão 100% aprovados para evitar a pasta de spam.

### D. Histórico Completo de Banes / Advertências da Meta
- **Pergunta:** A linha `5515981512083` ou outro chip utilizado em disparos anteriores sofreu algum bloqueio temporário, aviso de spam ou restrição de rate limit durante os disparos do início de outubro?
- **Motivo da Incerteza:** Os logs locais não registram os retornos internos de qualidade de número da Meta (apenas status de sucesso/falha da requisição HTTP à Evolution API).

### E. Uso Real dos Workflows do n8n
- **Pergunta:** O n8n foi efetivamente utilizado como substituto do auto-responder Python em algum momento, ou o workflow `workflow_vocacao_update.json` foi apenas um teste conceitual mantido em paralelo?
- **Motivo da Incerteza:** O container `vocacao-n8n` está ativo, mas o arquivo de lote `INICIAR_TODAS_FERRAMENTAS.bat` dispara `auto_responder.py` em Python, indicando concorrência de responsabilidades entre os dois componentes.
