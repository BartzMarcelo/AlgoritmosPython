from classFuncionario import Funcionario

if __name__ == '__main__':

    # Criando o objeto e instanciando a classe.
    f1 = Funcionario('João', 2500.00)
    f2 = Funcionario('José', 1300.00)
    
    print(f1)
    print(f"Ganha o minimo ou mais: { 'Sim' if  f1.comparar_salario() else 'Não'}")

    print("-" * 30)

    print(f2)
    print(f"Ganha o minimo ou mais: { 'Sim' if  f2.comparar_salario() else 'Não'}")


    print(f"\nValor do salário minímo ataul: R$ { Funcionario.salario_minimo:.2f}.")



    