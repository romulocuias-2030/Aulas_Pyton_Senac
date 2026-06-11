# LISTA
# Tupla=()
# Lista[]
# nomes[1]="Romulo" >>> Atualizar
# nomes.pop() deleta o ultimo da lista
# nomes.append("Romulo") Adicionar a lista na ultima posição
# produtos.insert(2,'café'), insere na posição...sem apagar
# nomes=['Ana, Carlos, Marina, João']
# nomes.append("Romulo") #Adicionar a lista
# print (nomes)

# # LISTAR PRODUTOS
# produtos=['Arroz, feijão, macarrão']
# # LISTA TAREFAS
# tarefas=['Python, organizar, limpar']
# tarefas.append('le documentção')
# print("produtos: ",produtos)
# print("Tarefas", tarefas)

# LISTA ATIVIDADES
# atividades.clear() limpa listas
# produtos.extend(tarefas) junta listas

# atividades=produtos+tarefas
# print(atividades)
# print('Diferença')
# produtos.extend(tarefas)
# print("resposta produtos extend ", produtos)

# from random import randint
# numeros=[]
# for cont in range(4):
#     numeros.append(randint(1,10))
#     # (randint(2,10) entre 1 e 10 os numeros

# print(numeros)
# for cont in numeros:
#     print('Numeros aleatórios', cont)
    
#     print(numeros)
# for cont in range(len(numeros)):
#     print(f'{cont+1}º  número aleatório: {numeros[cont]}', sep='')
    
# print(f'a soma dos números é: {sum(numeros)}')
# print(f'o número maior é: {max(numeros)}')
# print(f'o número menor é: {min(numeros)}')

clientes=[]
print('Informe o nome e o telefone do cliente')
for cliente in range(2):
    clientes.append(input())
print(f'Cliente: {clientes[0]}')
print(f'Telefone: {clientes[1]}')

print('Ação1 - Lista Clientes', clientes)
 
cadastro_clientes=[]
cadastro_clientes.append(clientes[:])
print(f'Lista Cadastro de clientes: ', cadastro_clientes)

print('_____Segundo Cadastro__________')
print('Informe o nome e o telefone do cliente')
for cliente in range(2):
    clientes.append(input())
print(f'Cliente: {clientes[0]}')
print(f'Telefone: {clientes[1]}')

cadastro_clientes=[]
cadastro_clientes.append(clientes[:])
print(f'Lista Cadastro de clientes: ', cadastro_clientes)