# Decisão (if, elif, else)
idade=int(input("Digite sua idade: "))
if idade>=18:
    print("maior Idade")
else:
    print("menor Idade") 
    
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a primeira nota: "))
frequencia=float(input('Informe sua frequencia:'))
soma=(nota1+nota2)/2
if frequencia<75:
    print("Reprovado por frequencia!")
    
else:
    if soma>=7 and frequencia>=75:
        print(f"Sua nota é: {soma} aluno aprovado")
    elif soma>=5 and frequencia>=75:
        print(f"Sua nota é: {soma} você está em recuperação")
    else:
        print(f"Sua nota é: {soma}\n Reprovado por nota")
    



# # Cáculo do IMC
# peso= float(input("Digite seu peso: "))
# altura= float(input("Sua altura: "))
# imc=peso/(altura*altura)


# if imc<18.5:
#     print(f"seu IMC é: {imc:.2f}, você tem Magreza")
    
# elif 18.5<=imc<24.9:
#     print(f"seu IMC é: {imc:.2f}, está normal")
    
# elif 24.9<=imc<29.9:
#     print(f"seu imc é: {imc:.2f}, Você está com sobrepeso") 
    
# elif 29.9<=imc<39.9:
#     print(f"seu imc é: {imc:.2f}, Você está com obesidade")  
    
# else:
#     print(f"seu imc é: {imc:.2f}, Você está com obesidade grave") 

# # Cáculo do IMC
# idade= int(input("Digite sua idade: "))

# # Faixa Etaria
# if 0<=idade<12:
#     print(f"Sua idade é: {idade} ano(s), \nA categoria é: Infantil")
    
# elif 13<=idade<17:
#     print(f"Sua idade é: {idade} ano(s), \nA categoria é: Juvenil")
    
# elif 18<=idade<59:
#     print(f"Sua idade é: {idade} ano(s), \nA categoria é: Adulto") 
    
# elif idade>=60:
#     print(f"Sua idade é: {idade} ano(s), \nA categoria é: Adulto")     
    
# else:
#         print("Digite um número válido")

# Regras do Sistema
# nota= int(input("Digite uma nota: "))

# if nota>=9:
#     print(f"Sua nota é: {nota} , \nConceito A")
    
# elif 7<=nota<9:
#     print(f"Sua nota é: {nota} , \nConceito B")
    
# elif 5<=nota<7:
#     print(f"Sua nota é: {nota} , \nConceito C")
    
# else:
#     print(f"Sua nota é: {nota} , \nConceito D")