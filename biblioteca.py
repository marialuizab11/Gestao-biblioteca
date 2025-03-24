import csv
import os

#alteração

#Estou na teste1
#estou na teste2

def imprime_livros(leitor, disponiveis=False, emprestados=False, procura_id=False, id=None, procura_editora=False, editora=None):
    next(leitor)
    tem_livros = False

    for linha in leitor:            
            if disponiveis and linha[5]!='1':
                continue
            if emprestados and linha[5]=='1':
                continue
            if procura_id and id is not None and linha[0]!=id:
                continue
            if procura_editora and editora is not None and linha[3]!=editora:
                continue

            tem_livros = True

            print("--------")
            print(f"ID: {linha[0]}")
            print(f"Título: {linha[1]}")
            print(f"Autor(a): {linha[2]}")
            print(f"Editora: {linha[3]}")
            print(f"Ano de publicação: {linha[4]}")
        
            if (linha[5] == '1'):
                print("Situação: Disponível")
            elif (linha[5]=='0'):
                print("Situação: Emprestado")

    if not tem_livros and emprestados==True:
        print("Não há livros emprestados!")
    elif not tem_livros and procura_id==True:
        print("ID não encontrado no acervo!")
    elif not tem_livros and procura_editora==True:
        print("Editora não encontrada no acervo!")
    elif not tem_livros:
        print("Biblioteca Vazia!")

def lista_livros():
    try:
        with open('livraria.csv', 'r') as arq:
            leitor = csv.reader(arq)       
            imprime_livros(leitor)        
    except FileNotFoundError:
        print("Erro ao abrir arquivo!")

def gera_id():
    id=1
    try:    
        with open("livraria.csv", "r", newline='') as arq:
            leitor = csv.reader(arq)
            dados = list(leitor)
            id = int(dados[len(dados)-1][0])+1
    except FileNotFoundError:
        pass
    return id

def input_com_validacao(tela, ano=False):
    while True:
        valor = input(tela).strip()
        if ano:
            if valor.isdigit() and len(valor) == 4 and int(valor)<=2024:
                return int(valor)
            else:
                print("\nPor favor, digite um ano válido!\n")
        elif valor:
            return valor
        else:
            print("\nEste campo não pode ser vazio. Tente novamente!\n")

def verifica_duplicidade(nome, autor):
    try:
        with open('livraria.csv', 'r',newline='') as arq:
            leitor = csv.reader(arq)
            dados = list(leitor)
            for linha in dados:
                if linha[1] == nome and linha[2] == autor:
                    print("\nO livro já existe no nosso acervo!\n")
                    return False
            return True
    except FileNotFoundError:
        print("Erro ao ler arquivo")


def cadastra_livro():
    keys = ['ID','TITULO', 'AUTOR', 'EDITORA', 'ANO', 'SITUACAO']
    book = {'ID': gera_id(),
            'TITULO': input_com_validacao('Digite o título do livro: '),
             'AUTOR': input_com_validacao("Digite o nome do autor: "),
             'EDITORA': input_com_validacao('Digite o nome da editora: '),
             'ANO': int(input_com_validacao('Digite o ano de publicação: ', ano=True)),
             'SITUACAO': 1}
    

    if verifica_duplicidade(book['TITULO'], book['AUTOR']):
        arq_existe = os.path.isfile("livraria.csv")
        try:
            with open('livraria.csv', 'a', newline='') as arq:
                escreve = csv.DictWriter(arq, fieldnames= keys)

                if not arq_existe: #se o arquivo não existir escreve o cabeçalho
                    escreve.writeheader()
                escreve.writerow(book)
                print(f"\nLivro adicionado à biblioteca com ID {book['ID']}!")
        except FileNotFoundError:
            print("Erro ao abrir arquivo!")

def remove(id):
    try:
        with open('livraria.csv', 'r',newline='') as arq:
            leitor = csv.DictReader(arq)
            livros = list(leitor)
            encontrado = False
            tem_livros = bool(livros)

            for livro in livros:
                tem_livros = True
                if livro['ID'] == str(id):
                    livros.remove(livro)
                    encontrado = True
                    print("Livro removido com sucesso!")
                    break

        if not encontrado:
            print("Livro não encontrado no acervo!")
        if not tem_livros:
            print("Biblioteca Vazia!")
        if livros or not tem_livros:
            with open ('livraria.csv', 'w', newline='') as arq:
                escreve = csv.DictWriter(arq, fieldnames=['ID','TITULO', 'AUTOR', 'EDITORA', 'ANO', 'SITUACAO'])
                escreve.writeheader()
                escreve.writerows(livros)
    except FileNotFoundError:
        print("Erro ao abrir arquivo!")
    

def lista_disponiveis():
    try:
        with open('livraria.csv', 'r',newline='') as arq:
            leitor = csv.reader(arq)
            imprime_livros(leitor, disponiveis=True)
    except FileNotFoundError:
        print("Erro ao abrir arquivo!")

def lista_emprestados():
    try:
        with open('livraria.csv', 'r',newline='') as arq:
            leitor = csv.reader(arq)
            imprime_livros(leitor, emprestados=True)
    except FileNotFoundError:
        print("Erro ao abrir arquivo!")

def lista_id(id):
    try:
        with open('livraria.csv', 'r',newline='') as arq:
            leitor = csv.reader(arq)
            imprime_livros(leitor, procura_id=True, id=id)
    except FileNotFoundError:
        print("Erro ao abrir arquivo!")


def lista_editora(editora):
    try:
        with open('livraria.csv', 'r',newline='') as arq:
            leitor = csv.reader(arq)
            imprime_livros(leitor, procura_editora=True, editora=editora)
    except FileNotFoundError:
        print("Erro ao abrir arquivo!")

def modifica_situacao(id, situacao):
    try:
        with open('livraria.csv', 'r',newline='') as arq:
            leitor = csv.DictReader(arq)
            livros = list(leitor)
            encontrado = False
            tem_livros = False

            for livro in livros:
                tem_livros = True
                if livro['ID'] == str(id):
                    if situacao == '1':
                        livro['SITUACAO'] = '1'
                        print("Livro devolvido com sucesso!")
                    elif situacao == '0':
                        livro['SITUACAO'] = '0'
                        print("Livro emprestado com sucesso!")
                    encontrado = True
                    break

        if not encontrado:
            print("Livro não encontrado no acervo!")
        if not tem_livros:
            print("Biblioteca Vazia!")
        
        with open ('livraria.csv', 'w', newline='') as arq:
            escreve = csv.DictWriter(arq, fieldnames=['ID','TITULO', 'AUTOR', 'EDITORA', 'ANO', 'SITUACAO'])
            escreve.writeheader()
            escreve.writerows(livros)
    except FileNotFoundError:
        print("Erro ao abrir arquivo!")

def empresta_livro(id):
    modifica_situacao(id, situacao='0')

def devolve_livro(id):
    modifica_situacao(id, situacao='1')