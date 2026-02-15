resposta = ''

while  resposta not in ['S', 'N']:
    resposta = input('Deseja continuar? (S/N)').upper()
    if resposta not in ['S', 'N']:
        print('Opção inválida! Tente novamente.')
print('Ação registrada com sucesso!')