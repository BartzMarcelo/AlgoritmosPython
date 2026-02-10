from pessoa import Pessoa

if __name__ == '__main__':

    # Criando o objeto e instanciando a classe.
    p1: Pessoa = Pessoa('José')
    p2 = Pessoa ('Bruno')
    p3 : Pessoa = Pessoa('Carla')

    # Exibindo os dados:
    
    print(p1)
    print(p2)
    print(p3)
    print(f'Total de pessoas é {Pessoa.total_pessoas}.')