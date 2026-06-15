# matriz = [[1,2],[3,4]]

# print(matriz[0][0])
# print(matriz[0][1])
# print(matriz[1][0])
# print(matriz[1][1]) 


# Sistema de compras
""" lista_compras=[]

while True:
    print('\n-----Lista de compras-----')
    print('1 - Adicionar um item')
    print('2 - Remover um item')
    print('3 - Mostrar lista')
    print('4 - Sair')
    
    opcao=input('Escolha uma opção: ')
    
    if opcao == "1":
        item = input("Digite um item: ")
        lista_compras.append(item)
        print(f"{item} adicionado!")
        
    elif opcao == "2":
        item = input("Digite um item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} removido!")
        else:
            print("Item não encontrado!")
            
    elif opcao == "3":
        print("Sua lista de compras", lista_compras) 
        
    elif opcao == "4":
        print("Saindo....")
        break  
    else:
        print("Opção invalida.")  """  
        
  

produtos=[]        
while True:
    print('\n-----Loja de eletronicos-----')
    print('1 - Cadastrar produtos')
    print('2 - Listar produto')
    print('3 - Vender produto')
    print('4 - Mostrar estoque')
    print('5 - Sair')
    
    opcao=input('Escolha uma opção: ')
    
    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        estoque = int(input("Quantidade no estoque: "))
        produtos.append([nome, preco, estoque])
        print(f"{nome} cadastrado com sucesso!")
        
    elif opcao == "2":
        print('\nProdutos cadastrados')
        for p in produtos:
            print(f"Item: {p[0]}\nPreço: R${p[1]}\nEstoque: {p[2]}")
            
    elif opcao == "3":
        nome = input("Digite o nome do produto para venda: ")
        encontrado = False
        for p in produtos:
            if p[0]==nome:
                encontrado = True
                if p[2]>0:
                    p[2]-=1
                    print(f"Venda realizada! {nome} agora tem {p[2]} unidades.")
                else:
                    print("Produto sem estoque")
                break
        if not encontrado:
            print("Produto não encontrado")
                            
    elif opcao == "4":
        total_itens = sum([p[2] for p in produtos])
        print(f"Total de itens em estoque: {total_itens}")
    
    elif opcao == "5":
        print("Saindo....")
        break  
    else:
        print("Opção invalida.")