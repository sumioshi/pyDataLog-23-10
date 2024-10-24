# Importando o pyDatalog
from pyDatalog import pyDatalog

# Inicializando o pyDatalog
pyDatalog.create_terms('aluno, Nota, Nome, aprovado')

# Função para adicionar os fatos
def adicionar_fato_aluno(nome, nota):
    # Adicionando o fato de aluno no pyDatalog
    +aluno(nome, nota)

# Função para ler o arquivo e adicionar os fatos manualmente
def importar_dados_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            # Extraindo o nome e a nota da linha
            if 'aluno(' in linha:
                inicio = linha.find('("') + 2
                fim = linha.find('",')
                nome = linha[inicio:fim]  # Nome do aluno

                inicio_nota = linha.find(',', fim) + 1
                fim_nota = linha.find(').')
                nota = float(linha[inicio_nota:fim_nota])  # Nota do aluno

                # Adicionando o fato de aluno no pyDatalog
                adicionar_fato_aluno(nome, nota)
                print(f"Fato adicionado: aluno({nome}, {nota})")  # Debugging

# Definindo a regra para verificar se o aluno está aprovado
# Um aluno está aprovado se sua nota for maior ou igual a 7
aprovado(Nome) <= aluno(Nome, Nota) & (Nota >= 7)

# Importando os dados do arquivo
importar_dados_do_arquivo('alunos.txt')

# Fazendo uma consulta para verificar quais alunos estão aprovados
try:
    alunos_aprovados = aprovado(Nome)
    # Exibindo os alunos aprovados
    print("Alunos aprovados:")
    for resultado in alunos_aprovados:
        print(resultado[0])
except AttributeError as e:
    print("Erro: ", e)
