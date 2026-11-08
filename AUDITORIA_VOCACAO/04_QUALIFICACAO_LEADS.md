# 04 — Inteligência de Qualificação e Ranqueamento de Leads

## 1. Metodologia de Classificação dos Leads

A qualificação de oportunidades comerciais no ecossistema da Vocação combina **heurísticas determinísticas** (regras de negócio) e **julgamento semântico probabilístico** fornecido pelo modelo **Jev System One (`jev-latest`)** da plataforma TypeSafe AI.

Diferente de abordagens tradicionais que usam LLMs com temperatura livre (sujeitas a alucinações e respostas textuais prolixas), o sistema emprega o Jev para retornar tipos primitivos rigorosos (`choice`, `noul` e `score`), garantindo que o código em Python possa tomar decisões de rota sem parse instável.

---

## 2. Dimensões e Variáveis de Avaliação

O sistema qualifica o lead com base em 4 dimensões obrigatórias:

| Dimensão | Tipo no Jev | Intervalo / Opções | Significado Comercial |
| :--- | :--- | :--- | :--- |
| **`oferta_principal`** | `choice` | 4 ofertas oficiais | Seleciona o produto da esteira oficial com maior adequação técnica e comercial ao momento do lead. |
| **`perfil_maturidade`** | `choice` | `sem_presenca`, `site_legado`, `espaco_ambiente`, `regularizacao_maps` | Mapeia o diagnóstico técnico da presença online da empresa. |
| **`perda_conversao_local`**| `noul` | Probabilidade calibrada de 0.0 a 1.0 | Mede a chance de o negócio estar perdendo clientes do próprio bairro para concorrentes com presença superior. |
| **`urgencia_presenca`** | `score` | 0 (Baixa), 1 (Média), 2 (Crítica) | Determina a prioridade de abordagem na fila comercial. |

---

## 3. Matriz de Decisão: Ofertas e Critérios Oficiais

Conforme implementado no motor oficial `operacoes/auto_responder_docker/jev_engine.py` (linhas 25-59):

### A. Oferta 1: Vocação Start (Carro-Chefe — R$ 850,00)
- **Critério de Ativação:** Empresas sem site independente, com site quebrado/fora do ar, ou que dependem exclusivamente de Linktree, Instagram ou botão de WhatsApp solto.
- **Entregável:** Google Maps otimizado e blindado + Vitrine Digital One-Page ultra-rápida em subdomínio seguro (`cliente.vocacao.digital`) em até 7 dias úteis.

### B. Oferta 2: Vocação Update (Reforma Mobile-First — R$ 980,00)
- **Critério de Ativação:** Empresas que já possuem site legado, porém antigo, lento, não adaptado para smartphones ou visualmente desatualizado.
- **Entregável:** Reestruturação visual completa com abertura em menos de 0.5s sem reuniões demoradas (prazo de 5 dias úteis).

### C. Oferta 3: Combo Maps + Tour Virtual 360° GoPro Max (R$ 950,00)
- **Critério de Ativação:** Empresas onde o espaço físico é o maior diferencial de conversão e encantamento (studios de pilates, clínicas médicas e estéticas, escolas e academias).
- **Entregável:** Otimização avançada da ficha do Google Maps + Fotos panorâmicas esféricas em 5.6K integradas ao Google Street View com remoção profissional de tripé.

### D. Oferta 4: Presença Local no Google Maps (R$ 450,00)
- **Critério de Ativação:** Empresas consolidadas no mundo físico que necessitam apenas da regularização, blindagem contra concorrentes e ranqueamento local dos 8 pilares da ficha do Google Maps.

---

## 4. Diferenciação de Leads: Frios, Mornos, Quentes e Fila Ouro

Nos scripts operacionais e painéis de controle (`build_real_leads.py` e `disparador_fila_ouro_30.py`), os leads são categorizados por temperatura:

```
[LEAD FRIO]
   • Dados públicos extraídos de diretórios ou buscas gerais.
   • Sem validação prévia de decisor.
   • Apenas telefone de recepção ou e-mail institucional geral ('contato@').
   • Ação: Entrada na cadência fria de E-mail B2B ou primeiro toque WhatsApp.

[LEAD MORNO]
   • Presença digital auditada e classificada pelo Jev (urgência >= 1).
   • Identificado nome do responsável ou gestor da unidade.
   • Diagnóstico e Dossiê Watanabe pré-gerados e indexados no CRM.
   • Ação: Fila de disparo em janelas estratégicas com hook personalizado.

[LEAD QUENTE]
   • Respondeu positivamente ao primeiro toque ("sim", "pode mandar", "quero ver").
   • Recebeu o PDF oficial de diagnóstico com 3 páginas.
   • Oportunidade no Twenty CRM avançada para estágio 'DELIBERATING' / 'MEETING'.
   • Ação: Transição imediata para condução humana ou sugestão A/B do gestor.

[LEAD OURO (TOP 30)]
   • Score de Urgência = 2 (Crítica).
   • Probabilidade de perda local > 0.80.
   • Ticket de serviço do lead elevado (alta capacidade de pagamento).
   • Celular móvel validado com WhatsApp ativo.
   • Ação: Disparo prioritário com gancho hiperlocal (citando a rua/bairro e diferencial específico).
```

---

## 5. Implementação Técnica do Código do Jev

O código em `operacoes/auto_responder_docker/jev_engine.py` demonstra a chamada à API:

```python
payload = {
    "model": "jev-latest",
    "state": {
        "nome": lead_name,
        "mensagem_lead": message_text,
        "contexto": context
    },
    "questions": {
        "oferta_principal": {
            "type": "choice",
            "instructions": "Qual oferta da esteira oficial da Vocação tem o melhor fit imediato para este lead?",
            "criteria": { ... }
        },
        "perfil_maturidade": { "type": "choice", ... },
        "perda_conversao_local": { "type": "noul", ... },
        "urgencia_presenca": { "type": "score", ... }
    }
}
```

### Análise de Evidência e Validação Estatística
- **Evidência Comprovada:** O Jev classifica com consistência lógica (ex.: studios de pilates com ambiente requintado recebem consistentemente `combo_maps_tour360_950` ou `vocacao_update_980`).
- **Limitação Observada:** Não há evidência de loop de retroalimentação estatística histórica (machine learning supervisionado fechado com taxa de conversão real). O modelo opera como um classificador semântico especialista de alto nível, mas a conversão em vendas dependeu fortemente da qualidade do gancho da mensagem e do follow-up humano.
