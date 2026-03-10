from interfaces import Exportavel
from protocolos import Serializavel, LoggerSimples
from modelos import RedeNeuralProfunda, RegressaoLinear
from fabricas import FabricaTensorFlow

def processar_serializavel(obj: Serializavel):
    """ Aceita QUALQUER objeto que satisfaça o protocolo serializavel """
    obj.salvar("temp.txt")
    print(f"Dicionário: {obj.to_dict()}")

def main():
    print("="*40)
    print("Demontração de Padrões de Interfaces")
    print("="*40)
    # 1. Uso Polimórfico - Demonstração do poliformismo.

    modelos = [
        RegressaoLinear("Linear-v1"),
        RedeNeuralProfunda("Neural-v1")
    ] 
    for m in modelos:
        m.treinar([1,2], [1])
        if isinstance(m, Exportavel):
            print(f"{m.nome} pode ser exportado para JSON: {m.exportar_json()}")

    # 2. Protocolo 
    print("\n--- Testando Protocolo ---")
    logger = LoggerSimples()
    processar_serializavel(logger)

    # 3. Abstract Fatory
    print("\n--- Testando Fábricas ---")
    minha_fabrica = FabricaTensorFlow
    novo_modelo = minha_fabrica.criar_classificador()
    print(f"Modelo criado pela fábrica: {novo_modelo.nome}.")

if __name__ == "__main__":
    main()