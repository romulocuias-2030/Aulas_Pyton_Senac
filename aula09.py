#  While
# contador=99
# while 0<contador<100:
#     print("repetiu", contador, "vezes")
#     contador-=1


# numero=int(input('Digite um número ou zero para encerrar:'))
# while numero!=0:
#     numero=int(input('Digite um número ou zero para encerrar:'))
# print("Fim de execução") 


# while True:
#     numero=int(input('Digite um número ou zero para encerrar:'))
#     if numero!=0:
#         continue
#     else:
#         break
    
# print("Fim de execução") 

# .upper() > transforma em maiuscula
# .strip() > retira espaços, [0] faz com entendimento por exemplo "sim". converte em "S"

# resposta="S" 
# while resposta=='S':
#     n=int(input('Digite um número: '))
#     resposta=input('Deseja continuar? (S/N): ').upper().strip()[0]
     
# print ("Fim")

# .lower() > transforma em minuscula
# .strip() > retira espaços, [0] faz com entendimento por exemplo "sim". converte em "S"
# r="sim" 
# while r=='sim':
#     num=int(input('Digite um número: '))
#     r=input('Deseja continuar? (S/N): ').lower().strip()
     
# print ("Fim de execução")


# resposta='S' 
# while resposta=='S':
#     contador=1
#     soma=0
#     while contador<5:
#         nota=float(input(f"Digite a {contador}º nota:"))
#         contador=contador+1
#         soma=soma+nota
#         media=soma/4
#         print(f"a soma das notas: {soma:.1f} a média é: {media:.1f}")
        
#         if media<=4:
#             print("reprovado")
#         elif media<=6:
#             print("em recuperação")
#         else:
#             print("Aprovado!")
            
#     resposta=input('Deseja continuar? (S/N): ').upper().strip()[0]  



while True:
    contador=1
    soma=0
    while contador<5:
        nota=float(input(f"Digite a {contador}º nota:"))
        contador=contador+1
        soma=soma+nota
    media=soma/4
    print(f"a soma das notas: {soma:.1f} a média é: {media:.1f}")
        
    if media<=4:
        print("reprovado")
    elif media<=6:
        print("em recuperação")
    else:
        print("Aprovado!")
            
    resposta=input('Deseja continuar? (S/N): ').upper().strip()[0] 
    if resposta!='S':
        break 