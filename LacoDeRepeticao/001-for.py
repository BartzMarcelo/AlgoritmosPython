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

