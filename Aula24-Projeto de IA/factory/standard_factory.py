# A implementação da fábrica "amarra"os produtos tabulares.

from.base_factory import AnalysisFactory
from products.tabular_impl import TabularReader, TabularCleaner, TabularPreprocessor

class StandardMLFactory(AnalysisFactory):
    def create_reader(self): return TabularReader()
    def create_cleaner(self): return TabularCleaner()
    def create_preprocessor(self): return TabularPreprocessor()
    