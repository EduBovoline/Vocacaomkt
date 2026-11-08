# 🎨 MANUAL DE IDENTIDADE VISUAL & BRANDBOOK APLICADO — VOCAÇÃO
> **Versão Oficial 2026/2027**  
> **Aplica-se a:** Relatórios de Prospecção (HTML/PDF), Dossiês Internos, Templates de E-mail, Landing Pages e Comunicação Comercial.

---

## 🏛️ 1. POSICIONAMENTO & MANIFESTO DA MARCA

* **Tagline Principal:**  
  > *"Sua empresa já é confiável. Online, ela precisa parecer."*
* **Manifesto Operacional:**  
  * *Estrutura antes do marketing.*  
  * *Confiança antes do tráfego.*  
  * *Clareza antes da venda.*  
  * *Marketing chama. Estrutura sustenta.*
* **Compromisso Visual:**  
  Estilo editorial, sobriedade corporativa, minimalismo suíço, sem cores berrantes de "agência de marketing digital genérica".

---

## 🎨 2. PALETA CROMÁTICA OFICIAL (DESIGN TOKENS — PADRÃO MARCENARIA SUCESSO)

| Variável CSS | Código Hex | Papel na Interface |
| :--- | :---: | :--- |
| `--color-primary` | `#061B28` | **Dark Navy Profundo:** Headers institucionais, títulos nobres, topbars e textos de alto contraste. |
| `--color-accent` | `#E5B910` | **Dourado Solar Vocação:** Acentos nobres, estrelas de avaliação, botões principais e bordas de destaque. |
| `--color-accent-soft` | `#FCF9EB` | **Dourado Suave / Creme:** Fundo de cartões em destaque, badges de atenção e seleções suaves. |
| `--color-positive` | `#0B5E47` | **Verde Esmeralda Vocação:** Ícones de confirmação, selos de garantia e badges positivos. |
| `--color-bg` | `#FAFAF8` | **Off-White Quente Editorial:** Fundo suave padrão de todas as páginas e relatórios. |
| `--color-surface` | `#FFFFFF` | **Branco Puro:** Fundo de cartões, caixas de diagnóstico e tabelas. |
| `--color-border` | `#E2E8E5` | **Borda Suave:** Linhas divisórias e contornos sutis de cards (1px solid). |
| `--color-text-muted`| `#5A625F` | **Texto Secundário:** Subtítulos, notas explicativas, fontes de dados e metadados. |
| `--color-negative`  | `#9B2335` | **Vermelho Carmim:** Gargalos identificados, status críticos e alertas de conversão. |
| `--color-opportunity`| `#1D4E89`| **Azul Oportunidade:** Alertas de crescimento, diferenciais e tags informativas. |

---

## 🖋️ 3. TIPOGRAFIA OFICIAL

```html
<!-- Import Google Fonts Oficial -->
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
```

* **Display / Títulos (H1, H2, Números Grandes):**  
  `font-family: 'Fraunces', Georgia, serif;`  
  *Uso:* Traz peso editorial, tradição e sofisticação de consultoria corporativa.
* **Corpo / Interface / Tabelas (P, Li, Input, Buttons):**  
  `font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;`  
  *Uso:* Clareza geométrica, alta legibilidade no celular e tom moderno sem ruído.

---

## 📐 4. COMPONENTES VISUAIS PADRONIZADOS

### A. Botão Primário de Conversão (CTA)
```css
.btn-vocacao {
  display: inline-block;
  background-color: #0B5E47;
  color: #FFFFFF !important;
  font-family: 'DM Sans', sans-serif;
  font-size: 15px;
  font-weight: 600;
  text-decoration: none;
  padding: 14px 28px;
  border-radius: 6px;
  border: 1px solid #084937;
  box-shadow: 0 2px 4px rgba(11, 94, 71, 0.15);
  transition: all 0.2s ease;
}
.btn-vocacao:hover {
  background-color: #084937;
  transform: translateY(-1px);
}
```

### B. Card de Destaque / Estatística
```css
.card-stat {
  background-color: #FFFFFF;
  border: 1px solid #E2E8E5;
  border-radius: 8px;
  padding: 20px;
}
.stat-number {
  font-family: 'Fraunces', serif;
  font-size: 32px;
  font-weight: 700;
  color: #0B5E47;
}
.stat-label {
  font-family: 'DM Sans', sans-serif;
  font-size: 13px;
  color: #5A625F;
  margin-top: 4px;
}
```

### C. Logotipo Oficial em SVG (Versão Dark / Fundo Claro)
```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4001.88 3715.4" width="24" height="24" fill="none">
  <path d="M45.03 0.01l1213.22 0 1387.23 2638.86c-277.85,525.48 -495.08,935.8 -517.87,978.08 -64.91,120.45 -134.89,140.51 -212.88,3.18 -632.47,-1181.24 -1264.91,-2362.48 -1897.38,-3543.73 -28.66,-49.03 -23.4,-76.94 27.68,-76.4zm2311.4 0l1578.29 0c66.2,0 95.98,9.39 30.56,136.59 -56.81,110.47 -396.78,755.17 -769.29,1460.51l-839.57 -1597.1z" fill="#121816" />
  <rect transform="matrix(0.395693 0.564385 -1.12875 0.791372 3191.31 348.346)" width="275.97" height="1545.42" rx="154.54" ry="154.54" fill="#0B5E47" />
</svg>
```
