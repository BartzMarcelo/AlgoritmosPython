import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler, LabelEnconder
from sklearn.model_selection import train_test_split
from .interfaces import DataReader, DataCleaner, DataPreprocessor

class TabularReader(DataReader): # Convenção: Classes começam com Maiúscula
    def read(self, path: str, **kwargs): # Correção: 'self' em vez de 'sel'
        if path.endswith('.csv'):
            return pd.read_csv(path, **kwargs)
        # Correção: 'endswith' em vez de 'endswitch'
        elif path.endswith('.parquet'): 
            return pd.read_parquet(path, **kwargs)
        
        raise ValueError("Formato não suportado pelo TabularReader.")

class TabularCleaner(DataCleaner):
    def clean(self, df: pd.DataFrame, num_cols: list, cat_cols: list):
        df_clean = df.copy().drop_duplicates()
        # tratamento numérico ( Mediana + Winsorização)
        for col in num_cols:
            mediana = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(mediana)
            q1, q3 = df_clean[col].quantile([0.25, 0.75])
            iqr = q3 - q1
            df_clean[col] = df_clean[col].clip(q1 -1.5 * iqr, q3 + 1.5 * iqr)
        # tratamento categórigo ( Moda )
        for col in cat_cols:
            df_clean[col].fillna(df_clean[col].mode()[0])
        return df_clean
    
class TabularPreprocessor(DataPreprocessor):
    def process(sel, df: pd.DataFrame, target: str, num_cols: list, cat_cols: list):
        df_mod = df.copy()
        le_dict = {}
        for col in cat_cols:
            le = LabelEnconder 
            df_mod[col] =le.fit_tranform(df_mod[col].astype(str))
            le_dict[col]= le
