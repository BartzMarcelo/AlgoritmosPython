# modelos.py

""" Implementações Concretas """

from interfaces import ModeloTreinavel, Exportavel
from typing import List, Dict, Any, Optional
import random


class RegressaoLinear(ModeloTreinavel):
    def __init__(self, nome: str = "LinearReg"):
        self.nome = nome
        self._treinado = False

    def treinar(self, X: List[Any], y: List[Any], **kwargs) -> "RegressaoLinear":
        print(f"[{self.nome}] Treinando Regressão...")
        self._treinado = True
        return self
    
    def prever(self, X: List[Any]) -> List[Any]:
        return [random.uniform(0, 1) for _ in X]
    
    def avaliar(self, X_test: List[Any], y_test: List[Any]) -> Dict[str, float]:
        return {"mse": 0.01}
    
    @property
    def esta_treinado(self) -> bool:
        return self._treinado


class RedeNeuralProfunda(ModeloTreinavel, Exportavel):
    """
        Implementação múltipla: cumpre dois contratos.
        Herda de ModeloTreinavel e Exportavel.
    """
    def __init__(self, nome: str = "DeepNN", camadas: Optional[List[int]] = None):
        self.nome = nome
        self.arquitetura = camadas or [10, 5, 1]
        self._pesos = []
        self._treinado = False

    # Modelo treinavel implementations
    def treinar(self, X:List[Any], y:List[Any], epocas: int = 10, **kwargs) -> "RedeNeuralProfunda":
        print(f"[{self.nome}] Treinando rede neural por {epocas} épocas...")
        import random
        self._pesos = [random.random() for _ in range(sum(self.arquitetura))]
        self._treinado = True
        return self
    
    def prever(self, X:List[Any]) -> List[Any]:
        if not self._treinado:
            raise RuntimeError(" Modelo não treinado ")
        import random
        return [random.random() for _ in X]
    
    def avaliar(self, X_test: List[Any], y_test:List[Any]) -> Dict[str, float]:
        return {"acurácia": 0.95, "fi": 0.94}
    

    # Exportavel implementations 
    def exportar_onnx(self, caminho: str) -> bool:
        print(f"[{self.nome}] Exportando para ONNX: {caminho}")
        return True
    

    def exportar_json(self) -> Dict[str, Any]:
        return {
            "tipo": "RedeNeuralProfunda",
            "arquitetura": self.arquitetura,
            "pesos": len(self._pesos)
        }

    @property
    def esta_treinado(self) -> bool:
        return self._treinado
