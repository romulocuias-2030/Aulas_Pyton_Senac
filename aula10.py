# menu cliente
# ==== MENU CLIENTE====
# 1 - Cadastrar
# 2 - Listar
# 3 - Editar
# 4 - Excluir
# 0 - Sair
# Escolha uma opção
# Encerrando o programa


# print('==== MENU CLIENTE====')
# print()
# print(' 1 - Cadastrar \n 2 - Listar\n 3 - Editar\n 4 - Excluir\n 0 - Sair')
# print()
# opcao=int(input("Escolha uma opção:  "))

# while opcao!=0:

#     if opcao==1:
#         print('Cadastrar')
        
#     elif opcao==2:
#         print('Listar')
        
#     elif opcao==3:
#         print('Editar')
        
#     elif opcao==4:
#         print('Excluir')
        
#     elif opcao==0:
#         print('Sair')
        
#     else:
#         print('Opção inválida, tente denovo')
                
    
#     resposta=input('Deseja continuar? (S/N): ').upper().strip()[0] 
#     if resposta =='S':
#         opcao=int(input("Escolha uma opção:  "))
#     else:
#         break
    
# print('Fim de sessão') 
  

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

senha=''
login=''
tentativas=1

while tentativas<=3:
    if senha!=123 and login!='Paulo':
        print("Login ou senha incorreta")
        login=input('informe o seu login: ')
        senha=input('informe a senha: ')
        print("Acesso bloqueado")

         
            
# print('Acesso liberado')

# senha='123'
# t=0
# while t<3:
#     s=input("senha")
#     if


# senha='123'
# contador=1
# while tentativas<=3:
#     if senha!=123 and login!='Paulo':
#         login=input('informe o seu login: ')
#         senha=input('informe a senha: ')
        
#     print("Senha incorreta")
#     senha=int(input("Digite sua senha:"))