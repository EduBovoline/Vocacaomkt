# Medições de velocidade (base dos números usados nos anúncios)

Ferramenta: Lighthouse (mesmo motor do PageSpeed Insights), modo **celular**, rede simulada 4G lenta (padrão do Lighthouse).
Data: 20/10/2026. Teste feito no computador do Edu, uma rodada por URL.

| Página | Nota | FCP | LCP | Speed Index | TTI |
|---|---|---|---|---|---|
| Safety First **antigo** (safetyfirst.com.br, no ar hoje) | 60 | 3,3 s | 18,3 s | **9,5 s** | 24,5 s |
| Safety First **novo** (vocacao.digital/safety-first) | 70 | 3,1 s | 7,6 s | **3,1 s** | 7,6 s |
| Maçã d'Amor **novo** (vocacao.digital/maca-de-amor) | 86 | 1,9 s | 2,6 s | **4,8 s** | 2,9 s |
| Maçã d'Amor **antigo** | não medido (URL antiga não informada) | | | | |

## O que dá para afirmar nos anúncios

- **Safety First:** Speed Index de 9,5 s para 3,1 s = **3x mais rápido no celular** (9,5 / 3,1 = 3,06). Seguro e reproduzível.
- **Maçã d'Amor:** não existe medição do site antigo. **Não usar número de velocidade.** O argumento é o pedido direto no WhatsApp.

## O que NÃO dá para afirmar

- **"Abre em 0,4 s" / "menos de 0,5 s":** nenhuma das páginas medidas chegou perto disso. O menor LCP foi 2,6 s (Maçã). Em rede boa e aparelho bom pode ser mais rápido, mas não há medição que sustente o número.
- **"Demorava 6 s":** o site antigo da Safety First mediu LCP de 18,3 s e Speed Index de 9,5 s. O "6 s" não tinha base.
- Isso também vale para o texto do site (`README`, `index.html`, `vocacao-update.html`: "<0,5 s", "0.4s"), que deve ser revisado antes de ser prometido em anúncio.

## Oportunidade

O site novo da Safety First tem LCP de 7,6 s por causa do herói cinematográfico (vídeo/animação pesada). Otimizar isso melhora nota, conversão e permite uma promessa de velocidade mais forte.
