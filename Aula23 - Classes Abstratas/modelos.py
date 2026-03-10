""" Implementações Concretas """

from interfaces import ModeloTreinavel, Exportavel
from typing import List, Dict, Any, Optional
import random

import random
from typing import List, Any, Dict

class RegressaoLinear(ModeloTreinavel):
    def __init__(self, nome: str = "LinearReg"):
        self.nome = nome
        self._treinado = False  # Mantendo o padrão com underline

    def treinar(self, X: List[Any], y: List[Any], **kwargs) -> "RegressaoLinear":
        print(f"[{self.nome}] Treinando regressão...")
        self._treinado = True  # Corrigido para bater com o __init__
        return self

    def prever(self, X: List[Any]) -> List[Any]:
        # Corrigido o espaço e o loop 'for _ in X'
        return [random.uniform(0, 1) for _ in X]

    def avaliar(self, X_test: List[Any], y_test: List[Any]) -> Dict[str, float]:
        return {"mse": 0.01}
    
    @property
    def esta_treinado(self) -> bool:
        return self._treinado
    

class RedeNeuralProfunda(ModeloTreinavel):
    """
    Implementação Multipla: cumpre dois contratos.
    Herda de ModeloTreinavel e Exportavel.
    """
    def __init__(self, nome: str = "DeepNN", camadas : Optional [List[int]] = None):
        self.nome = nome
        self.arquetetura = camadas or [ 10, 5 ,1]
        self._pesos = []
        self._treinado = False
    
    # Modelo treinavel implementations
    from typing import List, Any

    # ... dentro da sua classe ...

    def treinar(self, X: List[Any], y: List[Any], epocas: int = 10, **kwargs) -> "RedeNeuralProfunda":
    # Sua lógica de treino aqui
        print(F"[{self.nome}] treinando rede neural por {epocas} épocas...")
        import random
        self._pesos = [random.random()for _ in range (sum(self.arquetetura))]
        self._treinado = True
        return self

    def prever(self, X:List[Any]) -> List[Any]:
        if not self._treinado: 
            raise RuntimeError(" Modelo não treinado. ")
        import random
        return[random.random( ) for _ in X]
    
    def avaliar( self, X_test: List[Any], y_test: List[Any])-> Dict[str, float]:
        return{"acurácia": 0.95, "fi": 0.94}
        
    # Exportavel implementations
    def exportar_onnx(self, caminho: str) -> bool:
        print(f"[{self.nome}]Exportando para ONNX: {caminho}")
        return True
    
    def exportar_json(self) -> Dict[str, Any]:
        return{
            "tipo": "RedeNeuralProfunda",
            "arquetetura":self.arquetetura,
            "pesos": len(self._pesos)
        }
    @property
    def esta_treinado(self) -> bool:
        return self._treinado


    