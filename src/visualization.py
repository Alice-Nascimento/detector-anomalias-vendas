"""
Módulo de visualização de dados para o projeto de detecção de anomalias em vendas.

- grafico_dispersao(df): gráfico de dispersão da quantidade vendida vs total da venda, destacando anomalias
- grafico_barras(df): gráfico de barras mostrando a distribuição de anomalias por produto.

Observação:
- Os gráficos são salvos na pasta 'outputs' e também exibidos na tela.
"""
import matplotlib.pyplot as plt  # Para criação de gráficos e visualizações
import seaborn as sns  # Para visualização de dados com estilo aprimorado
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir, "..", "outputs")
os.makedirs(output_dir, exist_ok=True)
sns.set_theme(style="whitegrid")


def grafico_dispersao(df):
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
    plt.ylim(df['total_venda'].min() - 100, df['total_venda'].max() + 1000)
    plt.xlim(df['quantidade'].min() - 1, df['quantidade'].max() + 1)
    plt.savefig(os.path.join(output_dir, "grafico_dispersao.png"), dpi=300)
    plt.show()


def grafico_barras(df):
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
    plt.savefig(os.path.join(output_dir, "grafico_barras.png"), dpi=300)
    plt.show()
