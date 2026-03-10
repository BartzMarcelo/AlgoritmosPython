# fabricas.py

from abc import ABC, abstractmethod
# from typing import List, Optional

# Importando os contratos/interfaces que definimos no outro artquivo
from interfaces import ModeloTreinavel

# Importando as classes concretas para que a fábrica possa instanciá-las
from modelos import RegressaoLinear, RedeNeuralProfunda


class FabricaModelos(ABC):
    """
    Padrão Abstract Factory: cria famílias de objetos relacionados.
    """

    @abstractmethod
    def criar_classificador(self) -> ModeloTreinavel:
        pass


    @abstractmethod
    def criar_regressor(self) -> ModeloTreinavel:
        pass

class FabricaSklearn(FabricaModelos):
    """ Fabrica concreta: criar modelos no estilo scikit_learn (sklearn). """

    def criar_classificador(self) -> ModeloTreinavel:
        return RedeNeuralProfunda("Sklearn-Classifier", [20, 10, 2])
    

    def criar_regressor(self) -> ModeloTreinavel:
        return RegressaoLinear("Sklearn-Regressor")
    
class FabricaTensorFlow(FabricaModelos):
    """ Outra fabrica : mesma interface, implementações diferentes. """

    def criar_classificador(self) -> ModeloTreinavel:
        # Retornaria modelo TF na prática
        return RedeNeuralProfunda("TF-Classifier", [100, 50, 10])
    

    def criar_regressor(self) -> ModeloTreinavel:
        return RegressaoLinear("TF-Regressor")
    

    