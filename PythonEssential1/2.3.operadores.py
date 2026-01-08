# Operadores:

# Exponenciação: **
# print(2 ** 3)
# print(2 ** 3.)
# print(2. ** 3)
# print(2. ** 3.)
# 8
# 8.0
# 8.0
# 8.0
# Quando os dois ** argumentos são inteiros, o resultado também é um número inteiro;
# Quando pelo menos um argumento ** é um float, o resultado também é um float.

# Multiplicação:
# # print(2 * 3)
# # print(2 * 3.)
# # print(2. * 3)
# # print(2. * 3.)
# # 6
# # 6.0
# # 6.0
# # 6.0

# Divisão: 
# print(6 / 3)
# print(6 / 3.)
# print(6. / 3)
# print(6. / 3.)
# # 2.0
# 2.0
# 2.0
# 2.0
# O resultado produzido pelo operador de divisão é sempre um float, independentemente de parecer ou não ser um flutuante
# à primeira vista: 1 / 2, ou se parece com um inteiro puro: 2 / 1.

# Divisão de número inteiro (divisão arredondada)
# Um sinal // (barra dupla) é um operador de divisão inteira. Difere do padrão / operador em dois detalhes:

# seu resultado não possui a parte fracionária ‒ está ausente (para inteiros), ou é sempre igual a zero (para flutuantes); isso significa que os resultados são sempre arredondados;
# ele está de acordo com a regra integer vs. float.

# print(6 // 3)
# print(6 // 3.)
# print(6. // 3)
# print(6. // 3.)
# 2
# 2.0
# 2.0
# 2.0

# Restante (módulo): %
# print(14 % 4)
# 2
# Como você pode ver, o resultado é dois. É por isso que:

# 14 // 4 dá 3 → este é o quociente inteiro;
# 3 * 4 dá 12 → como resultado da multiplicação de quociente e divisor;
# 14 - 12 dá 2 → este é o restante.

# Este exemplo é um pouco mais complicado:
# print(12 % 4.5) 
# Qual é o resultado?
# 3.0 – não 3 mas 3.0. A regra ainda funciona:

# 12 // 4.5 dá 2.0,
# 2.0 * 4.5 dá 9.0,
# 12 - 9.0 dá 3.0.

# Operadores e suas prioridades

# 1 **
# 2 +, - unário
# 3 *, /, //, %
# 4 +, - binário

# Pontos principais
# 1. Uma expressão é uma combinação de valores (ou variáveis, operadores, chamadas para funções - você aprenderá sobre eles em breve) que resulta em um determinado valor, por exemplo, 1 + 2.

# 2. Operadores são símbolos especiais ou palavras-chave que são capazes de operar nos valores e realizar operações (matemáticas), por exemplo, o operador * multiplica dois valores: x * y.

# 3. Operadores aritméticos em Python: + (adição), - (subtração), * (multiplicação), / (divisão clássica ‒ sempre retorna um ponto flutuante), % (módulo ‒ divide o operando esquerdo pelo operando direito e retorna o restante da operação, por exemplo , 5 % 2 = 1), ** (exponenciação ‒ operando esquerdo elevado à potência do operando direito, por exemplo, 2 ** 3 = 2 * 2 * 2 = 8), // (floor/divisão inteira ‒ retorna um número resultante da divisão, mas arredondado para o número inteiro mais próximo, por exemplo, 3 // 2.0 = 1.0)

# 4. Um operador unário é um operador com apenas um operando, por exemplo, -1 ou +3.

# 5. Um operador binário é um operador com dois operandos, por exemplo, 4 + 5 ou 12 % 5.

# 6. Alguns operadores agem antes de outros - a hierarquia de prioridades:

# o operador ** (exponenciação) tem a prioridade mais alta;
# então o unário + e - (Nota: um operador unário à direita do operador de exponenciação se liga mais fortemente, por exemplo, 4 ** -1 é igual a 0.25)
# então: *, /, e %,
# e, por fim, a prioridade mais baixa: binário + e -.
# 7. Subexpressões entre parênteses são sempre calculadas primeiro, por exemplo, 15 - 1 * (5 * (1 + 2)) = 0.

# 8. O operador de exponenciação usa a associação do lado direito, por exemplo, 2 ** 2 ** 3 = 256.

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))