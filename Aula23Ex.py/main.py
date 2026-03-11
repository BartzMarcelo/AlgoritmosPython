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

    # 1. Uso Polimórfico
    modelos = [ 
        RegressaoLinear("Linear-v1"),
        RedeNeuralProfunda("Neural-v1"),
        ModeloMedia("Media-v1") 
    ]

    print("\n--- Processando Modelos ---")
    for m in modelos:
        # Treinamento
        m.treinar([1, 2], [1])
        
        # Previsão (Captura o retorno da lista [42.0, 42.0])
        previsoes = m.prever([10, 20])
        
        # Exibição Única de Resultados
        print(f"Modelo: {m.nome}")
        print(f"Previsão Fixa: {previsoes}")
        print(f"Status Treinado: {m.esta_treinado}") # <-- Aparece apenas 1x aqui
        
        # Verificação de Interface
        if isinstance(m, Exportavel):
            print(f"Exportação JSON: {m.exportar_json()}")
            
        print("-" * 35)

    # 2. Protocolo
    print("\n--- Testando Protocolo ---")
    logger = LoggerSimples()
    processar_serializavel(logger)

    # 3. Fábricas (Abstract Factory)
    print("\n--- Testando Fábricas ---")
    fabrica = FabricaSklearn() 
    novo_modelo = fabrica.criar_classificador()
    print(f"Modelo criado via Fábrica: {novo_modelo.nome}")

if __name__ == "__main__":
    main()