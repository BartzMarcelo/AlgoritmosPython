num1 = int(input('Digite um némero: '))
num2 = int(input('Digite um némero: '))
num3 = int(input('Digite um némero: '))

if num1 > num2 and num1 > num3:
    print(num1," é o maior número.")
if num2 > num1 and num2 > num3:
    print(num2," é o maior número.")
else:
    print(num3," é o maior número.")


n1 = int(input('Digite um número: '))
n2 = int(input('Digite um némero: '))
n3 = int(input('Digite um némero: '))

# Inicializar a variável 'maior' como primeiro valor
maior = n1
# Comparar com o segundo
if n2 > maior:
    maior = n2

# Comparar com o terceiro
if num3 > maior:
    maior = n3

    print(f'\nO valor do maior numero é : {maior}.')
    
    