from interfaces import  Exportavel
from protocolos import Serializavel, LoggerSimples
from modelos import RegressaoLinear, RedeNeuralProfunda
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
        RedeNeuralProfunda("Neural-v1")
    ]

    for m in modelos:
        m.treinar([1, 2], [1])
        if isinstance(m, Exportavel):
            print(f"{m.nome} pode ser exportado para JSON: {m.exportar_json()}")

    # 2. Protocolo
    print("\n--- Testando Protocolo ---")
    logger = LoggerSimples()
    processar_serializavel(logger)

    #3. Abstract Factory
    print("\n--- Testando Fábricas ---")
    minha_fabrica = FabricaSklearn() # FabricaTensorFlow()
    novo_modelo = minha_fabrica.criar_classificador()
    print(f"Modelo criado pela fábrica: {novo_modelo.nome}")

if __name__ == "__main__":
    main()

# processar_serializavel()

