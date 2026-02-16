RESUMO DA SEÇÃO
1. Você pode passar informações para funções usando parâmetros. Suas funções podem ter quantos parâmetros forem necessários.

Um exemplo de função de um parâmetro:


def hi(name):
    print("Oi,", name)
 
hi("Greg")
 
Um exemplo de função de dois parâmetros:


def hi_all(name_1, name_2):
    print("Oi,", name_2)
    print("Oi,", name_1)
 
hi_all("Sebastian", "Konrad")
 
Um exemplo de função de três parâmetros:


def address(street, city, postal_code):
    print("Seu endereço é:", street, "St.,", city, postal_code)
 
s = input("Street: ")
p_c = input("Código postal: ")
c = input("Cidade: ")
address(s, c, p_c)
 
2. Você pode passar argumentos para uma função usando as seguintes técnicas:

passagem de argumento posicional em que a ordem dos argumentos passou importa (Ex. 1)
passagem de argumentos da palavra-chave (nomeada) na qual a ordem dos argumentos passados não importa (ex. 2)
uma combinação de passagem de argumento de posição e de palavra-chave (por exemplo, 3.)

Ex. 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # saídas: 3
subtra(2, 5) # saídas: -3
 
 
Ex. 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # saídas: 3
subtra(b=2, a=5) # saídas: 3
 
Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # saídas: 3
subtra(5, 2) # saídas: 3
 
É importante lembrar que argumentos de posição não devem seguir argumentos de palavra-chave. É por isso que, se você tentar executar o seguinte trecho:


def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # saídas: 3
subtra(a=5, 2) # Syntax Error
 
O Python não vai deixar e sinalizar um SyntaxError.

3. Você pode usar a técnica de passagem de argumento da palavra-chave para predefinir um valor para um determinado argumento:


def name(first_name, last_name="Smith"):
    print(first_name, last_name)
 
name("Andy") # saídas: Andy Smith
name("Betty", "Johnson") # saídas: Betty Johnson (the keyword argument replaced by "Johnson")
 