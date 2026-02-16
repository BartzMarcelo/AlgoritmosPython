elfos = 'Três Anéis para os Reis-Elfos sob este céu;'
lista = elfos.split()
print (lista)

for palavra in lista:
    for letra in palavra:
        print(letra, end="-")
    print(palavra)