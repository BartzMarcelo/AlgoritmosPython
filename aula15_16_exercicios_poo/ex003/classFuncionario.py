class Funcionario:

    salario_minimo = float(1621.00)
    
    
    def __init__(self, nome: str, salario: float)-> None:
        self.nome = nome
        self.salario = salario

    def comparar_salario(self) -> bool:
        
        return self.salario >= Funcionario.salario_minimo
    
    def __str__(self)-> str:
        return f'O funcionario: {self.nome} | Salário: {self.salario:.2f}'
        


        # if self.comparar_salario() == True:
        # #     print(f'O salário de {self.nome} é maior ou igual ao salário minímo ')
        # # else:
        # #     print(f'O salário de {self.nome} é menor que o salário minímo ')
        
        #     return f"O salário de {self.nome} (R$ {self.salario:.2f}) é maior ou igual ao salário mínimo."
        # else:
        #     return f"O salário de {self.nome} (R$ {self.salario:.2f}) é menor que o salário mínimo."
      
    



    