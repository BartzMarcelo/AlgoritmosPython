class Carro:

    # Atributos
    def __init__(self, modelo: str, cor : str, ano: int)-> None:
        self.modelo: str = modelo
        self.cor: str = cor
        self.ano: int = ano
        self.pisca: bool = False

    # Métodos
    def buzina(self):
        """ Buzina e Verifica o estado do pisca do carro."""
        print(f'O carro {self.modelo} está buzinando.')
        print(f'E esta com o pisca {"ligado" if self.pisca else "desligado"}.')


    def toggle_pisca(self)->None:
        """ Liga ou desliga o pisca do carro."""
        self.pisca = not self.pisca





