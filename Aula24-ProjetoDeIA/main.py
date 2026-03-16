# main.py
import os
import pandas as pd
from factory.standard_factory import StandardMLFactory
from factory.series_factory import SeriesFactory
from core.orchestrator import AnaliseDadosIA

def main():
    # 1. Configuração de caminhos e dados de exemplo
    # Criando uma pasta data/raw se não existir para evitar erros
    os.makedirs('data/raw', exist_ok=True)
    
    csv_path = 'data/raw/dataset_exemplo.csv'
    
    # Criando um DataFrame fictício para teste
    data = {
        'data_registro': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'valor_venda': [10, 20, np.nan, 40, 50, 60, 70, 80, 90, 100],
        'categoria': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B'],
        'target': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    }
    pd.DataFrame(data).to_csv(csv_path, index=False)

    print("--- Iniciando Pipeline de Análise de IA ---")

    # 2. Exemplo com StandardMLFactory (Dados Tabulares)
    print("\n[Execução 1] Utilizando Fábrica Padrão (Tabular):")
    factory_tabular = StandardMLFactory()
    ia_tabular = AnaliseDadosIA(factory_tabular)
    
    try:
        X_train, X_test, y_train, y_test = ia_tabular.executar_pipeline(csv_path, target='target')
        print(f"Sucesso! Treino: {X_train.shape}, Teste: {X_test.shape}")
    except Exception as e:
        print(f"Erro no pipeline tabular: {e}")

    print("-" * 40)

    # 3. Exemplo com SeriesFactory (Séries Temporais)
    print("\n[Execução 2] Utilizando Fábrica de Séries Temporais:")
    factory_temporal = SeriesFactory()
    ia_temporal = AnaliseDadosIA(factory_temporal)
    
    try:
        # Note que o orquestrador chama os mesmos métodos, 
        # mas o comportamento interno (limpeza/split) muda.
        X_t, X_v, y_t, y_v = ia_temporal.executar_pipeline(csv_path, target='target')
        print(f"Sucesso! Janela temporal aplicada. Treino: {X_t.shape}")
    except Exception as e:
        print(f"Erro no pipeline temporal: {e}")

if __name__ == "__main__":
    import numpy as np # Importado aqui para a criação do dado fictício
    main()