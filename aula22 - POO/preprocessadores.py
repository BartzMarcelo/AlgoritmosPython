""" Este Arquivo será uma biblioteca de ferramentas de dados"""

import statistics

class  PreprocessadorDados:
    """
    Classe para pipeline de preprocessamento.
    Demonstra como PP organiza código de ML.
    """

    def __init__(self, nome, tecnica = "padronizacao"):
        self.nome = nome
        self.tecnica = tecnica
        self.esta_ajustado = False
        self.estatisticas = {}

    def ajustar(self, dados):
        # import statistics
        self.estatisticas = {
            "media": statistics.mean(dados),
            "desvio": statistics.stdev(dados) if len(dados)> 1 else 1 
        }
        self.esta_ajustado = True
        print(f"[{self.nome}] Ajustado com {len(dados)} amostras: ")
        return self