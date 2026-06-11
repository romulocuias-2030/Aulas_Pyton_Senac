nomes_produtos = []
valores_produtos = []


opcao = ""

while opcao != "0":
    print("\n===== MENU PRODUTO =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produto")
    print("3 - Editar produto")
    print("4 - Excluir produto")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    
    if opcao == "1":
        print("\n######### Cadastro de Produtos ######### ")
        produto=input("Nome: ")
        valor=float(input("Preço: R$"))
        if produto == "":
            print('Nome não pode ser vazio.')
        else:
            nomes_produtos.append(produto)
            valores_produtos.append(valor)
            print("Produto cadastrado com sucesso!")
            
    elif opcao == "2":
        print("\n######### Lista de Produtos ######### ")
        
        if len(nomes_produtos) == "":
            print('Nome não pode ser vazio.')
        else:
            for i in range(len(nomes_produtos)): 
                print(f"{i} - Nome {nomes_produtos[i]} \n Telefone {valores_produtos[i]}")
       
            
    elif opcao == "3":
        print("\n######### Editar Produtos ######### ")
        
        if len(nomes_produtos) == "":
            print('Nome não pode ser vazio.')
        else:
            for i in range(len(nomes_produtos)): 
                print(f"{i} - Nome {nomes_produtos[i]}")
        try:
            indice = int(input('Digite o numero do produto que deseja: '))
            if indice < 0 or indice>= len(nomes_produtos):
                print("! Indice invalido.")