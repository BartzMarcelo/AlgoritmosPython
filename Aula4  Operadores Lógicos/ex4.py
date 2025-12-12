


num1 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))
operacao = input('Digite operação desejada: +, -, *, /, ** :') 


if operacao == "+":
    resultado=num1+num3
elif operacao == "-":
    resultado=num1-num3
elif operacao == "*":
    resultado=num1*num3
elif operacao == "/":
    if num3 != 0:
        resultado = num1/num3
    else:
        print("ERRO: Divisão por zero não é permitida.")
        resultado = "Indefinido"
    #resultado=num1/num3
elif operacao == "**":
    resultado=num1**num3
else:
    print("\nERRO: Operação inválida. Por favor, use +, -, *, /, ou **.")
    resultado = "Inválida" # Define o resultado como uma string de erro

print('\na. A equação é: ',num1,operacao,num3,"=",resultado )
print("\nb. Onde o primeiro input foi ",num1,"o segundo foi", num3," e o terceiro ", operacao,".")
print()


