from classeContaBancaria import ContaBancaria


if __name__ == '__main__':

    # Criando o objeto e instanciando a classe.
    cb1 = ContaBancaria(' João', 1200.00)
    cb2 = ContaBancaria(' Maria', 300.00)
    
    cb1.aplicar_juros()
    cb2.aplicar_juros()

    print(cb1)
    print(cb2)