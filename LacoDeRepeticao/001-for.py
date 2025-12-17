for i in [1, 2, 3, 4 ,5]:
    print('i =', i)
print('')
planetas = ['Mercurio', 'Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Netuno']   
print(planetas)
for i in planetas:
    print('i =', i)
print('')

# range(inicio, fim, passo)
for i in range(5):
    print('i =', i) 
print('-----------------------')
for i in range(2,21,2):
    print('i =', i)
print('-----------------------')
# Decremento.
for i in range(9, -1, -1):
    print('i =', i)
print('-----------------------')
for i in range(5,1):
    print('i =', i) 
print('-----------------------')
# lista = []
# for i in range(3):
#     texto = input('Digite algo: ')
#     lista.append(str(i) + ':' + texto)
# print(lista)
print('-----------------------')
# Casting para list do range.
numeros = range(0,10)
print(type(numeros))
print(numeros)
# Convertendo para uma lista
lista_num = list(numeros)
print(type(lista_num))
print(lista_num)
print('-----------------------')
for num in range(1,6):
    print('num =', num) 
print('-----------------------')
# Estrutura de repetição
for num in range(10):
    #Estrutura condicional
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é impar.')
print('-------')
# R E V I S Ã O
# print('-------')
# Tipo de dados
# int
# float
# listas (append, pop, sort, reverse, split, join, list)
# print('-----------------------')
# ESTRURA Condicional

# # if -. simples
# # if ... else -. composta
# # if ... elif ... else -. encadeada
# if if -> aninhado


# Estrutura de Repetição(FOR)
# range(inicio, fim, passo)