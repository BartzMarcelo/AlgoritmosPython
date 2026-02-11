class Funcionario:

    salario_minimo = float(1620.00)
    
    
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def verificar_salario_minimo(self) -> str:
        
        return self.salario >= Funcionario.salario_minimo
    
    def __str__(self)-> str:
        return  f"A área do círculo com raio {self.raio} é {self.calcular_area():.2f}."

    