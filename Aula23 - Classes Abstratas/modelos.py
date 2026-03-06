""" Implementações Concretas """

from interfaces import ModeloTreinavel, Exportavel
from typing import List, Dict, Any, Optional
import random

class RegressaoLinear(ModeloTreinavel):
    def __init__(self, nome: str = "LinearReg"):
        self.nome = nome
        self._coeficientes = None
        self.intercepto = 0.0
        self._treinado = False