# Aula 17 - Manipulação de Dados para IA
# Foco: processamento de datasets e coordenadas

#Seção 1: Manipulação de Listas

def demonstrar_listas():
    '''Demonstra operações fundamentais com listas.'''



    print('=== Manipulação de Listas ===')

    # Criação de dataset simulado
    # Enxergue como uma MATRIZ
    dataset = [
        [5.1, 3.5, 'setosa'],
        [4.9, 3.0, 'setosa'],
        [7.0, 3.2, 'versicolor'],
        [6.4, 3.2, 'versicolor'],
        [6.3, 3.3, 'virginica']
    ]

    print(f"Dataset original({len(dataset)} amostras):")
    for i, amostra in enumerate(dataset, 1):
        print(f"{i}. {amostra}")


    # # Acesso e modificação

    print(f'\n --- Acesso e Modificação ---')
    primeira = dataset[0] # primeira amostra
    ultima = dataset[-1] # última posição  
    features = dataset[0:2]# Slicing: primeiros dois elementos
    label = dataset[0][2]

    print(f'Primeira amostra: {primeira}')
    print(f'última amostra: {ultima}')
    print(f'Features (X): {features}')
    print(f'Label(y): {label}')
        



        #Adição de dados



        # print('\n--- Adição de Dados ---')
    nova_amostra = [5.5, 2.3, 'virginica']
    dataset.append(nova_amostra) # adicionando ao final
    print(f'Após append:{len(dataset)}amostras')
                       

        #Inserção do início
    dataset.insert(0, [4.6, 3.1,'setosa'])
    print(f'Após insert(0): {len(dataset)}amostras')
    print(dataset)



        # Remoção de dados
    print(f'\n --- Remoção de dados ---')
    removido = dataset.pop() # remove o último
    print(f' Removido (pop): {removido}')
    print(f"Dataset original({len(dataset)} amostras):")

    dataset.pop(0 )# remove a amostra do índice passado entre parenteses
    print(f' Após pop(0): {len(dataset)} amostras')
                
    


        #Busca e contagem
    
    print(f'\n--- Busca e Contagem ---')

    #Extrair todas os labels usando list comprehension

    labels = [amostra[2] for amostra in dataset]
    print(f' Labels:{labels}')
    print(f'Contagem "setosa" :{labels.count("setosa")}')
    print(f"Índice primeiro 'versicolor': {labels.index('versicolor')}")



     #Ordenação

    print(f'\n--- Ordenação ___')
     #Ordena por primeira feature(índice 0 de cada sublista
     # key = lambada x: x[0] define a chave de ordenação



    dataset_ordenado = sorted(dataset, key=lambda x: x[0])
    print(' Dataset ordenado por feature1: ')
    for amostra in dataset_ordenado:
        print(f'   {amostra}')                              


#===================================
# Seção 2 - Slicing avançado
#===================================

def demonstrar_slicing():
    """ Demonstrar técnicas avançadas de fatiamento"""
    print('\n=== SLINCING AVANÇADO===\n')

    #Simular uma série temporal(temperaturas horárias)
                   # ìndices de 0 a 11
    temperaturas = [22, 23, 25, 28,30, 29, 27, 24,22 ,21 ,20 , 19]
    print(f'Dados completos{temperaturas}')
    print(f'Total de horas: {len(temperaturas)}')
    # Análise temporal com slicing
    madrugada = temperaturas[:6] #00h as 05
    manha  = temperaturas[6:12]# 06 as 12
    ultima_3h = temperaturas[-3:]# últimas 3 horas
    print(f'\nManhã (00 - 05): {madrugada}')
    print(f' Média madrugada: {sum(madrugada)/len(madrugada):.1f}°C')
    print(f'\nmanha(06-12: {manha}')
      print(f' Média : {sum(madrugada)/len(madrugada):.1f}°C')
    print*(f'\n Últimas 3h: {ultimas_3h}')









# # Seção 3 - Tuplas e Imutabilidade
def demonstrar_tuplas():



# #Seção 4 - Compreensão de listas
def demonstrar_compreensoes():

# Execução - Main


# demonstrar_listas()
demonstrar_slicing()