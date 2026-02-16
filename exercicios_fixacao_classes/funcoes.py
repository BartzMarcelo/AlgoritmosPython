import pessoa

def cadastrar_aluno():
    print(f"\n--- Novo Cadastro ---")
    nome = input("Nome: ")
    pais = input("País: ")
    idioma = input("Idioma: ")
    # Dica: use o int() para garantir que a idade seja um número
    idade = int(input("Idade: "))
    
    return pessoa.Aluno(nome,pais, idioma, idade)

def exibir_alunos(lista):
    print('\n--- Lista Final de Alunos ---')
    for aluno in lista:
        print(f'Aluno(a) {aluno.nome} de {aluno.pais}, idioma {aluno.idioma}  com a idade de {aluno.idade} anos.')