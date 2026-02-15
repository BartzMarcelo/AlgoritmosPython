RESUMO DA SEÇÃO
1. Em Python, há uma distinção entre dois tipos de erros:

erros de sintaxe (erros de análise), que ocorrem quando o analisador se depara com uma declaração que está incorreta. Exemplificando:
Tentando executar a seguinte linha:


print("Olá Mundo!)
 
causará um SyntaxError e resultará na seguinte mensagem (ou similar) no console:

Preste atenção na seta: ela indica o local em que o analisador Python teve problemas. No nosso caso, é a aspas duplas ausentes. Você percebeu isso?

Output
File "main.py", line 1
 
    print("Olá Mundo!)
                        ^
SyntaxError: EOL while scanning string literal
exceções, que ocorrem mesmo quando uma declaração / expressão está sintaticamente correta; Esses são os erros que são detectados durante a execução quando seu código resulta em um erro que não é tradicionalmente fatal. Exemplificando:
Tentando executar a seguinte linha:


print(1/0)
 
causará uma exceção ZeroDivisionError e resultará na seguinte mensagem (ou similar) no console:

Traceback (most recent call last):
  File "main.py", line 1, in
    print(1/0)
ZeroDivisionError: division by zero
Preste atenção na última linha da mensagem de erro - ela realmente informa o que aconteceu. Há muitos tipos diferentes de exceções, como ZeroDivisionError, NameError, TypeError e muito mais; e esta parte da mensagem informa que tipo de exceção foi gerada. As linhas anteriores mostram o contexto em que a exceção ocorreu.

2. Você pode "capturar" e manipular exceções no Python usando o bloco try-except. Portanto, se você suspeitar que qualquer trecho específico pode gerar uma exceção, você pode escrever o código que tratará normalmente e não interromperá o programa. Veja o exemplo:


while True:
    try:
        number = int(input("Insira um número inteiro: "))
        print(number/2)
        break
    except:
        print("Aviso: o valor inserido não é um número válido. Tente novamente...")
 
O código acima solicita a entrada do usuário até que ele digite um número inteiro válido. Se o usuário digitar um valor que não pode ser convertido em um int, o programa exibirá Aviso: o valor inserido não é um número válido. Tente novamente..., e peça ao usuário para inserir um número novamente. O que acontece nesse caso?

O programa entra no loop while.
O bloco try é executado. O usuário digita um valor errado, por exemplo: Olá!.
Uma exceção ocorre e o restante da cláusula try é ignorado. O programa salta para o bloco de except, executa-o e, em seguida, continua a executar após o bloco try-except.
Se o usuário digitar um valor correto e nenhuma exceção ocorrer, as instruções subsequentes no bloco try serão executadas.

3. Você pode lidar com várias exceções no seu bloco de código. Veja os seguintes exemplos:


while True:
    try:
        number = int(input("Digite um número int: "))
        print(5/number)
        break
    except ValueError:
        print("Valor errado.")
    except ZeroDivisionError:
        print("Desculpe. Não consigo dividir por zero.")
    except:
        print("eu não sei o que fazer...")
 
Você pode usar vários blocos except em uma instrução try e especificar nomes de exceção específico. Se uma das except for executada, as outras serão ignoradas. Lembre-se: você pode especificar uma exceção interna específica apenas uma vez. Além disso, não se esqueça que a exceção padrão (ou genérica), sem nome especificado, deve ser colocada na parte inferior (use primeiro as exceções mais específicas e a última mais geral).

Você também pode especificar e lidar com várias exceções integradas em uma única cláusula except:


while True:
    try:
        number = int(input("Digite um número int: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor errado ou nenhuma divisão por regra de zero quebrada.")
    except:
        print("Desculpe, algo deu errado...")
 
4. Algumas das exceções internas mais úteis do Python são: ZeroDivisionError, ValueError, TypeError, AttributeError e SyntaxError. Mais uma exceção que, em nossa opinião, merece sua atenção é a exceção KeyboardInterrupt, que é acionada quando o usuário pressiona a tecla de interrupção (CTRL-C ou Excluir). Execute o código acima e pressione a combinação de teclas para ver o que acontece.

Para saber mais sobre as exceções integradas ao Python, consulte a documentação oficial do Python.

5. Por último, mas não menos importante, você deve se lembrar sobre como testar e depurar seu código. Use técnicas de depuração, como depuração de print ; se possível - peça a alguém para ler seu código e ajudá-lo a encontrar bugs ou aprimorá-lo; tente isolar o fragmento de código problemático e suscetível a erros: teste suas funções aplicando valores de argumento previsíveis e tente lidar com as situações em que alguém insere valores errados; comentem as partes do código que ocultam o problema. Por fim, faça pausas e retorne ao seu código com um novo olhar.