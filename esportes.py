# Importando o pyDatalog
from pyDatalog import pyDatalog

# Inicializando o pyDatalog
pyDatalog.create_terms('gosta_de, Pessoa1, Pessoa2, Esporte, compartilham_esporte')

# Função para adicionar os fatos
def adicionar_fato_gosta_de(pessoa, esporte):
    # Adicionando o fato de gosta_de no pyDatalog
    +gosta_de(pessoa, esporte)

# Função para ler o arquivo e adicionar os fatos manualmente
def importar_dados_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            # Extraindo a pessoa e o esporte da linha
            if 'gosta_de(' in linha:
                inicio_pessoa = linha.find('("') + 2
                fim_pessoa = linha.find('",')
                pessoa = linha[inicio_pessoa:fim_pessoa]  # Nome da pessoa

                inicio_esporte = linha.find('",', fim_pessoa) + 3
                fim_esporte = linha.find('").')
                esporte = linha[inicio_esporte:fim_esporte]  # Esporte

                # Adicionando o fato de gosta_de no pyDatalog
                adicionar_fato_gosta_de(pessoa, esporte)
                print(f"Fato adicionado: gosta_de({pessoa}, {esporte})")  # Debugging

# Definindo a regra para verificar se duas pessoas gostam do mesmo esporte
# Duas pessoas compartilham o mesmo esporte se ambas gostam do mesmo esporte
compartilham_esporte(Pessoa1, Pessoa2, Esporte) <= (gosta_de(Pessoa1, Esporte)) & (gosta_de(Pessoa2, Esporte)) & (Pessoa1 != Pessoa2)

# Importando os dados do arquivo
importar_dados_do_arquivo('esportes.txt')

# Fazendo uma consulta para verificar quais pares de pessoas compartilham o mesmo interesse esportivo
pares_interessados = compartilham_esporte(Pessoa1, Pessoa2, Esporte)

# Exibindo os pares de pessoas que compartilham o mesmo interesse esportivo
print("Pares de pessoas que compartilham o mesmo interesse esportivo:")
for resultado in pares_interessados:
    print(f"{resultado[0]} e {resultado[1]} gostam de {resultado[2]}")
