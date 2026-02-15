valor = int(input( 'Digite um número: '))

if valor > 0 and valor % 2 == 0:
    print('É um par positivo.')
elif valor > 0 and valor % 2 == 1:
    print('É um ímpar positivo.')         
elif valor < 0 and valor % 2 == 0:
    print('É um par negativo.') 
elif valor < 0 and valor % 2 == 1:
    print( 'É um impar negativo. ')
else:
    print('É zero.')

if valor % 3 == 0 and valor % 2 == 1:
    print( valor, 'é multiplo de 3.')     
if valor % 5 == 0 and valor % 2 == 1:
    print( valor, 'é multiplo de 5.')       
if valor % 7 == 0 and valor % 2 == 1: 
   print( valor,'é multiplo de 7.')
else:
    print(valor,'não é múltiplo de 3, 5 e 7.')
 