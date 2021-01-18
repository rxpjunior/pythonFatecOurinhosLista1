# 3 - Desenvolva um código que receba um valor inserido pelo usuário e retorne se esse número é PAR ou ÍMPAR.
num=float(input("Entre com um numero: "))
if num % 2 == 0:
    print("O numero %f é par!" % num)
else:
       print("O numero %f é impar!" % num)
