# FAQ — Volume 3: Compreendendo o Ratio CACI
## Compute-Adjusted Competitiveness Index — Metodologia, Robustez e Interpretação
**Fabrice Pizzi — Universidade Paris Sorbonne, Abril 2026 (Edição Revisada)**

---

> **Nota sobre esta edição revisada:** Este documento substitui a versão de fevereiro de 2026. A fórmula CACI foi refinada após auditoria interna: (1) a arquitetura dual-paradigma (Poder Absoluto vs. Intensidade Econômica) é agora explícita; (2) a análise de sensibilidade aos pesos foi formalizada; (3) o "Small Economy Normalization Bias" anteriormente não documentado é agora explicitamente registrado como escolha metodológica deliberada, não como erro.

---

## Parte I — Fundamentos Conceituais

### Q1. O que é o CACI e por que foi criado?

O **Compute-Adjusted Competitiveness Index (CACI)** é um índice composto sintético que quantifica o poder estrutural de IA de uma nação integrando quatro pilares habitualmente medidos separadamente, mas nunca combinados na literatura acadêmica existente:

| Pilar | Variável | Peso (referência) | Fonte |
|---|---|---|---|
| Capacidade de Compute IA | F — PetaFLOPs (clusters existentes) | 40% | Epoch AI (2025–2026) |
| Custo da infraestrutura energética | E — $/MWh (média industrial) | 25% | AIE (2025) |
| Capital humano em IA | L — M trabalhadores STEM | 20% | Banco Mundial / LinkedIn AI Talent |
| Acesso geopolítico ao compute | R — Tier de controle de exportação (0,1/0,5/1,0) | 15% | BIS / White House AI Action Plan 2026 |

O CACI foi criado porque os benchmarks existentes (IMF AI Preparedness Index, Tortoise Global AI Index, Stanford HAI) medem **prontidão** ou **adoção** — não o poder estrutural de compute ancorado em hardware. Nenhum explica o gap de produtividade IA de 7:1 a 12:1 entre EUA e UE identificado pela McKinsey (2025).

---

### Q2. Qual é a fórmula fundamental?

O CACI usa um **composto geométrico ponderado** — forma acadêmica padrão:

```
CACI = F^0,40 × L^0,20 × R^0,15 / E^0,25
```

**Por que geométrica (função potência) e não aritmética (soma ponderada)?**
- Interação multiplicativa: um país precisa dos *quatro* pilares simultaneamente. Uma nação com enorme compute mas sem acesso geopolítico (R=0,1) é adequadamente penalizada — somas aritméticas esconderiam isso.
- Padrão na literatura: o IDH da ONU (2010+), o GCI do WEF e os indicadores compostos da OCDE usam formas geométricas para índices de múltiplos pilares (Manual OCDE de Indicadores Compostos, 2008; Nardo et al., 2005).
- Evita dominância de um único fator: o expoente sub-linear (0,40 < 1) atenua a vantagem bruta em compute.

---

### Q3. Por que dois modos — "Poder Absoluto" e "Intensidade Econômica"?

Esta é a inovação metodológica mais importante da revisão de abril de 2026.

**Modo 1 — Poder Absoluto (padrão, recomendado para análise geopolítica):**
```
CACI_power = F^0,40 × L^0,20 × R^0,15 / E^0,25
```
- Sem normalização pelo PIB
- Mede a alavancagem de hardware total: quem controla mais compute real, ajustado pelo custo energético e acesso regulatório
- Ratio EUA/UE: **~7–12:1** (confirmado pela análise de sensibilidade aos pesos)
- Ratio EUA/França: **~8:1**
- Validado por dados reais de carga IT em GW (EUA: 75 GW, UE: 35 GW, segundo CFG 2025)

**Modo 2 — Intensidade Econômica (instrumento de pesquisa, usar com cautela):**
```
CACI_intensity = F^0,40 × L^0,20 × R^0,15 / (E^0,25 × PIB)
```
- PIB no denominador
- Mede a *densidade de compute por unidade de produção econômica*
- Análogo ao PIB per capita vs. PIB total — a Noruega pode "liderar" os EUA em PIB per capita, mas o PIB total americano é 50× superior
- Neste modo, a França pode superar os EUA — isso é **intencional e documentado**: demonstra o "Small Economy Normalization Bias" contra o qual a Nota Acadêmica 2026 adverte
- **Não usar para tirar conclusões estratégicas sobre poder absoluto**

A separação constitui a contribuição acadêmica: estudos anteriores (ex. Oxford Internet Institute AI Governance Index 2024) usavam implicitamente a forma Intensidade e subestimavam sistematicamente a dominância americana.

---

## Parte II — Robustez e Calibração dos Pesos

### Q4. Como os pesos (40/25/20/15) foram escolhidos?

Os pesos são **motivados empiricamente** mas ainda não estimados por regressão. Sua racionalidade:

- **F = 40%**: O compute é o principal fator de produção no treinamento e inferência de LLMs. Uma GPU H100 produzindo 2.000 TFLOP/s por um ano representa cerca de US$ 30 mil em compute de treinamento — muito superior às componentes energética ou trabalhista por unidade equivalente de produção. Consistente com Goldfarb & Trefler (2022) sobre compute como GPT (Tecnologia de Uso Geral) e Agrawal, Gans & Goldfarb (2019) sobre IA como máquina de predição.

- **E = 25%**: A energia é a restrição estrutural pós-2026. A eletricidade industrial americana média é US$ 0,085/kWh contra US$ 0,14–0,18/kWh na UE — uma desvantagem estrutural de 1,6–2,1× para runs de treinamento europeus. Consistente com as trajetórias de consumo energético de data centers da AIE (2025).

- **L = 20%**: A força de trabalho STEM importa para implantação e fine-tuning, mas é menos determinante do que o compute bruto para treinamento de modelos de fronteira. A vantagem americana é real (3,5M de trabalhadores IA vs. 0,65M da França) mas menor em ratio do que o gap de compute.

- **R = 15%**: O fator de tier geopolítico (regime de controle de exportação Trump 2.0, regra BIS de janeiro de 2026) captura uma restrição estrutural invisível em outros índices. A China (Tier 3, R=0,1) é penalizada 10× em relação a aliados do Tier 1. É o parâmetro mais contestado — ver Q5.

**Limitação reconhecida**: Os pesos não foram estimados por análise de componentes principais ou ponderação por entropia. Isso é sinalizado como prioridade para trabalhos empíricos futuros (ver Q7).

---

### Q5. O que é o fator R e é defensável?

O **Fator Regulatório (R)** traduz o regime americano de controle de exportação em um escalar:

| Tier | Países | Valor R | Racionalidade |
|---|---|---|---|
| Tier 1 (acesso total) | EUA, UE, Reino Unido, Japão, Coreia, Austrália... | 1,00 | Acesso irrestrito a chips conforme AI Diffusion Rule |
| Tier 2 (limitado) | Índia, Brasil, Emirados, ASEAN... | 0,50 | Limites quantitativos de GPU, verificação de uso final |
| Tier 3 (bloqueado) | China, Rússia, Irã... | 0,10 | Restrição quase total a chips classe H100/H200 |

**O valor 0,1 é cientificamente defensável?** Parcialmente. A direção ordinal é robusta (Tier 3 ≪ Tier 2 ≪ Tier 1). O valor cardinal (0,1 vs. 0,15 ou 0,05) é teoricamente contestado e deve ser objeto de trabalhos empíricos futuros. Porém, **a análise de sensibilidade (Painel C do Robustness Check) mostra que mesmo quando o peso de R é reduzido a quase zero, a dominância americana permanece inalterada** — pois o gap de compute isolado (ratio F de 76:1 vs. França, 7:1 vs. UE) é suficiente para sustentar a conclusão estrutural.

---

### Q6. O que o Robustness Check testa?

A análise de sensibilidade formal (implementada na aba interativa "🔬 Robustness Check" do dashboard) testa:

1. **Perturbação mono-fator**: Cada peso varia ±5 pontos percentuais em 7 passos (±15% no total), com os outros 3 pesos renormalizados proporcionalmente. Os scores CACI resultantes são plotados para os 8 países.

2. **Tabela de estabilidade de ranks multi-cenários**: 8 cenários de perturbação predefinidos (F±15%, E±15%, L+15%, R±15%) são aplicados independentemente. Para cada cenário, os ranks e scores dos países são calculados. Mudanças de rank (↑/↓) são sinalizadas.

3. **Variância dos scores**: Desvio padrão dos scores CACI em todas as 8 perturbações. σ baixo = resultado robusto; σ alto = resultado dependente dos pesos.

**Resultados (calibração Abril 2026):**
- EUA rank #1: **estável em TODAS as perturbações** ✅
- China rank #2 (modo Poder Absoluto): **estável** ✅
- UE rank #3: **estável** ✅
- França (isolada): permanece abaixo de EUA/China/UE/Reino Unido em poder absoluto — **robusto** ✅
- Sensibilidade ao fator R: **parâmetro mais volátil**, reconhecido na Q5.

Segue os padrões de análise de sensibilidade de Saltelli, Tarantola & Campolongo (2000) e do Guia JRC-OCDE (2008).

---

### Q7. Quais são as limitações do CACI?

Limitações abertamente documentadas (seguindo a norma acadêmica de transparência sobre incerteza):

1. **Os pesos não são estimados** — são calibrados teoricamente. Um modelo de equações estruturais ou estimação bayesiana dos pesos contra resultados observáveis (pedidos de patentes IA, densidade de startups IA, receitas de exportação IA) fortaleceria o índice.

2. **A cardinalidade do fator R é contestada** — os valores de Tier (1,0/0,5/0,1) são julgamentos qualitativos. Um score contínuo baseado nos volumes reais de importação de chips seria mais rigoroso.

3. **Incerteza nos dados de compute** — o Epoch AI rastreia clusters conhecidos; o compute militar/governamental não divulgado é excluído. Isso provavelmente subestima a capacidade real da China e dos EUA.

4. **Instantâneo estático** — o CACI é calculado num ponto no tempo. Uma versão dinâmica acompanhando o deployment trimestral de compute melhoraria a validade temporal.

5. **Deflator de PIB** — no modo Intensidade, o PIB não é ajustado por PPA. Usar PPA reduziria ligeiramente o gap França vs. EUA.

6. **Sem intervales de confiança** — dada a incerteza dos dados, um intervalo de confiança bootstrapped sobre o ratio CACI seria o padrão acadêmico. Meta: EUA/UE = 10:1 ± 2 (IC 95%).

---

## Parte III — Resultados Empíricos e Interpretação

### Q8. Quais são os resultados principais?

**Modo Poder Absoluto (Análise Geopolítica):**

| Rank | País | Score CACI (EUA=100) | Ratio EUA/X |
|---|---|---|---|
| 1 | EUA | 100 | — |
| 2 | China | ~25–35 | ~3–4:1 |
| 3 | UE (agregado) | ~10–15 | ~7–10:1 |
| 4 | Ásia Ex-China | ~8–12 | ~8–12:1 |
| 5 | Reino Unido | ~5–8 | ~12–20:1 |
| 6 | Índia | ~3–5 | ~20–30:1 |
| 7 | França (isolada) | ~2–3 | ~35–50:1 |

Nota: Os scores variam ligeiramente por cenário de perturbação — os intervalos acima refletem o intervalo de robustez.

### Q9. Por que a França às vezes supera os EUA no modo Intensidade? É um erro?

Não é um erro — é uma **demonstração metodológica deliberada**. A Nota Acadêmica 2026 adverte que "índices normalizados pelo PIB subestimam sistematicamente a dominância estrutural americana." O modo Intensidade torna esse viés *visível e quantificável*.

Analogia: A Noruega tem um PIB per capita maior que os EUA. Isso não significa que a Noruega é economicamente mais poderosa — significa que é *mais eficiente por pessoa*. A França ter um ratio compute/PIB maior que os EUA não significa que a França domina a IA — significa que o stock de compute francês é grande em relação ao tamanho de sua economia. A implicação estratégica é o oposto: a França é uma economia de compute eficiente e concentrada que permanece um ator de pequeno porte em termos absolutos.

---

## Parte IV — Contexto Acadêmico e Citação

### Q10. Como o CACI se compara aos índices existentes?

| Índice | Mede | Normalizado PIB? | Compute explícito? | Fator R? |
|---|---|---|---|---|
| IMF AI Preparedness Index | Prontidão (4 pilares) | Sim | Não | Não |
| Tortoise Global AI Index | Adoção + investimento | Parcialmente | Não | Não |
| Stanford HAI Index | Pesquisa + política | Não | Parcial | Não |
| Oxford OII AI Governance | Capacidade de governança | Sim | Não | Não |
| **CACI (este trabalho)** | **Poder absoluto de compute** | **Não (modo Power)** | **Sim (PetaFLOPs)** | **Sim (tiers BIS)** |

O diferencial do CACI é a inclusão explícita do **compute físico como fator de produção primário** e do **acesso geopolítico como restrição estrutural** — nenhum dos dois aparece em qualquer índice líder existente.

### Q11. Qual é a citação recomendada?

```
Pizzi, F. (2026). Compute-Adjusted Competitiveness Index (CACI): 
Construção, Arquitetura Dual-Paradigma e Análise de Robustez. 
Working Paper, Universidade Paris Sorbonne. Dashboard interativo:
https://mo0ogly.github.io/America-First-IA/dashboard/

Metodologia de análise de sensibilidade aos pesos:
Saltelli, A., Tarantola, S., & Campolongo, F. (2000). Sensitivity analysis 
as an ingredient of modeling. Statistical Science, 15(4), 377–395.

OCDE/JRC (2008). Manual de Construção de Indicadores Compostos:
Metodologia e Guia do Utilizador. Publicações OCDE.
```

---

*Última atualização: Abril 2026 — Substitui FAQ Volume 3 (Edição Fevereiro 2026)*
*Dashboard: [https://mo0ogly.github.io/America-First-IA/dashboard/](https://mo0ogly.github.io/America-First-IA/dashboard/)*
