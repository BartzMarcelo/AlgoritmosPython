RESUMO DA SEÇÃO
1. Uma variável que existe fora de uma função tem escopo dentro do corpo da função (exemplo 1), a menos que a função defina uma variável com o mesmo nome (exemplo 2 e exemplo 3), por exemplo:

Exemplo 1:


var = 2
 
 
def mult_by_var(x):
    return x * var
 
 
print(mult_by_var(7)) # saídas: 14
 
Exemplo 2:


def mult(x):
    var = 5
    return x * var
 
 
print(mult(7)) # saídas: 35
 
Exemplo 3:


def mult(x):
    var = 7
    return x * var
 
 
var = 3
print(mult(7)) # saídas: 49
 
2. Uma variável que existe dentro de uma função tem escopo dentro do corpo da função (exemplo 4), por exemplo:

Exemplo 4:


def adding(x):
    var = 7
    return x + var
 
 
print(adding(4)) # saídas: 11
print(var) # NameError
 
3. Você pode usar a palavra-chave global seguida por um nome de variável para tornar o escopo da variável global, por exemplo:


var = 2
print(var) # saídas: 2
 
 
def return_var():
    global var
    var = 5
    return var
 
 
print(return_var()) # saídas: 5
print(var) # saídas: 5
 