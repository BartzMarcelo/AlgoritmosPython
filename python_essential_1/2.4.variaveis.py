# Nomes de variáveis
# o nome da variável deve ser composto de letras maiúsculas ou minúsculas, dígitos e o caractere _ (sublinhado);
# o nome da variável deve começar com uma letra;
# o caractere de sublinhado é uma letra;
# as letras maiúsculas e minúsculas são tratadas como diferentes (um pouco diferente do que no mundo real - Alice e ALICE são os mesmos nomes, mas em Python são dois nomes de variáveis diferentes e, consequentemente, duas variáveis diferentes);
# o nome da variável não deve ser nenhuma das palavras reservadas do Python (as palavras-chave - explicaremos mais sobre isso em breve).
# Observe que as mesmas restrições se aplicam a nomes de função.

# O PEP 8 - Guia de Estilo para Código Python recomenda a seguinte convenção de nomenclatura para variáveis e funções em Python:
# os nomes de variáveis devem estar em letras minúsculas, com palavras separadas por sublinhados para melhorar a legibilidade (por exemplo, var, my_variable)
# nomes de funções seguem a mesma convenção que nomes de variáveis (por exemplo, fun, my_function)
# também é possível usar casos mistos (por exemplo, myVariable), mas apenas em contextos onde esse já é o estilo predominante, para manter a compatibilidade com a convenção adotada.

# Palavras-chave
# Dê uma olhada na lista de palavras que desempenham um papel muito especial em todos os programas Python.

# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
#  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Eles são chamados de palavras-chave ou (mais precisamente) palavras-chave reservadas. Eles são reservados porque você não deve usá-los como nomes: nem para suas variáveis, nem funções, nem quaisquer outras entidades nomeadas que você deseja criar.

# O significado da palavra reservada é predefinido e não deve ser alterado de forma alguma.

# Felizmente, devido ao fato de que o Python faz distinção entre maiúsculas e minúsculas, você pode modificar qualquer uma dessas palavras alterando 
# a letra de qualquer letra, criando assim uma nova palavra, que não é mais reservada.