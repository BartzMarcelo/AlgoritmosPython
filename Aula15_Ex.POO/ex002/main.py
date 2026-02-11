from classCirculo import Circulo

if __name__ == '__main__':

    # Criando o objeto e instanciando a classe.
    c1 = Circulo(5.0)
    c2 = Circulo(10.0)
    
    print(c1)
    print(c2)

    #Acessando o atributo da classe.
    print(f'\nO valor de pi utilizando é : {Circulo.PI}')