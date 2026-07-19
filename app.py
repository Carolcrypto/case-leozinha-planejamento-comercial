# Código utilizado no app.py

Este arquivo é responsável pela criação do dashboard interativo utilizando Streamlit.

O objetivo é apresentar os resultados da análise comercial de forma visual e facilitar a interpretação dos dados para tomada de decisão.

A aplicação realiza as seguintes etapas:

## 1. Carregamento dos dados

O dashboard utiliza a função `carregar_dados()` criada no arquivo `analise.py`, que retorna a base tratada com os indicadores e score comercial calculado.

---

## 2. Apresentação dos indicadores principais (KPIs)

São exibidos indicadores gerais do negócio:

- Quantidade de clientes analisados;
- Volume financeiro total movimentado;
- Quantidade total de transações;
- Ticket médio das operações.

Esses indicadores permitem uma visão geral da base analisada.

---

## 3. Ranking de clientes

O dashboard apresenta os clientes com maior pontuação utilizando o score 50/30/20.

São exibidos:

- Top 10 clientes prioritários;
- Ranking dos melhores scores;
- Lista final dos 100 clientes prioritários para campanhas comerciais.

---

## 4. Análises comerciais

Foram adicionadas análises complementares para apoiar a tomada de decisão:

- Volume financeiro por segmento;
- Volume financeiro por estado.

Essas análises permitem identificar quais perfis de clientes possuem maior representatividade comercial.

---

## 5. Lista de campanha

A aplicação gera uma tabela final contendo os 100 clientes prioritários ordenados pelo score comercial.

Foi criada uma coluna de ranking de 1 a 100 para facilitar a priorização das ações comerciais.

---

## Tecnologias utilizadas

- Streamlit → construção do dashboard interativo;
- Pandas → manipulação e apresentação dos dados;
- Python → desenvolvimento da solução.

import streamlit as st
from analise import carregar_dados

st.set_page_config(
    page_title="Case Leozinha",
    layout="wide"
)

df = carregar_dados()

st.title("📊 Case Técnico - Planejamento Comercial")

st.write(
    """
    Dashboard para definição dos clientes prioritários
    utilizando a metodologia de score 50/30/20.
    """
)

# ==========================
# KPIs
# ==========================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Clientes",
    len(df)
)

c2.metric(
    "Volume Total",
    f"R$ {df['volume'].sum():,.0f}"
)

c3.metric(
    "Transações",
    int(df["transacoes"].sum())
)

c4.metric(
    "Ticket Médio",
    f"R$ {df['ticket_medio'].mean():,.2f}"
)

st.divider()

# ==========================
# TOP 10
# ==========================

st.subheader("🏆 Top 10 Clientes")

top10 = df.sort_values(
    "score_final",
    ascending=False
).head(10)

st.dataframe(top10)

st.divider()

# ==========================
# Ranking
# ==========================

st.subheader("📈 Ranking dos 20 melhores")

grafico = (
    df.sort_values(
        "score_final",
        ascending=False
    )
    .head(20)
    .set_index("nome_fantasia")
)

st.bar_chart(grafico["score_final"])

st.divider()

# ==========================
# Segmentos
# ==========================

st.subheader("Segmentos com maior volume")

segmento = (
    df.groupby("segmento")["volume"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(segmento)

st.divider()

# ==========================
# Estados
# ==========================

st.subheader("Volume por Estado")

estado = (
    df.groupby("estado")["volume"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(estado)

st.divider()

# ==========================
# Campanha
# ==========================

st.subheader("🎯 Top 100 Clientes Prioritários")

campanha = (
    df.sort_values(
        "score_final",
        ascending=False
    )
    .head(100)
    .copy()
)

# Criar ranking de 1 a 100
campanha.insert(
    0,
    "Ranking",
    range(1, 101)
)

st.dataframe(
    campanha,
    use_container_width=True
)
