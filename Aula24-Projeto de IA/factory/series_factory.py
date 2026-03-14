# Esta fábrica garante que, ao ser chamada, todos os componentes entregues sejam da familia "Temporal".

from .base_factory import AnalysisFactory
from products.temporal_impl import TemporalReader, TemporalCleaner,TemporalPreprocessor

class SeriesFactory(AnalysisFactory):
    """Fábrica especializada em dados de Séries Temporais"""

    def create_reader(self):
        return TemporalReader
    
    def create_cleaner(self):
        return TemporalCleaner
    
    def create_preprocessor(self):
        return TemporalPreprocessor

