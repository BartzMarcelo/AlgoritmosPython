while True:
    comando= input('Digite "sair" para fechar o programa: ')
    if comando.lower() == "sair":
        break # Interrompe o loop imediatamente.
print(f'Você digitou: {comando} .')