RESUMO DA SEÇÃO
1. Uma função pode chamar outras funções, ou até mesmo ela mesma. Quando uma função se chama, essa situação é conhecida como recursão, e a função que se chama e contém uma condição de terminação específica (ou seja, o caso base - uma condição que não diz à função para fazer chamadas adicionais para essa função) é chamado de função recursiva.

2. Você pode usar funções recursivas no Python para escrever um código limpo e elegante e dividi-lo em pedaços menores e organizados. Por outro lado, você precisa ter muito cuidado, pois pode ser fácil cometer um erro e criar uma função que nunca termina. Você também precisa se lembrar que as chamadas recursivas consomem muita memória e, portanto, às vezes podem ser ineficientes.

Ao usar a recursão, você precisa levar em consideração todas as vantagens e desvantagens.

A função fatorial é um exemplo clássico de como o conceito de recursão pode ser colocado em prática:



# Implementação recursiva da função fatorial.
 
def factorial(n):
    if n == 1: # O caso base (condição de rescisão).
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24
 