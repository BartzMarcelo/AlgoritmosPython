# A interface da fábrica que define quais produtos devem ser entregues.
from abc import ABC, abstractmethod
from products.interfaces import DataReader, DataCleaner, DataPreprocessor

class AnalysisFactory(ABC):
    
    @abstractmethod
    def create_reader(self) -> DataReader:
        pass
    
    @abstractmethod
    def create_cleaner(self) -> DataCleaner:
        pass

    @abstractmethod
    def create_preprocessor(self) -> DataPreprocessor:
        pass