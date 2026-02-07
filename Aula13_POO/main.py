"""Fazer os imports, se necessário."""
import veiculo

if __name__ == '__main__':
    volvo = veiculo.Carro('Volvo', 'Verde', 2000)
    volvo.buzina()
    volvo.toggle_pisca()
    volvo.buzina()