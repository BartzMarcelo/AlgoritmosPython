print(" Ola, mundo!")
print() #Gera uma linha vazia. Bom para separar duas linhas entre si.
print("A aranha pequenininha\nsubiu a tromba d'água.")# \ = caractere de escape e vem de newline(nova linha). 
print()
print("abaixo veio a chuva\ne lavou a aranha.") # O uso de \n provoca uma quebra de linha.
print()
print("Meu nome é", "Python.", end=" ")
#  Uso de 1 de 2 argumentos da função print(), end=. Para usá-lo, é necessário conhecer algumas regras:  
# um argumento de palavra-chave consiste em três elementos: uma palavra-chave que identifica o argumento (end aqui); um sinal de igual (=); e um valor atribuído a esse argumento;
# qualquer argumento de palavra-chave deve ser colocado após o último argumento posicional (isso é muito importante)
# Em nosso exemplo, utilizamos o argumento chave end e o definimos como uma sequência contendo um espaço.
print("Monty Python.")
# Meu nome é Python. Monty Python.
print()
print("Meu", "nome", "é", "Monty", "Python.", sep="-")
# Meu-nome-é-Monty-Python.
print("Meu", "nome", "é", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
# Meu_nome_é*Monty*Python.*
# Os parâmetros end e sep podem ser utilizadas para formatar a saída do print().
# O parâmetro sep especifica o separador entre os argumentos de saída, por exemplo, print("H", "E", "L", "L", "O", sep="-"), 
# enquanto o parâmetro end especifica o que imprimir no final da impressão.









