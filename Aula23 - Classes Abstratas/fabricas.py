from abc import ABC,abstractmethod
from typing import List, Optional

# Importando os contratos / interfaces que definimos no outro arquivo
from interfaces import ModeloTreinavel

# Importando as classes concretas para que as fábrica possa instancia-las.

from modelos import RegressãoLinear

class FabricaModelos(ABC):
    """ padrão Abstract Factory cria objetos relacionados"""
