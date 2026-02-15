class Aluno:

    pernas = 2
    cabeca = 1
    braço = 2
    total_pessoas = int=0

    def __init__(self,nome, pais, idioma, idade):
        self.pais = nome
        self.nome = pais
        self.idioma = idioma
        self.idade = idade
        Aluno.total_pessoas +=1

    def escreve(sel):
        print('Aluno escrevendo')
    
    def fala(self):
        print('Aluno falando')

    def anda (self):
        print('Aluno andando')

        


