# Declaração de variáveis  

valor = int(input("Digite um número: "))   
 # Bloco Aninhadi


if valor > 0:
    print("Valor positivo.")
    if valor % 3 ==0:
        print( valor," é multiplo de três.")
    elif valor % 5 == 0:
        print( valor," é multiplo de cinco.")
    else:
        print( valor," não é multiplo de três nem de cinco.")    

elif valor < 0:
    print("Valor negativo.")
    if abs(valor) % 7 == 0:
        print( valor, " é multiuplo de sete.")
    else:
        print( valor, " o valor não multiplo de 7")
    print("Valor igual a zero.")
else: 
    print("Valor igual a zero.") 


