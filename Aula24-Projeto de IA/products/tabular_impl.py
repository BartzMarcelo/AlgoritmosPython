import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from .interfaces import DataReader, DataCleaner, DataPreprocessor

class TabularReader(DataReader): 
    def read(self, path: str, **kwargs): 
        if path.endswith('.csv'):
            return pd.read_csv(path, **kwargs)
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
            df_clean[col] = df_clean[col].clip(q1 - 1.5 * iqr, q3 + 1.5 * iqr)
            
        # tratamento categórico ( Moda )
        for col in cat_cols:
            # Adicionada a atribuição df_clean[col] = ... para salvar a alteração
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
            
        return df_clean
    
class TabularPreprocessor(DataPreprocessor):
    def process(self, df: pd.DataFrame, target: str, num_cols: list, cat_cols: list):
        # 1 - transformando texto em número(Encoding)
        df_mod = df.copy()
        le_dict = {}
        
        for col in cat_cols:
            # Corrigido: LabelEncoder() com parênteses e sem o 'n' extra
            le = LabelEncoder() 
            # Corrigido: fit_transform (com 's')
            df_mod[col] = le.fit_transform(df_mod[col].astype(str))
            le_dict[col] = le
        # 2 =nSeparando Pergunta e Resposta    
        X = df_mod.drop(colums=[target])
        y = df_mod[target]
        # 3 - Normalização (Escalonamento)
        scaler = StandardScaler()
        X[num_cols]= scaler.fit_transform(X[num_cols]) 
        # 4 - Divisão treino e Teste
        stratify = y if y.munique()< else None
        return train_test_split(X, y, test_size = 0.2, random_state= 42, stratify=stratify)
    

