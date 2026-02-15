# import pessoa

# lista_de_alunos = []


# continuar = '0'
# while continuar != '1':
#     if __name__ == '__main__':
#         print(f"\n--- Cadastro do Aluno nº {len(lista_de_alunos) + 1} ---")
#         # brasileiro = pessoa.Aluno('Brasil', 'Português', 18)
#         # # brasileiro.escreve()
#         # # brasileiro.fala()
#         # # brasileiro.anda()
#         # print(f'O aluno do {brasileiro.pais} fala {brasileiro.idioma} e tem {brasileiro.idade} anos.')
#         # print(f'Total de instâncias(objetos) criadas: {pessoa.Aluno.total_pessoas}')
#         # continuar = input('Digite 1 para sair: ')
#         print(f"\n--- Cadastro do Aluno nº {len(lista_de_alunos) + 1} ---")
#         # 2. Pegamos os dados dinamicamente
#         pais = input("País: ")
#         idioma = input("Idioma: ")
#         idade = int(input("Idade: ")) # Convertendo para inteiro
#         # 3. Instanciamos e ADICIONAMOS à lista
#         novo_aluno = pessoa.Aluno(pais, idioma, idade)
#         lista_de_alunos.append(novo_aluno)
        
#         print(f'Total de instâncias no sistema: {pessoa.Aluno.total_pessoas}')
#         # 4. Exibindo todos os cadastrados ao final
#         print('\n--- Lista Final de Alunos ---')
#         for aluno in lista_de_alunos:
#             print(f'Aluno do {aluno.pais} - {aluno.idioma} - {aluno.idade} anos.')
                
#         continuar = input('Digite 1 para sair ou qualquer tecla para continuar: ')
#     print()
# print('Programa encerrado!')

import funcoes

def executar():
    lista_de_alunos = []
    continuar = '0'

    while continuar != '1':
        # Usamos o prefixo "funcoes." para chamar o que está no outro arquivo
        novo_aluno = funcoes.cadastrar_aluno()
        lista_de_alunos.append(novo_aluno)
        
        continuar = input('Digite 1 para sair ou Enter para novo cadastro: ')

    funcoes.exibir_alunos(lista_de_alunos)
    print('Programa encerrado!')

if __name__ == '__main__':
    executar()