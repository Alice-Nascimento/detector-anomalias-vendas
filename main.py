# Criando dados simulados de vendas

# Importando as bilbiotecas necessárias
import pandas as pd
import numpy as np
import random

# Importando o algoritmo Isolation Forest
from sklearn.ensemble import IsolationForest

# Importando bibliotecas para visualização gráfica
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Garantindo que os números aleatórios sejam os mesmos toda vez
np.random.seed(42)

# Criando datas e tipos de produto
datas = pd.date_range(start="2025-01-01", periods=100, freq="D")
produtos = ['Mouse', 'Teclado', 'Monitor', 'Notebook']

# Geraando os dados
dados = []

for data in datas:
    for _ in range(3):  # 3 vendas por dia
        produto = random.choice(produtos)
        quantidade = np.random.randint(1, 10)
        preco = round(np.random.uniform(100, 2000), 2)
        total = quantidade * preco
        dados.append([data, produto, quantidade, preco, total])

# Criando o DataFrame
df = pd.DataFrame(dados, columns=['data', 'produto', 'quantidade', 'preco_unitario', 'total_venda'])

# Inseririndo anomalias
df.loc[5, 'total_venda'] = 50000
df.loc[20, 'quantidade'] = -5
df.loc[35, 'preco_unitario'] = 0

# Corrigindo total_venda após as alterações
df['total_venda'] = df['quantidade'] * df['preco_unitario']

# Mostrando os primeiros dados
print(df.head())

# Selecionar colunas que o modelo vai analisar
colunas_modelo = ['quantidade', 'preco_unitario', 'total_venda']
dados_modelo = df[colunas_modelo]

# Criando o modelo Isolation Forest
modelo = IsolationForest(contamination=0.02, random_state=42)

# Aplicando o modelo aos dados
df['anomalia'] = modelo.fit_predict(dados_modelo)

# Convertendo: -1 (anômalo) → 1 / 1 (normal) → 0
df['anomalia'] = df['anomalia'].apply(lambda x: 1 if x == -1 else 0)

# Mostrando quantas anomalias foram encontradas
print("Total de anomalias detectadas:", df['anomalia'].sum())

# Mostrando os registros classificados como anômalos
print(df[df['anomalia'] == 1])


# Gráfico de dispersão: Total da venda vs Quantidade vendida
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='quantidade',
    y='total_venda',
    hue='anomalia',
    palette={0: 'blue', 1: 'red'},
    data=df
)
plt.title('Anomalias em Vendas (vermelho = anômalo)')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Total da Venda (R$)')
plt.legend(title='Anomalia')
plt.tight_layout()

# Força o eixo do gráfico a mostrar tudo
plt.ylim(df['total_venda'].min() - 100, df['total_venda'].max() + 1000)
plt.xlim(df['quantidade'].min() - 1, df['quantidade'].max() + 1)

# Salva o gráfico como imagem
plt.savefig('grafico_dispersao.png', dpi=300)
plt.show()

# Gráfico de barras: anomalias por produto
plt.figure(figsize=(8, 5))
sns.countplot(
    x='produto',
    hue='anomalia',
    data=df,
    palette={0: 'blue', 1: 'red'}
)
plt.title('Distribuição de Anomalias por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade de Registros')
plt.legend(title='Anomalia')
plt.tight_layout()


# Salva o gráfico como imagem
plt.savefig('grafico_barras.png', dpi=300)
plt.show()
