# for numero in range(10):
#     if numero == 5:
#         break
#     print(numero)
    
# print('********')

""" for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)
    
print('********')

for numero in range(10):
    if numero % 2 == 0:
        print(numero)
     """
# print('********')

""" # for numero in range(10):
#     if numero == 5:
#         pass """ #  Pass >> passa direto e ignora até eu decidir como irei escrever depois a linha de código
#     print(numero) 

""" print("Alo" """ #SyntaxError: '(' was never closed
# Try >> Fazer isso...
# Except >> se não isso...

# try:
#     print(10/0)
# except:    
#     print("Ocorreu um Erro!") 

# try:
#     numero = int (input("Digite um numero: "))
#     resultado = 10 / numero
#     print(resultado)
# except:    
#     print("Ocorreu um Erro!") 

""" try:
    numero = int (input("Digite um numero: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:    
    print("Você digitou algo invalido!") # Não reconhece a string ou real, somente inteiros
except ZeroDivisionError:    
    print("Erro de divisão por zero!") # Não há divisão por zero """
    
""" try:
    # codigo de erro
    x = int("abc")
except Exception as e:    
    print("!Ocorreu um Erro!", e) """


""" lista = [1,2,3]    
try:
    # index error
        print(lista[5])
except IndexError:    
    print("!Indice fora do intervalo!")     """
    
    
""" try:
    # type error
        soma = "Texto" + 10
except TypeError:    
    print("!Tipos incompativeis de soma!")  """  

""" dados = {'Nome':'Ana'}    
try:
    # key error
        print(dados["idade"]) # Chave inexistente
except KeyError:    
    print("!Chave inexistente!")    """    
    
    
try:
     # Entrada de dados
     num1 = float(input("Digite o primeiro número: "))       
     num2 = float(input("Digite o segundo número: "))  
     # operação
     resultado = num1 / num2      
except ValueError:
     print("Erro: Você deve digitar apenas números válidos")
except ZeroDivisionError:
     print("Erro: Não é possível dividir por zero")
else:
     # Executa somente se não houver erro
     print(f"O resultado da divisão é: {resultado}") 
finally:
     #Sempre executa
     print("programa finalizado!")         
        