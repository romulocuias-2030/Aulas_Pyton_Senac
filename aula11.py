print('==== MENU CLIENTE====')
print()
print(' 1 - Cadastrar \n 2 - Listar\n 3 - Editar\n 4 - Excluir\n 0 - Sair')
print()
opcao=int(input("Escolha uma opção:  "))
cliente_cadastrado=False

while opcao!=0:

    if opcao==1:
        print('Cadastrar')
        nome_cliente=input('Digite o nome do cliente: ')
        telefone=input('Digite o telefone: ')
        email=input('Digite o email: ')
        endereco=input('Digite o endereço: ')
        print(f'Nome: {nome_cliente}\nTelefone: {telefone}\nEmail: {email}\nEndereço: {endereco}')
        print('Cliente cadastrado com sucesso!')
        cliente_cadastrado=True
    
        
    elif opcao==2:
        print('Listar Cliente')
        if cliente_cadastrado == True:
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
  

# Login e senha
# print('==== FAZER LOGIN ====')
# print()
# login='persons'
# senha=123456
# logar=(input("Digite seu login:  "))
# s=int(input("digite sua senha:  "))


# if senha!=s and login!=logar:
#     print('dados incorretos!')
#     logar=(input("Digite seu login:  "))
#     s=int(input("digite sua senha:  "))
        
# elif senha!=s or login!=logar:
#     print('Login ou senha incorretos!')
#     logar=(input("Digite seu login:  "))
#     s=int(input("digite sua senha:  "))
        
# elif senha==s and login==logar:
#     print(f'Seja bem vindo: {logar}')

    
    


# passoword=123456
# user='persons'

# login=(input("Digite seu login:"))
# senha=int(input("Digite sua senha:"))


# while senha!=123456:
#     print("Senha incorreta")
#     senha=int(input("Digite sua senha:"))
    
# print('Seja bem vindo: ')