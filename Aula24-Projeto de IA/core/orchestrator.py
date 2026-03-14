# O cliente (Orquestrador) que utiliza a fabrica .  
# Ele não sabe como as coisa são feitas, apenas que a fabrica as entregas.

import numpy as np

class AnaliseDadosIA:
    def __init__(self, factory):
        self.reader = factory.create_reader()
        self.cleaner = factory.create_cleaner()
        self.preprocessor = factory.create_preprocessor()

    def executar_pipeline(self, caminho, target):
        # 1. Leitura
        df = self.reader.read(caminho)

        # 2. Seleção de colunas (Correção dos erros de digitação)
        # Erros originais: inclue -> include | colums -> columns | tolidt -> tolist
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

        # Se o alvo (target) estiver na lista de colunas, removemos para não processá-lo como feature
        if target in num_cols: num_cols.remove(target)
        if target in cat_cols: cat_cols.remove(target)

        # 3. Limpeza
        df_clean = self.cleaner.clean(df, num_cols, cat_cols)

        # 4. Processamento
        return self.preprocessor.process(df_clean, target, num_cols, cat_cols)
