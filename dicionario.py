pessoa = {'Nome':'Ana','Idade':19, 'Cidade':'Belém','Telefone':'919961126487'}

# print(f"Nome: {pessoa['Nome']}")
# print(f"Idade: {pessoa['Idade']}")
# print(f"Cidade: {pessoa['Cidade']}")
# print(f"Telefone: {pessoa['Telefone']}")

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa)

for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")
    
#  Adicionar    
pessoa['Profissão']='Engenheiro'
print(pessoa)
#  Substituir    
pessoa['Profissão']='Administrador'
print(pessoa)

del pessoa['Profissão']
print(pessoa)

for p,z in pessoa.items():
    print (z) 
    
for z in pessoa.values():
    print(z)      
    
pessoa ["Notas"]=[7.0,8.0,9.0]
print(pessoa)

media = sum(pessoa["Notas"])/len(pessoa["Notas"]) 
print(f"a média é: {media}")  

print(pessoa.get('Profissão','Chave não encontrada'))