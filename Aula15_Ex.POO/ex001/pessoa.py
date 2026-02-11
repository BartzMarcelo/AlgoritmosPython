class Pessoa:

    qtd_pernas = int (2)
    qtd_bracos = int (2)
    total_pessoas : int = 0
    
    def __init__(self, nome: str)-> None:
        self.nome: str = nome        
        Pessoa.total_pessoas +=1

    def __str__(self)-> str :
        return f'Nome:{self.nome}'
     
    

