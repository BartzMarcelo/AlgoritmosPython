idade = int(input( 'Digite sua idade: '))

if idade < 16:
    print('Não pode  votar!')
elif idade == 16 or idade == 17:
    print('Voto opcional!')
elif idade >=18 and idade <= 70:
    print('Voto obrigatório!')
else:
    print('Voto opcional!')