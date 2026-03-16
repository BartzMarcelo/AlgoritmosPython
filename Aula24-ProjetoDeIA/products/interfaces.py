# products/interfaces.py
from abc import ABC, abstractmethod
import pandas as pd

class DataReader(ABC):
    @abstractmethod
    def read(self, path: str, **kwargs) -> pd.DataFrame: pass
    
class DataCleaner(ABC): 
    @abstractmethod
    def clean(self, df: pd.DataFrame, num_cols: list, cat_cols: list) -> pd.DataFrame: pass

class DataPreprocessor(ABC):
     @abstractmethod
     def process(self, df: pd.DataFrame, target: str, num_cols: list, cat_cols: list): pass