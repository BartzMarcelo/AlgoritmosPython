"""imports"""

from veiculo import Carro

if __name__ == '__main__':
    audi : Carro = Carro('a6', 'prata', 2012)
    print(f'Total de carros criados {Carro.total_carros}.')