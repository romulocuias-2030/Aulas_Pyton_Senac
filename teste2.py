""" # a:
# soma = 0
for produto in produtos:
    soma += precos[produtos.index(produto)]
print(f'o valor dos produtos é: R${soma:.2f}')

# b:
soma = 0
for produto in range(len(produtos)):
    soma += precos[produto]
print(f'o valor dos produtos é: R${soma:.2f}')
# c: """

soma = 0
contador = 0
notas = (7.5, 4.0, 6.5, 9.0, 3.5, 8.0)
aprovados = []  # Corrigido: alterado para lista para permitir adicionar itens

for nota in notas:
    soma += nota
    if nota >= 7.0:
        contador += 1
        aprovados.append(nota)  # Corrigido: adiciona a nota atual à lista de aprovados
        print(f"Aprovado em nota: {nota}")  # Corrigido: mostra a nota atual, não todas
    elif 5.0 <= nota < 7.0:
        print(f"Nota de recuperação: {nota}")
    elif nota < 5.0:
        print(f"Reprovado: {nota}")  
        
print(f'lista de aprovados: {aprovados}')  # Corrigido: exibe a lista diretamente              
print(f'A média da turma é: {soma/(len(notas)):.1f}')
print(f'Total de alunos aprovados é: {contador}')             

