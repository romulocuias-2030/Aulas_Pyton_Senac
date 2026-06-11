# Sistema simples de cadastro de cliente
# Variáveis do cliente (inicialmente vazias)
nomes_clientes = []
telefones_clientes = []


opcao = ""

while opcao != "0":
    print("\n===== MENU CLIENTE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar cliente")
    print("3 - Editar cliente")
    print("4 - Excluir cliente")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Cadastro de Cliente ---")
        nome=input("Nome: ")
        telefone=input("telefone: ")
        if nome=="":
            print('Nome não pode ser vazio.')
        else:
            nomes_clientes.append(nome)
            telefones_clientes.append(telefone)
            print("cliente cadastrado.")

    elif opcao == "2":
        print("\n--- Listar Cliente ---")
        if len(nomes_clientes) == 0:
            print("! Nenhum cliente cadastrado.")

        else:
            for i in range (len(nomes_clientes)):
                print(f"{i} - Nome {nomes_clientes[i]} \n Telefone {telefones_clientes[i]}")

    elif opcao == "3":
        print("\n--- Editar Cliente ---")
        if len(nomes_clientes) == 0:
            print("! Nenhum cliente para editar")
        else:
            for i in range (len(nomes_clientes)):
                print(f"{i} - {nomes_clientes[i]}")
            try:
                indice = int(input('Digite o numero do cliente que deseja: '))
                if indice < 0 or indice>= len(nomes_clientes):
                    print("! Indice invalido.")
                else: 
                    novo_nome=input("Novo nome (Enter para manter): ")
                    novo_tel=input("Novo telefone (Enter para manter): ")
                    if novo_nome!="":
                        nomes_clientes[indice]=novo_nome
                    if novo_tel!="":
                        telefones_clientes[indice]=novo_tel
                    print("Cliente Atualizado")
            except ValueError:
                print("! Digite um numero válido.")
                
                
    elif opcao == "4":
        print("\n--- Excluir Cliente ---")
        if len(nomes_clientes) == 0:
            print("! Nenhum cliente para excluir: ")
        else:
            for i in range (len(nomes_clientes)):
                print(f"{i} - {nomes_clientes[i]}")
            try:
                indice = int(input('Digite o numero do cliente que deseja excluir: '))
                if indice < 0 or indice>= len(nomes_clientes):
                    print("! Indice invalido.")
                else: 
                    nomes_clientes.pop(indice)
                    telefones_clientes.pop(indice)
                    print("Cliente excluído")
            except ValueError:
                print("! Digite um numero válido.")