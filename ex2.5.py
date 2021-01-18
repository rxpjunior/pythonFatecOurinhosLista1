#5 - Em um código, leia um número inteiro fornecido pelo usuário e verifique se ele é positivo ou negativo. Se ele for POSITIVO calcule a sua raiz quadrada. Se ele for NEGATIVO calcule o seu valor ao quadrado.
num=float(input("Entre com um numero: "))
if num > 0:
    print("O numero %f é positivo e sua raiz quadrada é: %f" %(num,(num**0.5)))
else:
    print("O numero %f é negativo e seu quadrado é: %f" %(num,(num*num)))
