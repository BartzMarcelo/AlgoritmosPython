# Exercício 4: Análise de Dados Aninhados (Dicionário de Dicionários)
# Cenário: Você tem um dicionário que armazena o desempenho de diferentes modelos em diferentes métricas.


experimentos = {
    "Modelo_A": {"acuracia": 0.89, "tempo_treino": 120, "memoria": "4GB"},
    "Modelo_B": {"acuracia": 0.94, "tempo_treino": 450, "memoria": "8GB"},
    "Modelo_C": {"acuracia": 0.82, "tempo_treino": 80,  "memoria": "2GB"}
}
# Tarefa:

# Escreva um código que percorra esse dicionário e identifique qual o nome do modelo que possui a maior acurácia.


maior_acuracia_modelo = None
maior_acuracia = 0

for modelo, metricas in experimentos.items():
  
    if metricas["acuracia"] > maior_acuracia:
        maior_acuracia = metricas["acuracia"]
        maior_acuracia_modelo = modelo
print()
print(f' A maior acurácia está no { maior_acuracia_modelo}')
print()


print(f'\n Versão do professor Roberto\n')  

#1) Inicialização de dados:
melhor_modelo = ""# armazena
maior_acuracia = 0 # guardar o maior valor
#2) Loop - percorrer o dicionário
for modelo, metricas in experimentos.items():
    if metricas["acuracia"] > maior_acuracia:
        maior_acuracia = metricas["acuracia"]
        melhor_modelo = modelo
print()
print(f' A maior acurácia está no { melhor_modelo}, sendo o valor da acuracia {maior_acuracia}')
print()


# Adicione um novo modelo chamado "Modelo_D" ao dicionário, mas faça isso solicitando que o usuário (ou simulando uma entrada) forneça um dicionário com as mesmas três chaves de métricas.


print("--- Cadastro do Modelo_D ---\n")  

novas_metricas = {
    "acuracia": float(input("Digite a acurácia : ")),
    "tempo_treino": int(input("Digite o tempo de treino em segundos: ")),
    "memoria": input("Digite o valor da memória com GB: " )
}

experimentos["Modelo_D"] = novas_metricas
print()
print(f"Modelo_D: {experimentos['Modelo_D']}" ) 
print()  


print(f"Experiementos atualizado: {experimentos}")
print()
maior_acuracia_modelo = None
maior_acuracia = 0

for modelo, metricas in experimentos.items():
  
    if metricas["acuracia"] > maior_acuracia:
        maior_acuracia = metricas["acuracia"]
        maior_acuracia_modelo = modelo
print()
print(f'A maior acurácia está no { maior_acuracia_modelo}')
print()

print("Listando chaves com lista\n")
print(f"Modelos registrados: {list(experimentos.keys())}")




