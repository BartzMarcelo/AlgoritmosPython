from interfaces import Exportavel
from protocolos import Serializavel, LoggerSimples
from modelos import RegressaoLinear, RedeNeuralProfunda, ModeloMedia 
from fabricas import FabricaTensorFlow, FabricaSklearn

def processar_serializavel(obj: Serializavel):
    """ Aceita QUALQUER objeto que satisfaça o protocolo Serializavel. """
    obj.salvar("temp.txt")
    print(f"Dicionário: {obj.to_dict()}")

def main():
    print("="*40)
    print("DEMONSTRAÇÃO DE PADRÕES E INTERFACES")
    print("="*40)

    # 1. Uso Polimórfico - Demonstração do polimorfismo
    modelos = [ 
        RegressaoLinear("Linear-v1"),
        RedeNeuralProfunda("Neural-v1"),
        ModeloMedia("Media-v1") 
    ]

    for m in modelos:
        # Executa o treino (mostrará a mensagem no terminal)
        m.treinar([1, 2], [1])
        
        # --- AJUSTE AQUI: Para mostrar o retorno do prever e a propriedade ---
        previsao = m.prever([10, 20]) # Simula uma entrada para receber o retorno
        print(f"Modelo: {m.nome}")
        print(f"Previsão Fixa: {previsao}")     # Mostrará a lista de 42.0
        print(f"Está Treinado: {m.esta_treinado}") # Mostrará True
        # ---------------------------------------------------------------------

        if isinstance(m, Exportavel):
            print(f"{m.nome} pode ser exportado para JSON: {m.exportar_json()}")
        print("-" * 30)

    # 2. Protocolo
    print("\n--- Testando Protocolo ---")
    logger = LoggerSimples()
    processar_serializavel(logger)

    # 3. Abstract Factory
    print("\n--- Testando Fábricas ---")
    minha_fabrica = FabricaSklearn() 
    novo_modelo = minha_fabrica.criar_classificador()
    print(f"Modelo criado pela fábrica: {novo_modelo.nome}")

if __name__ == "__main__":
    main()