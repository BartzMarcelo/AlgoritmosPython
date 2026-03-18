# core/orchestrator.py

class AnaliseDadosIA:
    """
    O Orquestrador (Contexto) do padrão Abstract Factory.
    Ele gerencia o fluxo de trabalho sem conhecer as implementações 
    específicas de como os dados são lidos, limpos ou processados.
    """
    
    def __init__(self, factory):
        """
        Injeção de Dependência: O orquestrador recebe uma fábrica
        e extrai dela os produtos necessários.
        """
        self.reader = factory.create_reader()
        self.cleaner = factory.create_cleaner()
        self.preprocessor = factory.create_preprocessor()

    def executar_pipeline(self, path: str, target: str, num_cols: list, cat_cols: list):
        """
        Executa o fluxo completo de processamento de dados.
        Recebe as listas de colunas para garantir que o Cleaner e o 
        Preprocessor saibam exatamente quais campos tratar.
        """
        
        # 1. Leitura dos dados (O orquestrador não sabe se é CSV, Parquet ou SQL)
        df = self.reader.read(path)
        
        # 2. Limpeza (O orquestrador não sabe se usa Mediana ou FFill)
        df_clean = self.cleaner.clean(df, num_cols, cat_cols)
        
        # 3. Pré-processamento (O orquestrador não sabe se houve shuffle ou escala)
        X_train, X_test, y_train, y_test = self.preprocessor.process(
            df_clean, target, num_cols, cat_cols
        )
        
        # Retorna os dados prontos para o treinamento do modelo
        return X_train, X_test, y_train, y_test