"""
Arquivo que define as "regras" que os outros devem seguir.
(Contratos e Protocolos)

"""
# Importa ferramentas para criar Classes Abstratas
from abc import ABC, abstractmethod, abstractproperty

# Tipagem estática para aumentar a segurança do código.
from typing import List, Dict, Any, Optional, Protocol

import json
import pickle

# Definindo a base para classes abastratas (ABC).

from abc import ABC, abstractmethod
from typing import List, Any

class ModeloTreinavel(ABC): 
    @abstractmethod # Obriga as subclasses a implementarem este método.
    def treinar(self, X: List[Any], y: List[Any], **kwargs) -> "ModeloTreinavel":
        """
        Método para treinar o modelo. Retorna o próprio objeto(self).
        """
        pass

    @abstractmethod
    def prever(self, X: List[Any]) -> List[Any]:
        """ Gera predições através de dados de entrada."""
        pass

    
    @abstractmethod
    def avaliar(self, X_test: List[Any], y_test: List[Any]) -> Dict[str, float]:
        """ Calcula métricas (ex: acurácia, erro)."""
        pass

    @abstractmethod
    def esta_treinando(self)-> bool:
        """Propriedade oara verificar o status do Modelo."""
        pass

    # Método Concreto: Já tem funcionalidade pronta, mas pode ser mudado.
    def salvar(self, caminho: str)-> bool:
        """ Usa a biblioteca pikle para salvar o objeto em disco."""
        try:
            with open(caminho, 'wb') as f:
                pickle.dump(self, f)
                return True               
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False
        
    @classmethod
    def carregar(cls, caminho: str) -> Optional["ModeloTreinavel"]:
        """ Método de classe para ler um modelo salvo em disco."""
        try:
            with open(caminho, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
        

class Exportavel(ABC):
    """ Contrato adicional para modelos que precisam exportar dados."""
    @abstractmethod
    def exportar_onnx(self, caminho: str)-> bool:
        """ Exporta para formato ONNX(Open Neural Networking Exchange)"""
        pass

    def exporta_json(self )-> Dict[str, Any]:
        """ Exporta representação JSON (JavaScript Object Notetion)do modelo"""
        pass

    
