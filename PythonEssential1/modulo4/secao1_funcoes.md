RESUMO DA SEÇÃO
1. Uma função é um bloco de código que executa uma tarefa específica quando a função é chamada (chamada). Você pode usar funções para tornar seu código reutilizável, melhor organizado e mais legível. As funções podem ter parâmetros e valores de retorno.

2. Há pelo menos quatro tipos básicos de funções no Python:

incorporadas que são parte integrante do Python (como a função de print()). Você pode ver uma lista completa das funções integradas do Python em https://docs.python.org/3/library/functions.html.
os que vêm de módulos pré-instalados (você aprenderá sobre eles no curso Fundamentos do Python 2)
funções definidas pelo usuário que são escritas pelos usuários para os usuários - você pode escrever suas próprias funções e usá-las livremente no código,
as funções lambda (você aprenderá sobre elas no curso Fundamentos do Python 2.)
3. Você pode definir sua própria função usando a palavra-chave def e a seguinte sintaxe:

def your_function(optional parameters):
    # o corpo da função
 
Você pode definir uma função que não aceita argumentos, por exemplo:


def message(): # definindo uma função
    print("Olá") # o corpo da função
 
message() # chamando a função
 
Você pode definir uma função que aceita argumentos, assim como a função de um parâmetro abaixo:


def hello(name): # definindo uma função
    print("Olá,", name) # o corpo da função
 
 
name = input("Entre um valor: ")
 
hello(name) # chamando a função
 
Falaremos sobre funções parametrizadas na próxima seção.

