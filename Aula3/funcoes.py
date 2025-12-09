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
# Retorna a raiz quadrada
print( math.sqrt(2))

### Valores Especiais ###
print( math.pi) # Valor de pi
print(math.e) # Valor de Euler
print( math.exp(4))# Euler elevado a n
print( math.log(1000,10)) # Retorna o logaritmo de um número pelo outro
print( math.log10(1000)) # Retorna o log 10 de um número 
#help(print)
grito = " Eu ESTOU GRITANDO!"
print( grito.lower()) # Passa para caixa baixa9 normal)
normal= " eu estou falando normalmente!"
print(normal.upper())# Passa para caixa alta
print(grito.capitalize()) # Somente a primeira letra maiúscula da frase
troca =' essa É UMA strING emBARALHADA' 
print( troca.swapcase()) # Inverte letra maiúscula para minúscula e vice-versa
espacos = '-', '    espacoso    ', '-'
print(espacos)
print('')
print('')
#.strip - remove os espaços em brancoem branco antes e depois da string
print( '-', '  tirando  ' .strip(), '-')
print('')
# .rstrip - retira os espaços à direita
print( '-', '  tirando  ' .rstrip(), '-')
# .lstrip - retira os espaços à esquerda
print( '-', '  tirando  ' .lstrip(), '-')

#replace - substitui uma string por outra, mas no print
texto = ' Um anel para todos governar, um anel para encontrar'
print(texto.replace('anel', 'pulseira'))
print(texto)
print()
# isalpha() - verifica se a string contém somente letras
p1 = "painel1"
print(p1.isalpha())
