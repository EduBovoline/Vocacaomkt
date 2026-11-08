# 🧭 MANUAL DA ESTEIRA DE PROSPECÇÃO COMERCIAL — VOCAÇÃO 2027
> **Documento Oficial de Arquitetura & Fluxo Passo a Passo**  
> **Versão:** Outubro / 2026  
> **Padrão Visual:** Estrutura Watanabe + Paleta Marcenaria Sucesso  

---

## 🎯 Perfil de Cliente Ideal (ICP) & Território Prioritário

### 1. Quem é o Cliente da Vocação:
* **Nichos de Alto Valor Agregado:** Oficinas mecânicas e autopeças especializadas, marcenarias e móveis planejados, consultórios e clínicas médicas/odontológicas independentes, pet shops premium locais, marmorarias, estúdios e serviços técnicos especializados.
* **Autonomia Direta de Decisão:** Empresas independentes onde o **proprietário/sócio está presente no balcão ou na operação** e atende diretamente no WhatsApp.
* **Critério de Fechamento Ágil:** O dono sente a dor de perder clientes no Google e tem autonomia total para fechar a solução em uma conversa de 5 minutos, sem comitês de aprovação.

### 2. Território Prioritário (Raio de Proximidade do Escritório):
* **Foco Inicial Absoluto:** Bairros no entorno imediato do endereço do Eduardo em Sorocaba:
  * **Santa Rosália** (sede / base operacional na Pereira da Silva)
  * **Jardim Brasilândia**
  * **Vila Santana**
  * **Trujillo**
  * **Além Ponte** e adjacências da Zona Leste / Central.
* **Poder da Conexão Local:** A proximidade física (*"estou aqui pertinho de vocês em Santa Rosália"*) quebra a barreira de desconfiança de agência remota e estabelece autoridade imediata de vizinho e parceiro comercial.

### ⛔ O que está TERMINANTEMENTE EXCLUÍDO (Critérios Negativos):
1. **Redes e Franquias de Shopping:** Estruturas corporativas com marketing terceirizado ou centralizado em São Paulo / outras capitais.
2. **Empresas Engessadas de Bairros Corporativos Distantes:** Empresas blindadas por secretárias e intermediários que barram o contato com o decisor.
3. **Comércios de Baixíssimo Ticket:** Negócios sem margem para absorver investimentos de R$ 450 a R$ 980.

---

## ⚡ Visão Geral do Fluxo em 5 Etapas

```
[Link Maps / Nome] 
       │
       ▼
[Etapa 1: Resolução de Dados (resolve_maps.js)]
       │
       ▼
[Etapa 2: Triagem Semântica Jev (jev_classifier.py)]
       │
       ▼
[Etapa 3: Geração Anti-Slop Watanabe + Marcenaria Sucesso (generate_lead.js)]
       │  ├── Relatório do Cliente (HTML)
       │  ├── Diagnóstico em PDF Oficial (3 Páginas A4)
       │  └── Dossiê Estratégico Interno (HTML)
       │
       ▼
[Etapa 4: Fila Operacional & Auto-Exclusão no Sub-CRM (painel.html / main.py)]
       │  └── Lead sai automaticamente do Banco para a Fila ao Vivo
       │
       ▼
[Etapa 5: Cadência de Disparo Docker & Controle do Gestor (Evolution API)]
          └── Disparo a cada ~4-5 min -> Resposta do Lead -> Gestor aprova com "1"
```

---

## 📍 Etapa 1: Resolução & Entrada de Dados

Quando um link do Google Maps é recebido (ex: `https://maps.app.goo.gl/...`):
* **Comando de execução:**
  ```bash
  node "C:\Users\edubo\.gemini\config\plugins\vocacao\skills\vocacao-prospeccao\scripts\resolve_maps.js" "<URL_MAPS>"
  ```
* **O que faz:**
  1. Resolve o redirecionamento curto em segundos.
  2. Extrai o nome oficial cadastrado no Google, coordenadas e link expandido.
  3. Previne erros de homônimos ou empresas fora de Sorocaba e região.

---

## 🧠 Etapa 2: Triagem & Qualificação Semântica com Jev System One

Em vez de alucinações de LLMs convencionais, o motor Jev (`jev-latest`) analisa os canais digitais de forma determinística:
* **Comando de execução:**
  ```bash
  python "C:\Users\edubo\.gemini\config\plugins\vocacao\skills\vocacao-prospeccao\scripts\jev_classifier.py" "<DADOS_LEAD_JSON_OU_TEXTO>"
  ```
* **Saídas do Jev:**
  * `oferta_recomendada`: Escolha ponderada entre *Vocação Start (R$ 850)*, *Vocação Update (R$ 980)*, *Combo Maps + Tour 360° (R$ 950)* ou *Presença no Maps (R$ 450)*.
  * `perfil_maturidade`: Classificação técnica (`sem_presenca`, `site_legado`, `espaco_ambiente` ou `regularizacao_maps`).
  * `perda_conversao_local`: Probabilidade calculada de 0.0 a 1.0 de perda de novos clientes no bairro.
  * `urgencia_score`: Score objetivo de urgência (0 a 2).

---

## 🎨 Etapa 3: Geração do Kit Anti-Slop (Watanabe + Marcenaria Sucesso)

A montagem do relatório é executada pelo script nativo [generate_lead.js](file:///C:/Users/edubo/.gemini/config/plugins/vocacao/skills/vocacao-prospeccao/scripts/generate_lead.js), que garante **Zero Consumo de Tokens** no layout e **Blindagem Total contra Slop**:

* **Comando de execução:**
  ```bash
  node "C:\Users\edubo\.gemini\config\plugins\vocacao\skills\vocacao-prospeccao\scripts\generate_lead.js" "<CAMINHO_DO_LEAD_DATA.JSON>"
  ```
* **Regras de Identidade Visual Aplicadas:**
  * **Estrutura Soberana:** Espelhada em [Watanabe auto peças](file:///C:/Antigravity%20projects/Vocação%202027/Prospects/Watanabe%20auto%20peças) (Header curvado com elipse, radar comparativo de pontuação por canal 0-10, tabela de concorrentes e oportunidades numeradas 01 a 04).
  * **Esquema Cromático Marcenaria Sucesso:**
    * `--color-primary`: `#061B28` (Dark Navy Profundo)
    * `--color-accent`: `#E5B910` (Dourado Solar Vocação)
    * `--color-accent-soft`: `#FCF9EB` (Creme Solar)
    * `--color-positive`: `#0B5E47` (Verde Esmeralda Vocação)
    * `--color-negative`: `#9B2335` (Vermelho Carmim)
    * `--color-bg`: `#FAFAF8` (Off-white editorial)
  * **Tipografia:** `Fraunces` (serif editorial) para títulos e destaques + `DM Sans` para leitura técnica.
* **Trava Anti-Slop Automática:**
  * Aborta imediatamente se detectar literais `undefined`, `null` ou `[object Object]`.
  * Exige no mínimo 3 a 5 concorrentes **reais** (rejeita termos como *"Clínicas Campolim"* ou *"Concorrente 1"*).
  * Compilação para PDF via Chrome Headless ([convert_pdf.js](file:///C:/Users/edubo/.gemini/config/plugins/vocacao/skills/vocacao-prospeccao/scripts/convert_pdf.js)), validando tamanho `>= 50.000 bytes`.

---

## 📋 Etapa 4: Fila Operacional & Auto-Exclusão no Sub-CRM

Gerenciado através do [painel.html](file:///C:/Vocação%202027/QG%20Vocação%202027%20do%20zero/auto_responder_docker/templates/painel.html) rodando no Docker (`http://localhost:5680/painel`):

* **Mapeamento de Bases:**
  * `leads_100_santa_rosalia_brasilandia.json`
  * `leads_alto_ticket_verificados.json`
* **Regra de Exclusão Automática da Live (Anti-Duplicidade):**
  * Sempre que um lead é adicionado à fila de disparo (individualmente via `addLeadToQueue` ou em lote via `adicionarLoteRequisitadoAFila`), a função `remove_leads_from_bank()` no backend remove o registro imediatamente dos bancos persistentes.
  * No frontend, o lead é expurgado da tabela e os contadores de leads virgens são atualizados instantaneamente.
  * Leads com chat aberto ou histórico de contato prévio nunca reaparecem como virgens.

---

## 📲 Etapa 5: Cadência de Disparo Docker & Controle do Gestor

O container Docker `vocacao-auto-responder` roda em background com cadência humanizada e proteção máxima:

* **Janela Comercial:** 09h00 às 18h00 (bloqueio automático à noite e finais de semana).
* **Cadência Anti-Bloqueio Meta:** 1 mensagem a cada 4 a 5 minutos (240s a 330s aleatórios).
* **Fluxo de 2 Passos (Toque com Permissão):**
  1. O motor dispara o gancho inicial sem PDF (mensagem curta de 4 linhas perguntando se pode enviar o diagnóstico).
  2. Quando o lead responde positivamente (*"Sim"*, *"Pode mandar"*, *"Quero"*):
     * O Jev qualifica a intenção.
     * O sistema notifica o Eduardo no WhatsApp (`5515981512083`).
     * O gestor responde apenas **"1"** no seu WhatsApp para autorizar.
     * O PDF de 3 páginas é disparado automaticamente com legenda de garantia.

---

## 📂 Mapa de Arquivos & Skills Vinculadas

| Função / Etapa | Arquivo / Skill Principal | Papel |
| :--- | :--- | :--- |
| **Diagnóstico de Leads** | `vocacao-prospeccao` | Gera HTML, PDF e Dossiê Interno no padrão oficial. |
| **Harness de Disparo** | `vocacao-motor-prospeccao` | Controla fila, warm-up e circuit breaker Meta. |
| **Alto Valor Local (Dono no Balcão)** | `vocacao-prospeccao-alto-ticket` | Prospecção de negócios locais independentes de alto valor agregado no raio de Santa Rosália e região vizinha (marcenarias, mecânicas especializadas, consultórios; sem redes ou franquias corporativas). |
| **Motor Docker** | `auto_responder_docker/main.py` | Servidor backend, webhook Evolution API e dispatcher. |
| **Sub-CRM Web** | `auto_responder_docker/templates/painel.html` | Interface visual de controle de fila e leads. |
| **Brandbook Oficial** | `MANUAL_BRANDBOOK_UI_VOCACAO.md` | Tokens de cor Marcenaria Sucesso e tipografia Fraunces. |
