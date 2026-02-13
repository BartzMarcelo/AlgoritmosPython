#Tradicional

quadrados = []

for x in range(10):
    quadrados.append(x**2)

# print(quadrados)[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Compressão ( mais rápido e legível)
quadrados2 = [x**2 for x in range(10)]
# print( quadrados2)[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Com Filtro
pares = [x for x in range(20) if x % 2 == 0]
# print (pares)[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Com condicional ternário

categorias = ["alto" if x > 10 else "baixo" for x in pares]
print(categorias)