#4 - Crie um programa que leia dois números e informe o maior entre eles.
num1=float(input("Entre com o primeiro numero: "))
num2=float(input("Entre com o segundo numero: "))
if num1 > num2:
    print("O numero %f é maior que o numero %f" %(num1,num2))
else:
    if num1 < num2:
        print("O numero %f é maior que o numero %f" %(num2,num1))
    else:
        print("Os numeros são identicos (%f)"% num1)
