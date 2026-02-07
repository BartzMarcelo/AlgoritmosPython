"""Fazer os imports, se necessário."""
import veiculo

if __name__ == '__main__':
    volvo = veiculo.Carro('Volvo', 'Verde', 2000)
    # volvo.buzina()
    # volvo.toggle_pisca()
    # volvo.buzina()
    fusca = veiculo.Carro('Fusca', 'Azul','1987')
    # print(f'Quantidade de rodas do {volvo.modelo} é {volvo.qtd_rodas}')
    # print(f'Quantidade de rodas do {fusca.modelo} é {fusca.qtd_rodas}')
    print(f'Total de carros criados {veiculo.Carro.total_carros}.')
    bmw = veiculo.Carro('Brasília muito velha', 'Prata',1950)
    print(f'Total de carros criados {veiculo.Carro.total_carros}.')