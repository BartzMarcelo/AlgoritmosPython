import streamlit as st

# Título do Aplicativo
st.title("Calculadora Si")

# 1. Inputs para os números
# Usamos st.number_input para obter números interativamente.
# O valor padrão é 0.0 para garantir que seja um float.
num1 = st.number_input('Digite o primeiro número:', value=0.0)
num3 = st.number_input('Digite o segundo número:', value=0.0)

# 2. Input para a operação
# Usamos st.selectbox para que o usuário escolha uma operação válida.
operacao = st.selectbox(
    'Selecione a operação desejada:',
    ('+', '-', '*', '/', '**')
)

# Variável para armazenar o resultado
resultado = None
erro_divisao = False

# 3. Lógica da Calculadora
if operacao == "+":
    resultado = num1 + num3
elif operacao == "-":
    resultado = num1 - num3
elif operacao == "*":
    resultado = num1 * num3
elif operacao == "/":
    if num3 != 0:
        resultado = num1 / num3
    else:
        # Se for divisão por zero, definimos uma flag e o resultado como None
        erro_divisao = True
        resultado = "Indefinido (Divisão por zero)"
elif operacao == "**":
    resultado = num1 ** num3

# 4. Exibição dos Resultados
st.header("Resultado")

# Exibe o resultado da equação
if erro_divisao:
    st.error("ERRO: Divisão por zero não é permitida.")
    st.markdown(f'a. A equação é: **{num1} {operacao} {num3} = Indefinido**')
else:
    # Formatação mais clara para exibir a equação e o resultado
    st.markdown(f'a. A equação é: **{num1} {operacao} {num3} = {resultado}**')

# Exibe os inputs originais
st.info(f"b. Onde o primeiro input foi **{num1}**, o segundo foi **{num3}** e a operação foi **{operacao}**.")