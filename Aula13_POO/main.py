"""Fazer os imports, se necessário."""
import veiculo
import os

if __name__ == '__main__':
    volvo = veiculo.Carro('Volvo', 'Verde', 2000)
    # volvo.buzina()
    # volvo.toggle_pisca()
    # volvo.buzina()
    fusca = veiculo.Carro('Fusca', 'Azul','1987')
    # print(f'Quantidade de rodas do {volvo.modelo} é {volvo.qtd_rodas}')
    # print(f'Quantidade de rodas do {fusca.modelo} é {fusca.qtd_rodas}')
    #print(f'Total de carros criados {veiculo.Carro.total_carros}.')
    bmw = veiculo.Carro('Brasília muito velha', 'Prata',1950)
    print(f'Total de carros criados {veiculo.Carro.total_carros}.')
      
    
    

# import veiculo
# import os

# ARQUIVO_DADOS = 'carros_cadastrados.txt'

# def carregar_historico():
#     """Lê o arquivo apenas para atualizar o contador global da classe."""
#     if os.path.exists(ARQUIVO_DADOS):
#         with open(ARQUIVO_DADOS, 'r') as arquivo:
#             for linha in arquivo:
#                 # O strip remove o \n e o split separa pela vírgula
#                 dados = linha.strip().split(',')
#                 if len(dados) == 3:
#                     m, c, a = dados
#                     # Recria o objeto apenas para o veiculo.Carro.total_carros subir
#                     veiculo.Carro(m, c, int(a))

# if __name__ == '__main__':
#     # 1. Carrega os carros que já foram salvos anteriormente
#     carregar_historico()
#     continuar = '0'
#     while continuar != '1':
#         # 2. Realiza o novo cadastro (Apenas uma vez)

#         print("--- CADASTRO DE NOVO CARRO ---")
#         modelo = input("Digite o modelo do carro: ")
#         cor    = input("Digite a cor do carro: ")
#         ano    = int(input("Digite o ano do carro: "))

#         # 3. Cria o objeto na memória (isso soma +1 ao total_carros)
#         carro_usuario = veiculo.Carro(modelo, cor, ano)

#         # 4. Salva os novos dados no arquivo TXT
#         with open(ARQUIVO_DADOS, 'a') as f:
#             f.write(f"{modelo},{cor},{ano}\n")

#         # 5. Exibe o resultado final
#         print(f"\nO carro {carro_usuario.modelo} foi salvo com sucesso!")
#         print(f"Total de carros registrados: {veiculo.Carro.total_carros}")
#         continuar = input('Deseja continuar a cadastrar? 0/1 ')
#     print()
#     print('Sistema encerrado. Volte sempre.')




