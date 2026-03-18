# # main.py
# import os
# import pandas as pd
# from factory.standard_factory import StandardMLFactory
# from factory.series_factory import SeriesFactory
# from core.orchestrator import AnaliseDadosIA

# def main():
#     # 1. Configuração de caminhos e dados de exemplo
#     # Criando uma pasta data/raw se não existir para evitar erros
#     os.makedirs('data/raw', exist_ok=True)
    
#     csv_path = 'data/raw/dataset_exemplo.csv'
    
#     # Criando um DataFrame fictício para teste
#     data = {
#         'data_registro': pd.date_range(start='2023-01-01', periods=10, freq='D'),
#         'valor_venda': [10, 20, np.nan, 40, 50, 60, 70, 80, 90, 100],
#         'categoria': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B'],
#         'target': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
#     }
#     pd.DataFrame(data).to_csv(csv_path, index=False)

#     print("--- Iniciando Pipeline de Análise de IA ---")

#     # 2. Exemplo com StandardMLFactory (Dados Tabulares)
#     print("\n[Execução 1] Utilizando Fábrica Padrão (Tabular):")
#     factory_tabular = StandardMLFactory()
#     ia_tabular = AnaliseDadosIA(factory_tabular)
    
#     try:
#         X_train, X_test, y_train, y_test = ia_tabular.executar_pipeline(csv_path, target='target')
#         print(f"Sucesso! Treino: {X_train.shape}, Teste: {X_test.shape}")
#     except Exception as e:
#         print(f"Erro no pipeline tabular: {e}")

#     print("-" * 40)

#     # 3. Exemplo com SeriesFactory (Séries Temporais)
#     print("\n[Execução 2] Utilizando Fábrica de Séries Temporais:")
#     factory_temporal = SeriesFactory()
#     ia_temporal = AnaliseDadosIA(factory_temporal)
    
#     try:
#         # Note que o orquestrador chama os mesmos métodos, 
#         # mas o comportamento interno (limpeza/split) muda.
#         X_t, X_v, y_t, y_v = ia_temporal.executar_pipeline(csv_path, target='target')
#         print(f"Sucesso! Janela temporal aplicada. Treino: {X_t.shape}")
#     except Exception as e:
#         print(f"Erro no pipeline temporal: {e}")

# if __name__ == "__main__":
#     import numpy as np # Importado aqui para a criação do dado fictício
#     main()

import pandas as pd
import numpy as np
import os
from core.orchestrator import AnaliseDadosIA
from factory.standard_factory import StandardMLFactory
from factory.series_factory import SeriesFactory

# 1. Criação do Ambiente de Teste
def gerar_dados_teste():
    os.makedirs('data/raw', exist_ok=True)
    
    # Projeto Crédito (Tabular)
    clientes = pd.DataFrame({
        'idade': [25, 30, np.nan, 45, 50, 22, 33, 40, 28, 35],
        'score': [700, 800, 650, np.nan, 900, 500, 600, 750, 850, 780],
        'categoria': ['A', 'B', 'A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
        'aprovado': [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    })
    clientes.to_csv('data/raw/dados_clientes.csv', index=False)
    
    # Projeto Bolsa (Temporal)
    mercado = pd.DataFrame({
        'data': pd.date_range(start='2024-01-01', periods=10),
        'preco': [100.0, 101.5, np.nan, 102.0, 105.0, 104.5, 106.0, 108.0, 107.5, 110.0],
        'target': [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]
    })
    mercado.to_csv('data/raw/dados_mercado.csv', index=False)
    print("Arquivos de teste gerados em data/raw/\n")

# 2. Implementação da Injeção de Dependência
def executar_exemplo(cenario, fabrica, path, target):
    print(f"--- Executando Cenário: {cenario} ---")
    try:
        # O segredo: Injetamos a fábrica no Orquestrador
        orquestrador = AnaliseDadosIA(fabrica)
        
        # Definindo colunas (no mundo real isso viria de uma config)
        num_cols = ['idade', 'score'] if 'clientes' in path else ['preco']
        cat_cols = ['categoria'] if 'clientes' in path else []
        
        X_train, X_test, y_train, y_test = orquestrador.executar_pipeline(
            path, target, num_cols, cat_cols
        )
        
        print(f"Sucesso! Treino: {X_train.shape}, Teste: {X_test.shape}")
        
        # Prova Real para o Cenário Temporal
        if "Bolsa" in cenario:
            ultimo_treino = X_train.index[-1]
            primeiro_teste = X_test.index[0]
            print(f" Validação Sequencial: Fim Treino Index({ultimo_treino}) -> Início Teste Index({primeiro_teste})")
            if primeiro_teste > ultimo_treino:
                print("Prova Real: Cronologia respeitada (sem embaralhamento).")
                
    except Exception as e:
        print(f"Erro no pipeline {cenario}: {e}")
    print("-" * 40 + "\n")

# 3. Prova Real (Bloco Principal)
if __name__ == "__main__":
    # Garante que os dados existem
    gerar_dados_teste()
    
    # Cenário A: Fábrica Padrão (Tabular)
    executar_exemplo(
        "Projeto Crédito (Estático)", 
        StandardMLFactory(), 
        'data/raw/dados_clientes.csv', 
        'aprovado'
    )
    
    # Cenário B: Fábrica de Séries Temporais (Cronológico)
    executar_exemplo(
        "Projeto Bolsa de Valores (Temporal)", 
        SeriesFactory(), 
        'data/raw/dados_mercado.csv', 
        'target'
    )