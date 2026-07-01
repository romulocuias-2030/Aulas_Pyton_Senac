#segue o codigo a se fazer

class Aluno:
    pass #segue o codigo a se fazer

aluno1=Aluno()
aluno2=Aluno()

aluno1.nome="Ana"
aluno2.idade=17

print(aluno1.nome)
print(aluno2.idade)

class Aluno:
    def __init__(self,nome, idade, endereco,email,sexo):# Metodo construtor
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
        self.email=email #self é uma referencia do objeto
        self.sexo=sexo
        
    def mostrar_dados(self):# Metodo construtor
        print("Nome:",self.nome)
        print("Idade:",self.idade)
        print("Endereço:",self.endereco)
        print("Email:",self.email) #self é uma referencia do objeto
        print("Sexo:",self.sexo)     
        
aluno1=Aluno("Carlos", 18,"Rua A, 123","carlos@email.com","M")  
aluno2=Aluno("Maria", 16,"Rua B, 456","maria@email.com","F")  

print(f"Aluno1: {aluno1.nome} tem {aluno1.idade} anos, sexo: {aluno1.sexo}, mora na {aluno1.endereco} e tem o email: {aluno1.email}")
print(f"Aluno1: {aluno2.nome} tem {aluno2.idade} anos, sexo: {aluno2.sexo},mora na {aluno2.endereco} e tem o email: {aluno2.email}")     

print("________________")
aluno1.mostrar_dados()
print("________________")
aluno2.mostrar_dados()