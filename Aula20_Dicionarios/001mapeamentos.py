"""
Dicionários são coleções mutáveis, indexadas por chaves (não por posição).

"""

config_modelo = {
    "nome": "Resnet50",
    "camadas": 50,
    "dropout": 0.5,
    "learning rate": 0.001,
    "prerained": True 
}

# Métodos Essenciais de Dicionário

    #Acesso seguro

#    .get(chave, default)# retorno default se não existir a chave
#    .setdefault(chave, val) # Insere chave com val senão existe

    # Visualizações (views)

#    .keys()   # retorna a visualização das chaves
#    .values() # retorna visualização dos valores
#    .items()   # retorna visualização dos pares (chave, valor)

    # Atualizão 

    # .update(outro_dict)  # Atualiza com pares de outro dict
    # .pop(chave)          # Remove e retorna o valor da chave
    # .popitem()           # Remove e retornar último por LIFO
    # .clear()             # Remove todos os itens

    
    # Criação Avançada
    # dict.fromkeys(interavel, valor)   # Cria dict com chaves do iteravel
    # {chave: valor for ...}            # Dict comprehension

    # Operações de conjuntos (álgebra de conjuntos)

# A = {1,2,3,4}
# B = {3,4,5,6}
   
# A|B     União: { 1,2,3,4,5,6}
# A & B   Intersecção: {3,4}
# A-B     Diferença: {1, 2}
# A ^ B   Diferença Simétrica:{ 1,2, 5, 6}
# A <= B  Subconjunto: False
# A >= B  Superconjunto: False





   
