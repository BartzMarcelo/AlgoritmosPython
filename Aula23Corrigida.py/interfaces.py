# interfaces.py
"""
Arquivo que define as "regras" que os outros devem seguir.
 ( Contratos e Protocolos )
"""
# Importa ferramentas para criar Classes Abstratas
from abc import ABC, abstractmethod

# Tipagem estática para aumentar a segurança do código
from typing import List, Dict, Any, Optional

import pickle

# Definindo a base para classes abstratas (ABC)
class ModeloTreinavel(ABC):
    @abstractmethod # Obriga as subclasses a implementarem este método.
    def treinar(self, X: List[Any], y: List[Any], **kwargs) -> "ModeloTreinavel":
        """ Método para treinar o modelo. Retorna o próprio objeto (self)."""
        pass

    @abstractmethod
    def prever(self, X: List[Any]) -> List[Any]:
        """ Gera predições a partir de dados de entrada. """
        pass

    @abstractmethod
    def avaliar(self, X_test: List[Any], y_test: List[Any]) -> Dict[str, float]:
        """ Calcula métricas ( ex: acurácia, erro)."""
        pass


    @property
    @abstractmethod
    def esta_treinado(self) -> bool:
        """ Propriedade para verificar o status do modelo. """
        pass

    # Método Concreto: Já tem funcionalidade pronta, mas pode ser mudado.
    def salvar(self, caminho: str) -> bool:
        """ Usa a biblioteca pickle para salvar o objeto em disco. """
        try:
            with open(caminho, 'wb') as f:
                pickle.dump(self, f)
                return True            
        except Exception: # as e:
            # print(f"Erro ao salvar: {e}")
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
    """ Contrato adicional para modelos que precisam exportar dados. """
    @abstractmethod
    def exportar_onnx(self, caminho:str) -> bool:
        """ Exporta para formato ONNX (Open Neural Network Exchange)."""
        pass

    def exportar_json(self) -> Dict[str, Any]:
        """ Exporta representação JSON (JavaScript Object Notation )do modelo. """
        pass

   
    