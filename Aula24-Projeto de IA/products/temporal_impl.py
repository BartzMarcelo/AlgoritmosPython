# Nesta implementação, a lógica de limpeza e divisão de dados respeita a natureza temporal.

import pandas as pd
import numpy as np
from .interfaces import DataReader, DataCleaner, DataPreprocessor

class TemporalReader(DataReader):
    def read(self, path: str, **kwargs):
        df = pd.read_csv(path, **kwargs)
        date_cols = df.select_dtypes(include=["object"]).columns
        if len(date_cols) > 0:
            df [date_cols[0]]= pd.to_datetime(df[date_cols[0]])
            df = df.sort_values(date_cols[0])
        return df

class TemporalCleaner(DataCleaner):
    def clean(self, df: pd.DataFrame, num_cols: list, cat_cols, list):
        df_clean = df.copy()
        df_clean[num_cols]= df_clean[num_cols].fillna(method = 'ffill').fillna(method = 'bfill')
        df_clean[cat_cols]= df_clean[cat_cols].fillna(method = 'ffill')
        return df_clean
    
class TemporalPreprocessor(DataPreprocessor):
    def process(self, df: pd.DataFrame, target: str, num_cols:list,cat_cols:list):
        X = df.drop(columns =[target])
        y = df[target]

        split_idx = int(len(df)*0.8)

        X_train, X_test =X.iloc[:split_idx],X.iloc[split_idx:]
        y_train, y_test =y.iloc[:split_idx],y.iloc[split_idx:]

        print("Aviso: Divisão temporal aplicada(sem embaralhamento).")
        return X_train, X_test, y_train, y_test



