'''
Listas são coleções  ordenadas, mutáveis e indexadas que podem
conter elementos de tipos diferentes.
-'''

# Características Fundamentais

dataset = [ 1, 2.5, " classe_A", True, [ 1,2]]   # tipos mistos de dados

# Manipulação
# .append(x)      # Adiciona ao final
# .extend(iter)   # Estende com outra sequência
# .insert(i, x)   # Insere na posição i
# .remove(x)      # Remove primeira ocorrência de x
# .pop([i])       # Remove e retorna (último ou índice i)
# .clear()        # Remove todos os elementos
# .index(x)       # Retorna índice da primeira ocorrência
# .count(x)       # Conta ocorrências
# .sort()         # Ordena in-place (ascendente)
# .reverse()      # Inverte in-place
# .copy()         # Cópia superficial (shallow)

#Fatiamento - Slicing -> sintaxe: lista[ inicio:fim:passo]
dados = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# print(dados[2:5])[10, 11, 12]
# print(dados[:3]) [17, 18, 19] 
# print(dados[7:])[10, 12, 14, 16, 18]
# print(dados[::2])[10, 12, 14, 16, 18]
# print(dados[::-1]) [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
# print(dados[-3:])[17, 18, 19]
