# Exercício 3: Mapeamento de Frequência (Iteração)
# Dada a lista de tags de processamento de imagens: tags = ["resize", "crop", "resize", "rotate", "normalize", "crop", "resize"].

# Crie um dicionário vazio chamado contagem.

# Percorra a lista tags e preencha o dicionário onde a chave é o nome da tag e o valor é a quantidade de vezes que ela aparece.

# Ao final, imprima o dicionário de contagem.

from collections import defaultdict
tags = ["resize", "crop", "resize", "rotate", "normalize", "crop", "resize"]

contagem = defaultdict(int)  

for tag in tags: contagem[tag] += 1
print(f"Contagem: {dict(contagem)}")
print()



