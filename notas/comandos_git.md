# Guia de Operações Git: Limpeza e Sincronização

Este guia documenta o fluxo de trabalho utilizado para remover diretórios do rastreamento do Git e sincronizar alterações entre máquinas.

---

## 1. Ciclo de Vida de um Commit

Para entender os comandos abaixo, é importante lembrar que o Git trabalha em três camadas:

* **Working Directory:** Onde você altera os arquivos.
* **Staging Area (Index):** Onde você prepara a "foto" do que será salvo.
* **Local Repository:** Onde o histórico é gravado.



---

## 2. Operações Realizadas

### **Verificação de Estado**
`git status`  
**O que faz:** Lista quais arquivos foram modificados, excluídos ou criados.  
**Uso técnico:** Essencial antes de qualquer commit para garantir que você não está enviando arquivos indesejados.

### **Preparação (Staging)**
`git add .`  
**O que faz:** Adiciona todas as modificações do diretório atual para a Staging Area.

### **Gravação de Histórico (Commit)**
`git commit -m "Sua mensagem aqui"`  
**O que faz:** Cria um novo ponto na história do projeto.  
**Importante:** Use sempre aspas duplas.

### **Sincronização com o Servidor (Push)**
`git push origin main`  
**O que faz:** Envia seus commits locais para o GitHub.

### **Conferência de Integridade**
`git log -1`  
**O que faz:** Exibe o último commit realizado.

---

## 3. Comandos de Manutenção e Sincronização

| Comando | Função |
| :--- | :--- |
| `rmdir <nome>` | Remove uma pasta física no Windows (deve estar vazia). |
| `git pull origin main` | **Essencial:** Atualiza seu PC com as mudanças do GitHub. |
| `git fetch --all` | Baixa as novidades do servidor sem aplicar ao código. |

---

> **Nota:** Mantenha seu arquivo `.env` fora do Git para sua segurança.

# Procedimentos de Clonagem e Gestão de Repositórios

Este guia detalha como baixar projetos do GitHub para a sua máquina local e como organizar os comandos por categorias.

---

## 1. Como Clonar para a Área de Trabalho

Para clonar um repositório diretamente para o seu Desktop, siga a sequência de comandos abaixo no PowerShell:

### **Passo a Passo**
1. **Navegar para o Desktop:**
   ```powershell
   cd ~/Desktop

   git clone [https://github.com/usuario/nome-do-projeto.git](https://github.com/usuario/nome-do-projeto.git)

   cd nome-do-projeto
    code .