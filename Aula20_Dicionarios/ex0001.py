# Crie um dicionário chamado treinamento com: modelo: "Random Forest", n_estimadores: 100 e max_depth: None.

# Adicione uma nova chave criterion com o valor "gini".

# Altere o valor de n_estimadores para 200.

# Remova a chave max_depth utilizando o método .pop().

# Imprima apenas as chaves do dicionário final.

print("Crie um dicionário chamado treinamento com: modelo: Random Forest, n_estimadores: 100 e max_depth: None.")  
treinamento = {
    "modelo": "Random Forest",
    "n_estimadores": 100,
    "max_depth": None,  
}
print(treinamento)
print()

print(f" Adicione uma nova chave criterion com o valor 'gini'.")
print()
treinamento["criterion"] = "gini"
print(treinamento)
print()

print(f"Altere o valor de n_estimadores para 200.") 
treinamento["n_estimadores"] = 200
print(treinamento)
print()

print("Remova a chave max_depth utilizando o método .pop().")   
treinamento.pop("max_depth")
print(treinamento)
print()

print(f"Imprima apenas as chaves do dicionário final.")  
print(treinamento.keys())
print()



