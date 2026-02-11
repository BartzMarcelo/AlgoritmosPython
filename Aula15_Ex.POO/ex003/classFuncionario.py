class Funcionario:

    salario_minimo = float(1412.00)
    
    
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def verificar_salario_minimo(self) -> bool:
        """Retorna True se o salário for maior ou igual ao mínimo da classe."""
        return self.salario >= Funcionario.salario_minimo
    