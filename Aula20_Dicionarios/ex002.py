# Exercício 2: Unicidade e IDs de Amostras (Sets)
# Você possui duas listas de IDs de pacientes que participaram de dois estudos clínicos diferentes. Alguns pacientes participaram de ambos.

estudo_A = {10, 22, 34, 45, 56, 78, 90}

estudo_B = {34, 45, 88, 90, 99, 110}

# Determine via código:

# Quais IDs são comuns aos dois estudos? (Interseção)

comuns = estudo_A & estudo_B
print(comuns)
print()

# Qual a lista completa de pacientes únicos envolvidos na pesquisa? (União)
completa = estudo_A | estudo_B
print(completa)
print(
    
)


# Quais pacientes participaram apenas do Estudo A e não do B? (Diferença)
somente_A = estudo_A ^ estudo_B
print(somente_A)
print()