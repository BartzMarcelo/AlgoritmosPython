n = int(input("Digite um número: ")) 
print(n >= 100)

# Leia três números.
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
 
largest_number = max(number1, number2, number3)
 
# Imprimir o resultado.
print("O maior número é:", largest_number)

#Instruções condicional aninhadas, por exemplo:

x = 10
 
if x > 5: # True
    if x == 6: # False
        print("aninhado: x == 6")
    elif x == 10: # True
        print("aninhado: x == 10")
    else:
        print("aninhado: else")
else:
    print("else")

for i in range(10):
   print("O valor de i é atualmente", i)

for i in range(2, 8):
    print("O valor de i é atualmente", i)
 
 
