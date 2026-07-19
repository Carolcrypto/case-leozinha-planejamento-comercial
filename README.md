# Case Técnico - Planejamento Comercial Leozinha

##  Sobre o Projeto

Este projeto foi desenvolvido como solução para um case técnico de planejamento comercial, com o objetivo de identificar os clientes com maior potencial para ações comerciais através de uma análise baseada em dados.

A solução utiliza informações de cadastro de clientes e histórico de transações para criar uma classificação dos clientes mais relevantes comercialmente, entregando uma lista dos **100 clientes prioritários** para atuação da equipe comercial.

---

##  Objetivo

O objetivo da análise foi responder:

- Quais clientes possuem maior potencial comercial?
- Como priorizar clientes para campanhas?
- Quais clientes apresentam maior valor para o negócio?
- Como transformar dados transacionais em uma estratégia comercial?

Para responder essas perguntas foi desenvolvido um modelo de priorização utilizando a metodologia **50/30/20**.

---

##  Metodologia 50/30/20

O modelo de pontuação foi criado considerando três indicadores principais:

### 50% - Volume Financeiro

Avalia o valor total movimentado pelo cliente no período analisado.

Clientes com maior volume financeiro recebem maior peso na classificação.

### 30% - Frequência de Transações

Considera a quantidade de transações realizadas pelo cliente.

Esse indicador representa o nível de recorrência e utilização da solução.

### 20% - Ticket Médio

Avalia o valor médio das operações realizadas pelo cliente.

Esse indicador identifica clientes com maior valor agregado por operação.

---

##  Modelo de Score

O ranking foi criado através da combinação dos indicadores:

```
Score Final =

(Score Volume × 50%)

+

(Score Frequência × 30%)

+

(Score Ticket Médio × 20%)
```

Após o cálculo, os clientes foram ordenados de acordo com o maior score final, gerando a lista dos **100 clientes prioritários**.

---

##  Dados Utilizados

Foram utilizadas duas bases principais:

### Cadastro de Clientes

Contendo informações como:

- Identificação do cliente
- Nome fantasia
- Segmento
- Porte
- Estado
- Cidade
- Taxa atual

### Histórico de Transações

Contendo informações como:

- Identificação da transação
- Cliente
- Data da operação
- Valor bruto
- Tipo de pagamento
- Bandeira
- Parcelamento

---

##  Dashboard

Foi desenvolvido um dashboard interativo utilizando Streamlit para apresentação dos resultados.

O dashboard apresenta:

- Quantidade total de clientes analisados
- Volume financeiro total
- Quantidade de transações
- Ticket médio
- Ranking dos 100 clientes prioritários
- Análise de volume por segmento
- Análise de volume por estado

---

##  Tecnologias Utilizadas

- Python
- Pandas
- Streamlit
- Excel
- Git/GitHub

---

## 📁 Estrutura do Projeto

```
CaseLeoMadeiras

├── app.py
├── analise.py
├── case_leomadeiras.xlsx
├── requirements.txt
├── README.md
└── imagens/
```

---


##  Resultado Final

A solução entrega uma lista priorizada dos **100 clientes com maior potencial comercial**, utilizando critérios objetivos baseados em comportamento transacional.

O modelo permite direcionar esforços comerciais considerando:

- Maior geração de receita
- Maior frequência de utilização
- Maior valor médio por operação

Dessa forma, a equipe comercial consegue tomar decisões mais estratégicas e direcionar campanhas para os clientes com maior potencial de retorno.

## Autor
Projeto desenvolvido por Carolina Fagundes como parte do processo seletivo para a vaga de Analista de Dados / BI do Grupo Leo Madeiras.
