import streamlit as st

# --- FUNÇÃO DE LÓGICA (Definida acima) ---
def classificar_idade_escolar(idade: int) -> str:
    """
    Classifica a série escolar com base na idade do aluno.
    """
    if idade < 0:
        return "Idade inválida: Digite um número positivo."
        
    if idade < 3:
        return 'Vá para o Berçário!'

    elif idade <= 5: 
        niveis_infantil = {3: 'N1 (3 anos)', 4: 'N2 (4 anos)', 5: 'N3 (5 anos)'}
        return f"Vá para a Educação Infantil na série {niveis_infantil.get(idade, 'Desconhecida')}"

    elif idade <= 14:
        serie = idade - 5
        return f"Vá para o Ensino Fundamental - {serie}º Ano"

    elif idade <= 17:
        serie = idade - 14
        return f"Vá para o Ensino Médio - {serie}º Ano"

    else:
        return 'Vá para a faculdade'
# ------------------------------------------


# --- INTERFACE STREAMLIT ---
# Define o título principal da aplicação
st.title("📚 Classificador Escolar por Idade")
st.markdown("Utilize a idade para descobrir a fase de ensino apropriada (baseado na legislação brasileira).")

# 1. Componente de Entrada de Número
# Usamos st.number_input para garantir que a entrada seja um número inteiro
idade = st.number_input(
    'Qual a idade do aluno?', 
    min_value=0, 
    max_value=120, 
    value=6, # Valor inicial
    step=1,
    help='Idade deve ser um número inteiro.'
)

# 2. Botão de Ação
if st.button('Verificar Fase Escolar', type="primary"):
    
    # Executa a lógica de classificação
    fase_escolar = classificar_idade_escolar(idade)

    # 3. Componente de Saída (Exibe o resultado)
    st.divider()
    st.subheader("Resultado da Classificação:")
    
    # Usa st.info ou st.success para destacar a mensagem
    if "inválida" in fase_escolar or "Desconhecida" in fase_escolar:
        st.error(fase_escolar)
    else:
        st.success(f"**{fase_escolar}**")
        
    st.caption('Fim da consulta.')

# ---------------------------