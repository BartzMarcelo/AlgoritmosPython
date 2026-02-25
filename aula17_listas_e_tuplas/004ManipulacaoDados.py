# # Aula 17 - Manipulação de Dados para IA
# # Foco: processamento de datasets e coordenadas

# #Seção 1: Manipulação de Listas

# def demonstrar_listas():
#     '''Demonstra operações fundamentais com listas.'''



#     print('=== Manipulação de Listas ===')

#     # Criação de dataset simulado
#     # Enxergue como uma MATRIZ
#     dataset = [
#         [5.1, 3.5, 'setosa'],
#         [4.9, 3.0, 'setosa'],
#         [7.0, 3.2, 'versicolor'],
#         [6.4, 3.2, 'versicolor'],
#         [6.3, 3.3, 'virginica']
#     ]

#     print(f"Dataset original({len(dataset)} amostras):")
#     for i, amostra in enumerate(dataset, 1):
#         print(f"{i}. {amostra}")


#     # # Acesso e modificação

#     print(f'\n --- Acesso e Modificação ---')
#     primeira = dataset[0] # primeira amostra
#     ultima = dataset[-1] # última posição  
#     features = dataset[0:2]# Slicing: primeiros dois elementos
#     label = dataset[0][2]

#     print(f'Primeira amostra: {primeira}')
#     print(f'última amostra: {ultima}')
#     print(f'Features (X): {features}')
#     print(f'Label(y): {label}')
        



#         #Adição de dados



#         # print('\n--- Adição de Dados ---')
#     nova_amostra = [5.5, 2.3, 'virginica']
#     dataset.append(nova_amostra) # adicionando ao final
#     print(f'Após append:{len(dataset)}amostras')
                       

#         #Inserção do início
#     dataset.insert(0, [4.6, 3.1,'setosa'])
#     print(f'Após insert(0): {len(dataset)}amostras')
#     print(dataset)



#         # Remoção de dados
#     print(f'\n --- Remoção de dados ---')
#     removido = dataset.pop() # remove o último
#     print(f' Removido (pop): {removido}')
#     print(f"Dataset original({len(dataset)} amostras):")

#     dataset.pop(0 )# remove a amostra do índice passado entre parenteses
#     print(f' Após pop(0): {len(dataset)} amostras')
                
    


#         #Busca e contagem
    
#     print(f'\n--- Busca e Contagem ---')

#     #Extrair todas os labels usando list comprehension

#     labels = [amostra[2] for amostra in dataset]
#     print(f' Labels:{labels}')
#     print(f'Contagem "setosa" :{labels.count("setosa")}')
#     print(f"Índice primeiro 'versicolor': {labels.index('versicolor')}")



#      #Ordenação

#     print(f'\n--- Ordenação ___')
#      #Ordena por primeira feature(índice 0 de cada sublista
#      # key = lambada x: x[0] define a chave de ordenação



#     dataset_ordenado = sorted(dataset, key=lambda x: x[0])
#     print(' Dataset ordenado por feature1: ')
#     for amostra in dataset_ordenado:
#         print(f'   {amostra}')                              


# #===================================
# # Seção 2 - Slicing avançado
# #===================================

# def demonstrar_slicing():
#     """ Demonstrar técnicas avançadas de fatiamento"""
#     print('\n=== SLINCING AVANÇADO===\n')

#     #Simular uma série temporal(temperaturas horárias)
#                    # ìndices de 0 a 11
#     temperaturas = [22, 23, 25, 28,30, 29, 27, 24,22 ,21 ,20 , 19]
#     print(f'Dados completos{temperaturas}')
#     print(f'Total de horas: {len(temperaturas)}')
#     # Análise temporal com slicing
#     madrugada = temperaturas[:6] #00h as 05
#     manha  = temperaturas[6:12]# 06 as 12
#     ultima_3h = temperaturas[-3:]# últimas 3 horas
#     print(f'\nManhã (00 - 05): {madrugada}')
#     print(f' Média madrugada: {sum(madrugada)/len(madrugada):.1f}°C')
#     print(f'\nmanha(06-12: {manha}')
#       print(f' Média : {sum(madrugada)/len(madrugada):.1f}°C')
#     print*(f'\n Últimas 3h: {ultimas_3h}')
#     # Slincing com passo: dados de 2 em 2 hora

#     amostras_intervalo = temperaturas[::2]
#     print(amostras_intervalo)

#     # reversao para analise retroativa
#     tendencia = temperaturas[::-1]
#     print (tendencia)

                                    











# # # Seção 3 - Tuplas e Imutabilidade
# def demonstrar_tuplas():



# # #Seção 4 - Compreensão de listas
# def demonstrar_compreensoes():

# # Execução - Main


# # demonstrar_listas()
# demonstrar_slicing()# Aula 17 - Manipulação de Dados para IA
# Foco: processamento de datasets e coordenadas

# Seção 1: Manipulação de Listas

# Aula 17 - Manipulação de Dados para IA
# # Foco: processamento de datasets e coordenadas
def demonstrar_listas():
    """Demonstra operações fundamentais com listas."""

    print('\n=== Manipulação de Listas ===')

    # Criação de dataset simulado (Matriz)
    dataset = [
        [5.1, 3.5, 'setosa'],
        [4.9, 3.0, 'setosa'],
        [7.0, 3.2, 'versicolor'],
        [6.4, 3.2, 'versicolor'],
        [6.3, 3.3, 'virginica']
    ]

    print(f"Dataset original ({len(dataset)} amostras):")
    for i, amostra in enumerate(dataset, 1):
        print(f"{i}. {amostra}")

    # Acesso e modificação
    print('\n--- Acesso e Modificação ---')
    primeira = dataset[0] 
    ultima = dataset[-1] 
    features = dataset[0:2] # Slicing: primeiros dois elementos
    label = dataset[0][2]

    print(f'Primeira amostra: {primeira}')
    print(f'Última amostra: {ultima}')
    print(f'Features (X): {features}')
    print(f'Label (y): {label}')

    # Adição de dados
    print('\n--- Adição de Dados ---')
    nova_amostra = [5.5, 2.3, 'virginica']
    dataset.append(nova_amostra) 
    print(f'Após append: {len(dataset)} amostras')

    # Inserção no início
    dataset.insert(0, [4.6, 3.1, 'setosa'])
    print(f'Após insert(0): {len(dataset)} amostras')

    # Remoção de dados
    print('\n--- Remoção de Dados ---')
    removido = dataset.pop() # remove o último
    print(f'Removido (pop): {removido}')

    dataset.pop(0) # remove a amostra do índice 0
    print(f'Após pop(0): {len(dataset)} amostras')

    # Busca e contagem
    print('\n--- Busca e Contagem ---')
    labels = [amostra[2] for amostra in dataset]
    print(f'Labels: {labels}')
    print(f'Contagem "setosa": {labels.count("setosa")}')
    print(f"Índice primeiro 'versicolor': {labels.index('versicolor')}")

    # Ordenação
    print('\n--- Ordenação ---')
    # Ordena por primeira feature (índice 0) usando lambda
    dataset_ordenado = sorted(dataset, key=lambda x: x[0])
    print('Dataset ordenado por feature1:')
    for amostra in dataset_ordenado:
        print(f'   {amostra}')


# Seção 2 - Slicing avançado
def demonstrar_slicing():
    """Demonstrar técnicas avançadas de fatiamento"""
    print('\n=== SLICING AVANÇADO ===')

    # Simular uma série temporal (temperaturas horárias)
    temperaturas = [22, 23, 25, 28, 30, 29, 27, 24, 22, 21, 20, 19]
    print(f'Dados completos: {temperaturas}')
    print(f'Total de horas: {len(temperaturas)}')

    # Análise temporal com slicing
    madrugada = temperaturas[:6]    # 00h às 05h
    manha = temperaturas[6:12]      # 06h às 11h
    ultima_3h = temperaturas[-3:]   # Últimas 3 horas

    print(f'\nMadrugada (00 - 05): {madrugada}')
    print(f'Média madrugada: {sum(madrugada)/len(madrugada):.1f}°C')
    
    print(f'\nManhã (06 - 11): {manha}')
    print(f'Média manhã: {sum(manha)/len(manha):.1f}°C') # Corrigido cálculo para manha
    
    print(f'\nÚltimas 3h: {ultima_3h}') # Corrigido nome da variável e sintaxe

    # Slicing com passo: dados de 2 em 2 horas
    amostras_intervalo = temperaturas[::2]
    print(f'\nAmostragem (2h em 2h): {amostras_intervalo}')

    # Reversão para análise retroativa
    tendencia = temperaturas[::-1]
    print(f'Tendência reversa: {tendencia}')


# Seção 3 - Tuplas e Imutabilidade
def demonstrar_tuplas():
    """Demontra Tuplas em Contexto de IA"""
    print('\n=== TUPLAS E IMUTABILIDADE ===')

    #Aplicação 1: Coordenadas em processamento de imagem

    print("--- Coordenadas de Bounding Box ---")
    # Formato: (x_min, y_min, x_max, y_max) - Padrão em visão computacional
    bbox_rosto = (100, 150, 200, 200)
    print(f"Boundin box: {bbox_rosto}.")
    print(f"Coordenadas: x_min={bbox_rosto[0]}, y_min= {bbox_rosto[1]}")

    # Desampacotamento(tuple unpacking)
    x_min, y_min, x_max, y_max = bbox_rosto
    largura = x_max - x_min # Calcula a adimensão horizontal
    altura = y_max - y_min # Calcula a dimensão vertical
    area= largura * altura
    print(f"Dimensões: {largura} * {altura} Área: {area} pixel]")

    # Aplicação 2: Configurações do modelo
    print(f"\n--- Configuração de Hiperparâmetros ---")
    config_redes_neurais = {
        "resnet50": (224, 224, 3), # altura, largura, canais
        "vgg16": (224, 224, 3),
        "inception": (299, 299, 3)
    }

    for modelo, dimensoes in config_redes_neurais.items():
        altura, largura, canais = dimensoes
        print(f"{modelo}: {altura} x { largura} x {canais}  (total: {altura * largura*canais} pixels)")

        print()

    # Aplicação 3: retorno múltiplo de funções
    print(f"\n--- Retorno Múltiplo de Funções ---")

    def calcular_metricas(y_true, Y_pred):
        """
        Calcula métricas de classificação
        Retorna tupla: ( acurácia, precisão e recall)

        """

        # Simulação de cálculo 
        acuracia = 0.9
        precisao = 0.89
        recall = 0.95
        return acuracia, precisao, recall
    # Desempacotamento no retorno
    acc, prec, rec = calcular_metricas([], [])
    print( "Métricas - Acc: {acc}, prec: {prec}, Rec: {rec}")

    # Aplicação 4: Imutabilidade com segurança
    print(f"\n--- Segurança dos Dados ---")

    coordenadas_gps = (-23.5505, -46.6333) # São Paulo
    print(f"Coordendas GPS: {coordenadas_gps}")
    #coordenadas_gps[0] = 10 # Erro! TypeError; 'tuple' object does not support item assigment
    # Tupla é imutável!
    print(" A Tupla protege contra modificação acidental.")    

    print()
    coordenada = (-23.5505, -46.6333) # Exemplo: São Paulo
    print(f'Coordenada fixa: {coordenada}')
    print(f"Tipo: {type(bbox_rosto)}.")
    print()
    # Tuplas não aceitam atribuição: coordenada[0] = 0 geraria erro


# Seção 4 - Compreensão de listas
def demonstrar_compreensoes():
    """
    Demonstra list comprehensios para processamento eficiente

    """
    print("\n=== Compreensão de Listas ===\n")

    # Dataset bruto com valores faltantes(None)

    dados_brutos = [ 23.5, None, 45.2, None, 12.8, 56.0, None, 34.5]
    print(f"Dados brutos: {dados_brutos}")

    # Filtragem de valores válidos( data cleaning )
    # Sintaxe: [expressão for item  in lista if condição]  
    dados_limpos = [ x for x in dados_brutos if x is not None]
    print(f"Dados limpos : {dados_limpos}")
    print(f"Removidos: {len(dados_brutos) - len(dados_limpos)} ")


    # Normalização ( escala 0-1)
    min_val = min(dados_limpos)
    max_val = max(dados_limpos)
    normalizados =[ (x-min_val) / (max_val - min_val) for x in dados_limpos]
    print(f"\nNormalizados [0,1]: {[round(x, 3) for x in normalizados]}")

    # Categorização com condicional
    categorias =[f"alto" if x > 40 else "médio" if x > 25 else "baixo" for x in dados_limpos]
    print(f"\nCategorias: {categorias}")

    # Compreensão aninhada; matriz de confusão simulada
    print(f"\n --- Matriz de Distâncias ---")
    pontos = [ (0,0), (1,1), (2,2)]

    # calcular a distância Euclidiana entre todos os pares
 
    distancias = [ [((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5 for p2 in pontos] for p1 in pontos]
    print(" Matriz de Distancias")
    for linha in distancias:
        print(f"{[round(d,2) for d in linha]}")     


# Execução - Main
if __name__ == "__main__":
    demonstrar_listas()
    demonstrar_slicing()
    demonstrar_tuplas()
    demonstrar_compreensoes()