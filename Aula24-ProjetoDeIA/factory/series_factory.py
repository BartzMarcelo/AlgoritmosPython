# factory/series_factory.py

from .base_factory import AnalysisFactory
# Ajustado para buscar na pasta products onde as interfaces e implementações residem
from products.interfaces import DataReader, DataCleaner, DataPreprocessor
from products.temporal_impl import TemporalReader, TemporalCleaner, TemporalPreprocessor

class SeriesFactory(AnalysisFactory):
    """Fábrica especializada em dados de Séries Temporais"""

    def create_reader(self) -> DataReader:
        return TemporalReader()
    
    def create_cleaner(self) -> DataCleaner:
        return TemporalCleaner()
    
    def create_preprocessor(self) -> DataPreprocessor:
        return TemporalPreprocessor()