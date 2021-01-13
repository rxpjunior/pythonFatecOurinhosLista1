#3.	Crie um algoritmo que receba um núero inteiro e retorne o seu antecessor e o seu sucessor.
entrada=input("Entre com um número inteiro: ")
try:
    aux1=int(entrada)
    print("O numero digitado foi %i, seu antecessor é %i e seu sucessor é %i" %(int(entrada),(int(entrada)-1),(int(entrada)+1)))
    
except:
    print("Você não entrou com um numero inteiro")
    
