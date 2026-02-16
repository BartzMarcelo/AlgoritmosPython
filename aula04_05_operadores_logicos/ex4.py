


import streamlit as st

st.title("Calculadora Simples")

num1 = st.number_input('Digite o primeiro número:', value=0.0)
num2 = st.number_input('Digite o segundo número:', value=0.0)
operacao = st.selectbox('Escolha a operação:', ['+', '-', '*', '/', '**'])

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        st.error("ERRO: Divisão por zero não é permitida.")
        resultado = "Indefinido"
elif operacao == "**":
    resultado = num1 ** num2
else:
    st.error("ERRO: Operação inválida.")
    resultado = "Inválida"

st.write(f"a. A equação é: {num1} {operacao} {num2} = {resultado}")
st.write(f"b. Onde o primeiro input foi {num1}, o segundo foi {num2} e o terceiro {operacao}.")


