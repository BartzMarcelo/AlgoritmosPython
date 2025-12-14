# Definindo uma lista vazia (o vetor) para armazenar as notas
notas_alunos = []
NUMERO_DE_ALUNOS = 5

print("--- Cadastro de Notas ---")

# Bloco para Receber os Dados (Popula a Lista)
# Usando um loop 'for' para iterar um número fixo de vezes
for i in range(NUMERO_DE_ALUNOS):
    while True:
        try:
            # Pede a nota e converte para float
            nota = float(input(f"Digite a nota do Aluno {i+1} (0 a 10): "))
            
            # Validação simples para garantir que a nota está no intervalo correto
            if 0 <= nota <= 10:
                # Adiciona a nota válida à lista (vetor)
                notas_alunos.append(nota)
                break  # Sai do loop 'while' e passa para o próximo aluno
            else:
                print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número.")

print("\n--- Resultados da Avaliação ---")

# Bloco para Processar os Dados (Condicional Encadeada)
# Percorre a lista de notas com um loop e índice
for i, nota in enumerate(notas_alunos):
    
    # A Condicional Encadeada
    if nota >= 9.0:
        # PRIMEIRA CONDIÇÃO
        classificacao = "Excelente (A)"
    elif nota >= 7.0:
        # SEGUNDA CONDIÇÃO (elif)
        classificacao = "Bom (B)"
    elif nota >= 5.0:
        # TERCEIRA CONDIÇÃO (elif)
        classificacao = "Satisfatório (C)"
    else:
        # CONDIÇÃO PADRÃO (else)
        classificacao = "Insatisfatório (D) - Precisa melhorar"

    # Exibe o resultado para o aluno
    print(f"Aluno {i+1}: Nota {nota:.2f} -> Classificação: {classificacao}")
    print(notas_alunos)