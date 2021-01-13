#7.	Crie um código que converta o valor inserido pelo usuário (em reais) para a moeda do dólar. O dólar hoje está em torno de R$5,33.
entrada=float(input("Entre com o valor em Reais: "))
valorDolar=5.33
valorConvertido=valorDolar*entrada
print("O valor R$ %.2f convertido para o valor do dólar fixado em R$ %.2f é de %.2f dólares" %(entrada,valorDolar,valorConvertido))
