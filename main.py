import biblioteca as b

# Projeto por MARIA LUIZA BEZERRA DOS SANTOS

while True:
    # menu
    print("\n--- BEM VINDO(A) A BIBLIOTECA ---\n")
    print("1 - Inserir livro")
    print("2 - Remover livro")
    print("3 - Listar livro por ID")
    print("4 - Livros disponíveis para empréstimo")
    print("5 - Livros emprestados")
    print("6 - Listar livros de uma editora")
    print("7 - Listar todos os livros da biblioteca")
    print("8 - Emprestar livro")
    print("9 - Devolver livro")
    print("10 - Sair")

    op = int(input("Digite sua opção: "))

    if op==10:
        break
    if op>10 or op<0:
        print("\nOPÇÃO INVÁLIDA \nTente novamente!")

    if op == 1:
        print("\n- CADASTRO DE LIVROS -\n")
        b.cadastra_livro()
    elif op == 2:
        print("\n- REMOVEÇÃO DE LIVRO -\n")
        id = input("Digite o id do livro: ")
        print()
        b.remove(id)
    elif op == 3:
        print("\n- LISTAR UM LIVRO -\n")
        id = input("Digite o id do livro: ")
        print()
        b.lista_id(id)
    elif op == 4:
        print("\n- LIVROS DISPONÍVEIS -\n")
        b.lista_disponiveis()
    elif op == 5:
        print("\n- LIVROS EMPRESTADOS -\n")
        b.lista_emprestados()
    elif op == 6:
        editora = input("Digite o nome da editora: ")
        print(f"\n- LIVROS DA {editora.upper()} -\n")
        b.lista_editora(editora)
    elif op == 7:
        print("\n- NOSSO ACERVO -\n")
        b.lista_livros()
    elif op == 8:
        print("\n- EMPRESTIMO DE LIVRO -\n")
        id = input("Digite o id do livro: ")
        print()
        b.empresta_livro(id)
    elif op == 9:
        print("\n- DEVOLUÇÃO DE LIVRO -\n")
        id = input("Digite o id do livro: ")
        print()
        b.devolve_livro(id)