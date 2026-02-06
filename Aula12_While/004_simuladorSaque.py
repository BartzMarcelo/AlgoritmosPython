saldo = 500

condicao = '1'

while condicao != '0':
    print(f'Saldo é de R$ {saldo:.2f}.')
    sacar = float(input('Quanto deseja sacar?'))
    print(f'O valor a sacar é de {sacar:.2f}.')
    if sacar >= saldo:
        print('Saldo insuficiente.')      
    else:
        saldo = saldo-sacar
        print(f'Seu saldo atual é {saldo:.2f}') 
           
    condicao = input('Deseja a continuar a sacar? ')
print('Obrigado por usar nosso banco.')