#===========================================
# SEÇÃO 1 : DICIONÁRIOS - FUNDAMENTOS
#===========================================

def demonstrar_dicionarios():
    """ Demonstra operações fundamentais com dicionários. """
    print("=== Dicionários Fundamentos ===\n")

    # Dataset de configuração de modelo
    config = {
        "modelo" : "RandomForest",
        "n_estimators": 100,
        "max_depth": 10,
        "random_state": 42,
        "features": ["idade", "renda", "score"]
    }

    print(f"Configuração inicial: {config}")
    print(f"Tipo: {type(config)}")
    print(f"Tamanho: {len(config)} pares")

    # Acesso
    print(f"\n--- Acesso ---")
    print(f"Modelo: {config['modelo']}")
    print(f"Min_samples_split: {config.get('min_samples_split', 'não definido')}")
    print(f" 'max_depth' existe? {'max_depth' in config}")

    # Modificação
    print(f"\n--- Modificação ---")
    config["n_estimators"] = 200  # altera
    config["min_samples_leaf"] = 5 # adiciona

    print(f"Apos modificações: {config}")

    # Remoção
    print(f"\n--- Remoção ---")
    removido = config.pop("random_state")
    print(f"Removido: {removido}")
    print(f"Restante: {config}")

    # Iteração
    print() # CORRIGIDO: era 'Print()'
    print(f"--- Iteração ---")
    print("Chaves:")
    for chave in config.keys():
        print(f"         - {chave}")
    
    print("\nValores:")
    for valor in config.values():
        print(f"        - {valor}")
    
    print("\nItens(chaves, valor): ")
    for chave, valor in config.items():
        print(f"{chave}: {valor}")
    print()

#===========================================
# SEÇÃO 2 : DICIONÁRIOS - AVANÇADOS
#===========================================

def dicionarios_avancados():
    """ Demonstra técnicas avançadas com dicionários. """
    print("=== Dicionários Avançados ===\n")
    # Dict Comprehension   
    print(f"\n--- Dict comprehension ---")

    # Mapeamento de IDs para códigos
    ids = range(1, 6)
    mapeamento = {f"user_{i}": f"ID-{1000+i}" for i in ids}
    print(f"Mapeamento de usuários:{mapeamento} ")
    print() 
    # Inversão de dicionário 
    original = {"a":1, "b":2, "c":3}
    invertido = {v:k for k, v in original.items()}
    print(f"Invertido: {invertido}")
    print()
    # Filtragem
    print(f"\n--- Filtragem---\n")
    metricas = {
        "acuracia": 0.92,
        "precisao": 0.89,
        "recall": 0.95,
        "f1_score": 0.92,
        "auc_roc": 0.97
    }

    # Filtra com métricas acima de 0.90
    metricas_altas = {k:v for k, v in metricas.items() if v > 0.90}
    print(f"Metricas > 0.90: {metricas_altas}")  
    print()
    # Dicionário aninhado (Nested Dict)
    print("--- Dicionário Aninhado ---\n")

    experimentos = {
        "exp_001": {
            "modelo": "SVM",
            "params": {"C":1.0, "kernel": "rbf"},
            "resultados": {"acc": 0.91, "f1":0.90}
        },
        "exp_002":{
            "modelo": "XGBoost",
            "params": {"n_estimators":100, "Ir":0.1},
            "resultados": {"acc": 0.85, "f1":0.84}  
        }
    }

    # Acesso aninhado
    print(f"Acurácia exp002: {experimentos['exp_002']['resultados']['acc']}")
    print()

    # Iteração aninhada
    print("\n Resumo de experiementos:\n")
    for exp_id, dados in experimentos.items():
        print(f" {exp_id}: {dados['modelo']} - Acc: {dados['resultados']['acc']}")
    print()
    # DefaultDict( padrão para chaves inexixtentes )
    print("\n Valores Padrão")
    from collections import defaultdict

    # Contagem de Categorias
    categorias =  ["A", 'B', "A", "C", "B", "A", "A"]
    contagem = defaultdict(int) # valor padrão: 0

    for cat in categorias: contagem[cat] += 1
    print(f" Contagem: {dict(contagem)}")
    print()























# Chamadas das funções
if __name__ == "__main__":
    demonstrar_dicionarios()
    dicionarios_avancados()