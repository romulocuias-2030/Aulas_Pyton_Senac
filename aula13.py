""" ---------AULA 13 COMANDO FOR-------------"""
# for contador in range(1,21):
#     print("Repetiu", contador, "vezes")
# print("Fim do programa com loops com for")
""" range(1,21): Começa no 1 e termina no 21. (1,21,2) conta em pares """ 

# i=0
# while i<20:
#    i+=1
#    print("Repetiu", i, "vezes") 
# print("Fim do programa com loops com while")

# from time import sleep
# for contador in range(1,21):
#   print("Repetiu", contador, "vezes")
#   sleep(1)
# print("Fim do programa com loops com for")

# from time import sleep
# for i in range(10,0,-1):
#     print("Repetiu", i, "vezes")
#     sleep(1)
# print("Fim do mundo")

# for c in range(1,5):
#     print(f"Informe a {c}º Nota")
    
# for i in range(1,10):
#     cont=3*i
#     print(f"3x{i}={cont}")

# num=int(input("escolha o número da Tabuada: "))
# for i in range(1,10):
#     cont=num*i
#     print(f"{num}x{i}={cont}")
    
# num=int(input("escolha o número da Tabuada: "))   
# for i in range(1, 10):
#     print(f"{num} x {i} = {num * i}") 
    
# num1=int(input("escolha o número da Tabuada: "))   
# for i in range(9, 20):
#     print(f"{i} - {num1} = {i-num1}")
 
 
""" print("TABUADA DE MULTIPLICÃO: OPÇÃO 1") 
print("TABUADA DE DIVISÃO: OPÇÃO 2") 
print("TABUADA DE SOMA: OPÇÃO 3") 
print("TABUADA DE SUBTRACÃO: OPÇÃO 4") 
opcao=int(input("Escolha uma opção:  "))
num=int(input("escolha o número da Tabuada: ")) 
# produto_cadastrado=False    
while opcao!=0:

    if opcao==1:
        print("......TABUADA DE MULTIPLICAÇÃO............")
        num=int(input("escolha o número da Tabuada: "))   
        for i in range(1, 10):
            print(f"{num} x {i} = {num * i}")   
    
# print("......TABUADA DE DIVISÃO............")
# num=int(input("escolha o número da Tabuada: "))   
# for i in range(1, 10):
#     print(f"{i} / {num} = {i // num}")  
    
    
# print("......TABUADA DE SOMA............")
# num=int(input("escolha o número da Tabuada: "))   
# for i in range(1, 10):
#     print(f"{num} + {i} = {num + i}") 
    
# print("......TABUADA DE SUBTRAÇÃO............")
# num=int(input("escolha o número da Tabuada: "))   
# for i in range(9,-1,-1):
#     print(f"{num}-{i} = {num-i}")  

# resposta=input('Deseja continuar? (S/N): ').upper().strip()[0] 
# if resposta =='S':
#         opcao=int(input("Escolha uma opção:  "))
    else:
        break       """
        
while True:
        num=int(input("escolha o número da Tabuada: ")) 
        operacao=input("escolha +, -, *, /: ") 
        
        if operacao=='+':
            print(" tabuada de adição")
            for c in range(1,11):
                print(f"{num}+{c}={num+c}")
        
        elif operacao=='-':
            print("tabuada de subtração")
            for c in range(1,10):
                print(f"{num}-{c}={num-c}") 
        elif operacao=='*':
            print("tabuada de multiplicação")
            for c in range(1,11):
             print(f"{num}*{c}={num*c}")
            
        elif operacao=='/':
            print("tabuada de Divisão")
            for c in range(1,11):
                print(f"{num}/{c}={num/c:.0f}") 
        else:
            print("Operação  com erro") 
    
        resposta=input('Deseja continuar? (S/N): ').upper().strip()[0] 
        if resposta =='S':
         opcao=int(input("Escolha uma opção:  "))
        else:
            break        