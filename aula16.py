# lista1=[1,2,3]
# lista2=lista1

# lista2.append(4)
# print(lista2, lista1)

# cadastro_clientes
""" cliente=[]
cadastro_clientes=[]

while True:# laço de repetição para cadastrar cliente
    resp=input('Deseja cadastrar cliente? (s/n): ')
    if resp == "n":
       break
    cliente.append(input("Digite o nome do cliente: "))
    cliente.append(int(input("Digite a idade do cliente: ")))
    cliente.append(input("Digite o telefone do Cliente: "))
    cadastro_clientes.append(cliente[:]) # insere o cliente na lista
    cliente.clear() # limpa a lista
    print(cliente)
listar=input('Deseja listar os clientes cadastrados? (s/n):')
if listar == "s":
    cadastro_clientes.sort()# lista ordem alfabetica
    for cliente in cadastro_clientes:
        print("*"*20)
        print(f'Cliente: {cliente[0]}')
        print(f'idade: {cliente[1]}')
        print(f'Telefone: {cliente[2]}')  """   
        
        
# cadastro_produtos
produto=[]
cadastro_produtos=[]

while True:# laço de repetição para cadastrar cliente
    resp=input('Deseja cadastrar mais produtos? (s/n): ')
    if resp == "n":
       break
    produto.append(input("Digite o nome do produto: "))
    produto.append(float(input("Digite o valor do produto: R$")))
    produto.append(input("Digite a quantidade: "))
    cadastro_produtos.append(produto[:]) # insere o cliente na lista
    produto.clear() # limpa a lista
    print(produto)
print()
print()
listar=input('Deseja listar os produtos cadastrados? (s/n):')
if listar == "s":
    cadastro_produtos.sort()# lista ordem alfabetica
    for produto in cadastro_produtos:
        print("*"*20)
        print(f'Nome do produto: {produto[0]}')
        print(f'Preço: {produto[1]}')
        print(f'Quantidade: {produto[2]}')           