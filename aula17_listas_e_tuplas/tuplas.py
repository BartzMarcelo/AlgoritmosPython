"""
Tuplas ()
são imutáveis, não podem ser alteradas, tornando-as ideias para:
- coordenadas(x,y) em processamento de imagens.
- configurações que não devem ser alterdas.
-retorno multiplo de funções.

"""

coordenda = (10, 20)
rgb = (255, 128,0)
config = ('localhost', 8080, True)
# Tupls é imutável mas a lista dentro dela é mutável.
# t[0] 10 # Erro! Tupla é imutável.
t = ( 1, 2 , [3,4])
t[2].append(5)
print(t)#(1, 2, [3, 4, 5])