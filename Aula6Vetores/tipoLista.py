# Uma lista de apenas inteiros
numeros = [1, 2, 3, 4, 5]

# Uma lista de strings
planetas = ["Mercúrio", "Vênus", "Terra", "Marte"]

# Uma lista de boleanos
respostas = [True, False, True, True]

# Uma lista composta por diferentes tipos de dados
misto = [1, "Olá", 3.14, False, [1, 2, 3]]

##################################################
# Mostra tipo da lista
planetas = ["Mercúrio", "Vênus", "Terra", "Marte"]
print(type(planetas))

# mostra toda lista de uma vez só
print('Lista de planetas :', planetas)

print(numeros)

# Mostra cada item individualmente de acordo com o indice

print('Primeiro planeta :', planetas[0])
print('Segundo planeta :', planetas[1]) 
print('Terceiro planeta :', planetas[2])
print('Quarto planeta :', planetas[3])

#Atribuir um novo valor a um indice especifico
planetas[1] = "Júpiter"
print('Lista de planetas atualizada :', planetas)
# print('planeta no indice 10: ', planetas[10])  # Isso causará um erro IndexError

# mostra cada item da lista do fim para o começo
print('Último planeta :', planetas[-1])
print('Penúltimo planeta :', planetas[-2])
print('Antepenúltimo planeta :', planetas[-3])      
print('Anteantepenúltimo planeta :', planetas[-4])

# mostra  intervalos de uma lista
# para isso usamos o operador :
# pegando todos os elementos a partir do segundo/
print('Planeta na posição 1 :',planetas[1])
# pegando todos os elementos até o terceiro (não inclui o índice 3)
print(planetas[:2])
print(planetas[1:3])
print(planetas)

print("")
print(planetas)
# Adicina novo elemento ao final da lista.
planetas.append('Vênus')
print(planetas)
# Remover último elemento da lista.
removido =planetas.pop()
print('')
print('Removido: ', removido)
print(planetas)
# Removendo um item específico.
segundo = planetas.pop(1)
print('')
print('Removido: ', segundo)
print(planetas)
print('')
planetas.append("Vênus")
print('')
print(planetas)
print('')
# Ordenar a lista.
print(planetas)
print('')
planetas.sort(reverse=True)
print(planetas)
print('')
planetas.sort
print(planetas)
print('')
planetas.reverse()
print(planetas)
print('')
# len retorna o tamanho da lista
print(len(planetas))
print('')

nome = 'Gandalf, o Cinzento., rabugento'
print((nome[5:]))
print(nome[:6])
print(nome[0])
parte = nome[3:8]
print(parte)
# nome[0] = 'F'  # -> É string e não objeto, portanto, não suporta.
print('')
# split divide uma lista
print(nome.split())
print('')
print(planetas) 
# join - Cria strings a partir de uma lista.
unir= ''.join(planetas)
print(unir)
print('')
juncao = '-'.join(planetas)
print(juncao)
print('')
