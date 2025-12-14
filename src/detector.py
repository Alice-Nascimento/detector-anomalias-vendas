"""
Módulo de detecção de anomalias para o projeto de vendas.
"""

from sklearn.ensemble import IsolationForest


def detectar_anomalias(dados_modelo, contamination=0.02):

    # Cria o modelo Isolation Forest
    modelo = IsolationForest(contamination=contamination, random_state=42)
    # Treina o modelo e prediz anomalias (-1 = anômalo, 1 = normal)
    anomalia = modelo.fit_predict(dados_modelo)
    # Converte a saída para formato intuitivo: -1 → 1, 1 → 0
    anomalia = [1 if x == -1 else 0 for x in anomalia]
    return anomalia
