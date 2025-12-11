idade = int(input( 'Digite sua idade: '))

if idade < 3:
    print('Vá para o Berçario!')
elif idade >=3 and idade <= 5:
    if idade == 3: 
        print('Vá para a Educação Infantil na série N1 (3 anos)')
    elif idade == 4:
        print('Vá para a Educação Infantil na série N2 (4 anos)')
    else: 
        print('Vá para a Educação Infantil na série N3 (5 anos)')    
elif idade >=6 and idade <= 14:
    if idade == 6:
        print('Vá para o Ensino Fundamental - 1º Ano')
    elif idade == 7:
        print('Vá para o Ensino Fundamental - 2º Ano')
    elif idade == 8:
        print('Vá para o Ensino Fundamental - 3º Ano')
    elif idade == 9:
        print('Vá para o Ensino Fundamental - 4º Ano')
    elif idade == 10:
        print('Vá para o Ensino Fundamental - 5º Ano')
    elif idade == 11:
        print('Vá para o Ensino Fundamental - 6º Ano')
    elif idade == 12:
        print('Vá para o Ensino Fundamental - 7º Ano')
    elif idade == 13:
        print('Vá para o Ensino Fundamental - 8º Ano')
    elif idade == 14:
        print('Vá para o Ensino Fundamental - 9º Ano')
elif idade >=15 and idade <= 17:
    if idade == 15:
        print('Vá para o Ensino Médio - 1º Ano')
    elif idade == 16:
        print('Vá para o Ensino Médio - 2º Ano')
    elif idade == 17:
        print('Vá para o Ensino Médio - 3º Ano')
else:
    print('Vá para faculdade')
    

