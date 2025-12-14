
from src.preprocessing import criar_dados_simulados, preparar_dados_modelo
from src.detector import detectar_anomalias
from src.visualization import grafico_dispersao, grafico_barras

# Criar e preparar os dados
df = criar_dados_simulados()
dados_modelo = preparar_dados_modelo(df)

# Detectar anomalias
df['anomalia'] = detectar_anomalias(dados_modelo)
print("Total de anomalias detectadas:", df['anomalia'].sum())
print(df[df['anomalia'] == 1])

# Gerar gráficos
grafico_dispersao(df)
grafico_barras(df)
