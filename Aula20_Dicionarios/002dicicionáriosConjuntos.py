#===========================================
#SEÇÃO 1 : DICIONÁRIOS - FUNDAMENTOS
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

    # Modificação (AGORA DENTRO DA FUNÇÃO)
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
    Print()
    print(f"\n--- Iteração ---")
    print("Chaves:")
    for chave in config.keys():
        print(f"         - {chave}")
    print()
    print("Valores:")
    for valor in config.values():
        print(f"        - {valor}")
    print()
    print("Itens(chaves, valor): ")
    for chave, valor in config.items():
        print(f"{chave}:{valor}")
    print()
#===========================================
#SEÇÃO 2 : DICIONÁRIOS - AVANÇADOS
#===========================================


    





# IMPORTANTE: Chame a função para que ela execute!
demonstrar_dicionarios()



























demonstrar_dicionarios()