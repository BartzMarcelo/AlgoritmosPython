class Carro:

    '''Classe Carro'''

    #Atributos Globais
    qtd_rodas: int = 4
    total_carros: int =0

    def __init__(self, modelo: str, cor : str, ano: int)-> None:
        self.modelo: str = modelo
        self.cor: str = cor
        self.ano: int = ano
        self.pisca: bool = False
        Carro.total_carros +=1 

     # Métodos
    def buzina(self):
        """ Buzina e Verifica o estado do pisca do carro."""
        print(f'O carro {self.modelo} está buzinando.')
        print(f'E esta com o pisca {"ligado" if self.pisca else "desligado"}.')

    def toggle_pisca(self)->None:
        """ Liga ou desliga o pisca do carro."""
        self.pisca = not self.pisca
    
    


    

