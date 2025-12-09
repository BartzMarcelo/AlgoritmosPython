'''Funções para Números - built-in'''

print(pow(2,10))
a = pow(3,2)
print(a)
print()
b = abs(-11)
print(b)

quociente, resto = divmod(5,3)
print("O quociente é ", quociente, " e o resto é ", resto,".")

print(resto)

print( bin(7))

print( oct(80))
print( bin(80))
print( round(3.14152632, 4))

# Importar a classe matemática
import math

# Arrendondamento para cima
print(math.ceil(4.1))
# Arrendondamento para baixo
print(math.floor(5.9))
# Retorna o valor absoluto de um float
print( math.fabs(-5.4))
# Calcular Fatorial
print( math.factorial(5))
# Retorna o resto da divisão com float
print(math.fmod(5,4))
# Trunca um número retornando o inteiro
print( math.trunc(5.2))
# Eleva o primeiro número ao segundo
print ( math.pow(2,9))