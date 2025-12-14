"""
Módulo de pré-processamento de dados para o projeto de detecção de anomalias em vendas. # noqa

Contém funções para:
- Criar dados simulados de vendas
- Inserir anomalias artificiais
- Preparar os dados para o modelo de detecção (seleção de colunas)
"""

import pandas as pd  # Para manipulação e análise de dados tabulares (DataFrames)
import numpy as np  # Para cálculos numéricos e operações com arrays
import random  # Para gerar números e elementos aleatórios


# Função para criar um DataFrame com dados simulados de vendas
def criar_dados_simulados():
    np.random.seed(42)
    datas = pd.date_range(start="2025-01-01", periods=100, freq="D")
    produtos = ['Mouse', 'Teclado', 'Monitor', 'Notebook']
    dados = []

    # Criar 3 vendas por dia para cada data
    for data in datas:
        for _ in range(3):
            produto = random.choice(produtos)
            quantidade = np.random.randint(1, 10)
            preco = round(np.random.uniform(100, 2000), 2)
            total = quantidade * preco
            dados.append([data, produto, quantidade, preco, total])

    # Cria o DataFrame com colunas nomeadas
    df = pd.DataFrame(dados, columns=['data', 'produto', 'quantidade', 'preco_unitario', 'total_venda'])

    # Inserindo anomalias
    df.loc[5, 'total_venda'] = 50000
    df.loc[20, 'quantidade'] = -5
    df.loc[35, 'preco_unitario'] = 0

    # Corrigindo total_venda
    df['total_venda'] = df['quantidade'] * df['preco_unitario']

    return df


# Função para selecionar as colunas que o modelo vai usar
def preparar_dados_modelo(df):
    colunas_modelo = ['quantidade', 'preco_unitario', 'total_venda']  # Apenas colunas numéricas relevantes
    return df[colunas_modelo]  # Retorna subset do DataFrame
