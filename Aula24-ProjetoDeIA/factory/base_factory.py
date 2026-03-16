# factory/base_factory.py
from abc import ABC, abstractmethod
# Importamos as interfaces da pasta products conforme sua estrutura
from products.interfaces import DataReader, DataCleaner, DataPreprocessor

class AnalysisFactory(ABC):
    """
    Interface da fábrica que define quais produtos devem ser entregues.
    Não deve importar a si mesma.
    """
    
    @abstractmethod
    def create_reader(self) -> DataReader:
        pass
    
    @abstractmethod
    def create_cleaner(self) -> DataCleaner:
        pass

    @abstractmethod
    def create_preprocessor(self) -> DataPreprocessor:
        pass