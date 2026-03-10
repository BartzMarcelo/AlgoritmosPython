from abc import ABC, abstractmethod
from typing import List, Optional

# Importando os contratos / interfaces
from interfaces import ModeloTreinavel

# Importando as classes concretas
# Dica: Certifique-se que o arquivo modelos.py não tenha acentos nos nomes das classes
from modelos import RegressaoLinear, RedeNeuralProfunda

class FabricaModelos(ABC):
    """ Padrão Abstract Factory: cria objetos relacionados """

    @abstractmethod
    def criar_classificador(self) -> ModeloTreinavel:
        pass

    @abstractmethod
    def criar_regressor(self) -> ModeloTreinavel:
        pass


class FabricaSklearn(FabricaModelos):
    """ Fábrica concreta: Criar modelos no estilo scikit-learn (sklearn). """

    def criar_classificador(self) -> ModeloTreinavel:
        return RedeNeuralProfunda("Sklearn-Classifier", [20, 10, 2])

    def criar_regressor(self) -> ModeloTreinavel:
        return RegressaoLinear("Sklearn-Regressor")


class FabricaTensorFlow(FabricaModelos):
    """ Outra fábrica: mesma interface, implementações são diferentes. """

    def criar_classificador(self) -> ModeloTreinavel:
        # Retornaria modelo TF na prática
        return RedeNeuralProfunda("TF-Classifier", [100, 50, 10])

    def criar_regressor(self) -> ModeloTreinavel:
        return RegressaoLinear("TF-Regressor")