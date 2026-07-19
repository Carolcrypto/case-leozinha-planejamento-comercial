## Código usado na analise.py

Este arquivo é responsável pelo tratamento, transformação e análise dos dados utilizados no projeto.

A função `carregar_dados()` realiza as seguintes etapas:

1. Importação das bases de dados:
- Cadastro de clientes (`Cadastro_Clientes`)
- Histórico de transações (`Transacoes`)

2. Integração das informações:
- As duas bases são relacionadas através do campo `id_cliente`, permitindo analisar o comportamento transacional de cada cliente junto com suas características cadastrais.

3. Criação dos indicadores comerciais:
Para cada cliente são calculados:

- **Volume:** soma do valor bruto de todas as transações realizadas.
- **Quantidade de transações:** número total de operações realizadas.
- **Ticket médio:** valor médio das transações.

4. Construção do Score Comercial:
Foi aplicada a metodologia 50/30/20 para gerar uma pontuação de prioridade:

- 50% → Volume financeiro movimentado
- 30% → Frequência de transações
- 20% → Ticket médio

Cada indicador foi normalizado através do ranking percentual (`rank pct=True`) para permitir a comparação entre clientes.

O resultado final é um DataFrame contendo o score comercial de cada cliente, permitindo ordenar e identificar os 100 clientes prioritários para ações comerciais.

    import pandas as pd

def carregar_dados():

    clientes = pd.read_excel(
        "case_leomadeiras.xlsx",
        sheet_name="Cadastro_Clientes"
    )

    transacoes = pd.read_excel(
        "case_leomadeiras.xlsx",
        sheet_name="Transacoes"
    )

    df = transacoes.merge(clientes, on="id_cliente")

    resumo = (
        df.groupby(
            [
                "id_cliente",
                "nome_fantasia",
                "segmento",
                "porte",
                "estado",
                "cidade",
                "taxa_atual_pct"
            ]
        )
        .agg(
            volume=("valor_bruto", "sum"),
            transacoes=("id_transacao", "count"),
            ticket_medio=("valor_bruto", "mean")
        )
        .reset_index()
    )

    resumo["score_volume"] = resumo["volume"].rank(pct=True) * 100
    resumo["score_transacoes"] = resumo["transacoes"].rank(pct=True) * 100
    resumo["score_ticket"] = resumo["ticket_medio"].rank(pct=True) * 100

    resumo["score_final"] = (
        resumo["score_volume"] * 0.5
        + resumo["score_transacoes"] * 0.3
        + resumo["score_ticket"] * 0.2
    )

    return resumo
