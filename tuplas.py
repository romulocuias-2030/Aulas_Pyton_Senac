# frase[start][stop]
# frase = "programador de sistemas"

""" print(frase[:15])
print(frase[15:])
print(frase[9:21:4])
print(len(frase))
print(frase.find('sistemas'))
print(frase.count('a'))

frase = frase.replace('sistemas', 'Jogos')
print(frase)
frase = " ".join(frase)
print(frase) """

# *************************
""" nome = input("Digite seu nome completo: ")
print("\n**********MAIUSCULAS E MINUSCULAS*********")
print(f"Nome em maiúsculo = {nome.upper()}")
print(f"Nome em minúsculo = {nome.lower()}")
print("Comprimento do texto:  ",len(nome))

print("\n************CONTANDO POSIÇÃO**************")
print(f"Total de letras = {len(nome)-nome.count(' ')}")
for cont, c in enumerate(nome):
    print(cont, c, end=' ')
print(f"Seu primeiro nome é:{nome[0:6]}")
print("\n*************NOME NA LISTA***************") 
nomes = nome.split(" ")
print(nomes)
print("\n*************NOME E SOBRE NOME*************")
print(f"Seu primeiro nome é: {nomes[0]} e seu sobrenome é {nomes[1]}")  """  
# *************************
""" nomes = ('Ana','Maria','João','Pedro')
print("\n***********")
print(nomes)

print("\n***********")
print(nomes[0])

print("\n***********")
print(len(nomes))

print("\n***********")
print(f"Foram cadastrados {len(nomes)} clientes")

print("\n***********")
print(f"O primeiro cliente cadastrado foi {nomes[0]}")
print(f"O segundo cliente cadastrado foi {nomes[1]}")
print(f"O terceiro cliente cadastrado foi {nomes[2]}")
print(f"O quarto cliente cadastrado foi {nomes[3]}")

print("\n***********")
for n in nomes:
    print(n, end=",")
    
print("\n***********")
for c,n in enumerate(nomes):
    print(f"O {c+1}º cliente cadastrado foi {n}") """
# *************************

print("\n***********")
premios = ('moto','carro','viagem','casa')
for c,n in enumerate(premios):
    print(f"O {c+1}º prêmio é um(a) {n}")
dinheiro = (1000.00,2000.00,5000.00)
premiacao = premios+dinheiro
print("\n***********")
print(premiacao)

# *************************
from random import randint
print("\n**SORTEIO**************************")
numeros = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),)
for c in numeros:
    print(c, end=" ")
print("\n*******************************************")
print(f"O maior número sorteado é: {max(numeros)}")
print(f"O menor número sorteado é: {min(numeros)}")
print("\n*******************************************")

nums=[]
for c in range(0,5):
    num = int(input("Digite um número: "))
    nums.append(num)
print("\n*******************************************")
   
print(type(nums))
print("\n*******************************************")
nums=tuple(nums)
print(type(nums)) 
print("\n*******************************************")
 
print(f"Os digitados foram: {nums}")

# *************************

produtos = ('pão','salgado','suco','café','bolo')
print("\n*******************************************")
print(produtos)

print("\n*******************************************")
for produto in produtos:
    print(f'Produtos a venda: {produto}')
print("\n**SORTED*************************")
print(sorted(produtos))
print("\n*********************************")
print(f"O produto {produto} está na posição: {produtos.index('suco')}")
print("\n*********************************")
for produto in produtos:
    print(f"O produto {produto} está na posição: {produtos.index(produto)}")
    
print("\n**Tira teima*******************")
for pos, prod in enumerate(produtos):
    print(f'o produto {prod} está na posição {pos}')
    
print("\n**Passo final******************")
for produto in range(len(produtos)):
    print(f"O produto {produtos[produto]} está na posição: {produto}")