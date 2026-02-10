class Carro:
    """Classe Carro"""

    def __init__(self,modelo: str = '')-> None:
        self.modelo: str = modelo
    
    def __str__(self)-> str:
        return  f'O meu modelo é {self.modelo}.'
