# 1.Variáveis e condicional simples:
# continuar = 's'
# while continuar == 's':
#     nome = 'João'
#     novo_nome = input('Digite um nome: ')
#     if nome.casefold() == novo_nome.casefold():
#         print('Pode entrar, por favor.')
#     else:
#         print('Não pode entrar, lamento.')

#     continuar = input('Deseja continuar? (s/n): ')

# print()

# 2. Lista com laço de repetição for e while:

# continuar = 's'
# salarios = []
# while continuar == 's' :
    
#     salarios.append(float(input('Digite o valor do salário:')))
#     continuar = input('Deseja continuar? (s/n): ') 

# for salario in salarios:
#     if salario <= 2500:
#         print(salario, ", salário baixo")   
#     elif salario > 2500 and salario <= 5000:
#         print(salario, ", salário médio")
#     elif salario > 5000 and salario <= 10000:
#         print(salario, ", salário alto")
#     else:
#         print(salario, ", salário alto")

# print()

# Problema 1 - valor hora
# Escreva um porograma que retorna o valor hora de um funcionario
# com base no seu salário mensal e horas trabalhdas.

# salario = float(input('Digite o valor do salário: '))
# horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
# valor_hora= salario/horas_trabalhadas
# print('O valor da hora trabalhada é de R$ ' ,valor_hora, '.'.

# Laço de repetição:

# for item in range(2,11,2):
#     print(item)

# Lista:

# nomes = []
# continuar = 's'

# while continuar == 's':

#     nomes.append(input('Digite um nome:'))
#     continuar= input('Deseja continuar? s/n: ' )

# print(nomes)

# for nome in nomes:
#     print(nome)
    
# senhas = ['abc', 'segura123', '12345', 'python123', 'oi' ]

# for senha in senhas:
#     if len(senha) >= 6:
#         print(senha, 'Pode fazer cadastro.')
#     else:
#         print(senha, 'Não pode.')

# while

tente
