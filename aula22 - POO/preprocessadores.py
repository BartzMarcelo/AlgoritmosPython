""" Este Arquivo será uma biblioteca de ferramentas de dados"""

import statistics

class PreprocessadorDados:
    """
    Classe para pipeline de preprocessamento.
    Demonstra como PP organiza código de ML.
    """

    def __init__(self, nome, tecnica="padronizacao"):
        self.nome = nome
        self.tecnica = tecnica
        self.esta_ajustado = False
        self.estatisticas = {}

    def ajustar(self, dados):
        # O dicionário foi fechado corretamente
        self.estatisticas = {
            "media": statistics.mean(dados),
            "desvio": statistics.stdev(dados) if len(dados) > 1 else 1 
        }
        self.esta_ajustado = True
        print(f"[{self.nome}] Ajustado com {len(dados)} amostras: ")
        return self
    
    def transformar(self, dados):
        """ Aplica transformação usando estatísticas aprendidas."""
        if not self.esta_ajustado:
            raise RuntimeError(f"[{self.nome}] Erro: preprocessador não ajustado!")
        
        if self.tecnica == "padronizacao":
            # Correção na ordem dos colchetes e nomes das chaves
            return [(x - self.estatisticas["media"]) / self.estatisticas["desvio"] for x in dados]
        
        return dados
    # Fim do método transformar

    # fecha a classe PreProcessadorDados:

    # Demonstração
    print(f"\n{"=" * 60}")
    print("PIPELINE DE ML COM POO")
    print(f"\n{"=" * 60}")

# Correção: Adicionado o 's' em scaler e removido o acento para bater com a lógica da classe

scaler = PreprocessadorDados("Scaler-x", tecnica="padronizacao")

# Lista de dados para o pipeline
dados_treino = [10, 20, 30, 40, 50]

# Método encadeado: ajustar e transformar
dados_transformados = scaler.ajustar(dados_treino).transformar(dados_treino)

print(f"dados originais: {dados_treino}")
print("")

# CORREÇÃO: Itera diretamente sobre a lista de resultados e formata cada número
print(f"Dados normalizados: {[round(x, 2) for x in dados_transformados]}")