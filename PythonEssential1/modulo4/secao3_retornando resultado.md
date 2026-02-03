RESUMO DA SEÇÃO
1. Você pode usar a palavra-chave return para informar uma função para retornar algum valor. A declaração de return sai da função, por exemplo:


def multiply(a, b):
    return a * b
 
print(multiply(3, 4)) # saídas: 12
 
 
def multiply(a, b):
    return
 
print(multiply(3, 4)) # saídas: None
 
2. O resultado de uma função pode ser facilmente atribuído a uma variável, por exemplo:


def wishes():
    return "Feliz aniversário!"
 
w = wishes()
 
print(w) # saídas: Feliz aniversário!
 
Veja a diferença de saída nos dois exemplos a seguir:


# Exemplo 1
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
wishes() # saídas: Meus desejos
 
 
# Exemplo 2
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
print(wishes())
 
# saídas: Meus desejos
# Feliz aniversário!
 
3. Você pode usar uma lista como argumento de função, por exemplo:


def hi_everybody(my_list):
    for name in my_list:
   "woda": "água",
        print("Oi,", name)
 
hi_everybody(["Adão", "John", "Lucy"])
 
4. Uma lista também pode ser um resultado de função, por exemplo:


def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
 
print(create_list(5))
 