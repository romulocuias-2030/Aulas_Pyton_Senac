# idade=int(input("Digite sua Idade:"))
# renda=float(input("Digite sua renda:"))
# print("RENDA/IDADE")
# if renda >= 3000 and idade > 21:
#     print(f"Sua Idade é: {idade} anos")
#     print(f"Sua renda é de: R${renda:.2f}")
#     print("Boa tarde!")
# else:
#     print("Você não atende aos requisitos.")
    
"""     Uso do and com condição verdadeiro """
# nome=(input("Usuario:"))
# idade=int(input(f"Bem vindo(a), {nome}. \nInsira sua idade:"))
# renda_mensal=float(input(f"Só mais um passo {nome}. \n Agora, informe sua renda mensal:"))
# check_renda=idade>21 and renda_mensal>3000.00
# print()
# print(f"{nome}\n{idade} anos\n Elegível para o crédito: {check_renda}")

"""     Uso do or como pelo menos um verdadeiro """
# nome=input("Usuario:")
# nota_prova=float(input(f"Bem vindo(a), {nome}. \ninsira a nota da prova:"))
# nota_trabalho=float(input("insira a nota do trabalho: "))
# check_nota=(nota_trabalho>7) or (nota_prova>7)
# print()
# print(f"{nome}\nAprovação: {check_nota}")

#    """ Uso do not como interruptor """ 
# sistema_ativo=True
# resultado=sistema_ativo
# print(not resultado)

""" Uso de variaveis booleanas """
idade= int(input("Digite sua idade: "))
carteira=input("Possui carteira (s/n): ")
carteira=input("Possui multa (s/n): ")
carteira=True
multa=True
condicao=(idade>=18) and carteira and multa
print(condicao)
