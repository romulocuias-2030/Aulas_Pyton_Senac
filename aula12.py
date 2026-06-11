print('==== MENU PRODUTOS====')
print()
print(' 1 - Cadastrar \n 2 - Listar\n 3 - Editar\n 4 - Excluir\n 0 - Sair')
print()
opcao=int(input("Escolha uma opção:  "))
produto_cadastrado=False

while opcao!=0:

    if opcao==1:
        print('======Cadastrar de produtos======\n')
        nome_produto=input('Digite o nome do produto: ')
        cod_produto=float(input('código do Produto: '))
        estoque=input('Digite a quantidade: ')
        preco=float(input('Digite o valor do produto: '))
        print(f'Nome: {nome_produto}\nCodigo do produto: {cod_produto}\nQuantidade: {estoque}\nValor do produto: {preco}')
        print('Cliente cadastrado com sucesso!')
        cliente_cadastrado=True
    
        
    elif opcao==2:
        print('Listar Cliente')
        if produto_cadastrado == True:
            print(f'Nome: {nome_cliente}\nTelefone: {telefone}\nEmail: {email}\nEndereço: {endereco}')
        else:
            print('Nenhum cliente cadastrado 😒')
    
    elif opcao==3:
        print('Editar cliente')
        if cliente_cadastrado == True:
           editar_nome=input('Digite o novo nome ou tecle enter para manter: ')
           editar_tel=input('Digite o novo Telefone ou tecle enter para manter: ')
           editar_email=input('Digite o novo Email ou tecle enter para manter: ')
           editar_ende=input('Digite o novo endereço ou tecle enter para manter: ')
           
           if editar_nome!="":
             nome_cliente=editar_nome
           if editar_tel!="":
             telefone=editar_tel
           if editar_email!="":
             email=editar_email 
           if editar_ende!="":
             endereco=editar_ende
             print('Cliente atualizado com sucesso!')
        else:
            print('Não há clientes para editar')  

    elif opcao==4:
        print('\n----Excluir cliente----\n')
        if cliente_cadastrado== True:
            confirmar=input('Tem certeza que deseja Excluir? (S/N): ').strip().upper()[0]
            if confirmar== "S":
                nome_cliente=""
                telefone=""
                email=""
                endereco=""
                cliente_cadastrado = False
                print('Dados excluídos')
            else:
                print('Operação cancelada')    
        else:
            print('Não há clientes cadastrados')    
        
    elif opcao==0:
        print('Sair')
        
    else:
        print('Opção inválida, tente denovo')
                
    
    resposta=input('Deseja continuar? (S/N): ').upper().strip()[0] 
    if resposta =='S':
        opcao=int(input("Escolha uma opção:  "))
    else:
        break
    
print('Fim de sessão')