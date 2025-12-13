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
print('planeta no indice 10: ', planetas[10])  # Isso causará um erro IndexError