"""Fazer os imports, se necessário."""
from Aula14_POO.String_Carro.carro import Carro


if __name__ == '__main__':
    volvo: Carro = Carro('Volvo', 'Verde', 2000)
    # volvo.buzina()
    # volvo.toggle_pisca()
    # volvo.buzina()
    fusca = Carro('Fusca', 'Azul','1987')
    # print(f'Quantidade de rodas do {volvo.modelo} é {volvo.qtd_rodas}')
    # print(f'Quantidade de rodas do {fusca.modelo} é {fusca.qtd_rodas}')
    # print(f'Total de carros criados {Carro.total_carros}.')     
    bmw = Carro('Brasília muito velha', 'Prata',1950)
    print(f'Total de carros criados {Carro.total_carros}.')


      
  
    
    