


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
    resultado=num1/num3
elif operacao == "**":
    resultado=num1**num3

print('a.A equação é: ',num1,operacao,num3,"=",resultado )
print("b. Onde o primeiro input foi ",num1,"o segundo foi", num3," e o terceiro ", operacao,".")


