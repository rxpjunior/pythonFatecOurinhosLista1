#7 - Em um supermercado ao comprar 24 ou mais latas de cerveja de uma determinada marca o valor da unidade saí por apenas R$ 2,35. Caso a quantidade de latas seja inferior, o valor da unidade é de R$ 2,75. Desenvolva um algoritmo que calcule, dependendo da quantidade de latas inserida pelo usuário, qual será o valor que deverá ser pago pelas cervejas.
numLatas=int(input("Entre com o numero de latas a ser adquirido: "))
if numLatas >=24:
    precoLata=2.35
else:
    precoLata=2.75
valorTotal=numLatas*precoLata
print("O valor de %i lata(s) de cerveja é: R$ %.2f" %(numLatas,valorTotal))
    
