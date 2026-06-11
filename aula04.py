# # Loja de Tecnologia
# nome_produto="software"
# nome_produto2="notboock"
# nome_produto_preco=450.0
# nome_produto2_preco=1500.0
# nome_produto_codigo=1230
# nome_produto2_codigo=1231
# nome_cliente="Romulo"
# idade=52
# genero="masculino"
# nome_cliente2="Maria"
# idade2=27
# genero2="feminino"
# print("Dados do cliente")
# print(f'Nome: {nome_cliente}\nIdade: {idade}\nGênero: {genero}')
# print(f'Produto: {nome_produto}\nPreço: {nome_produto_preco}\nCódigo do produto: {nome_produto_codigo}')
# print()
# print("Dados do segundo Cliente")
# print(f'Nome: {nome_cliente2}\nIdade: {idade2}\nGênero: {genero2}')
# print(f'Produto: {nome_produto2}\nPreço: {nome_produto2_preco}\nCódigo do produto: {nome_produto2_codigo}')


nome=input("Digite seu nome:")
idade=int(input("Idade:"))
endereco=input("Enderço:")
estado_civil=input("Estado Civil:")
escolaridade=input("Grau de instrução:")
salario1=float(input("Digite o primeiro valor:R$"))
salario2=float(input("Digite o segundo valor:R$"))
salario3=float(input("Digite o terceiro valor:R$"))
media = (salario1+salario2+salario3)/3
print()
print("Dados do Cliente")
print(f'Nome: {nome}\nIdade: {idade}\nEndereço: {endereco}\nEstado civil: {estado_civil}\nGrau de instrução: {escolaridade}')
print(f"a média do salário é: R$ {media}")