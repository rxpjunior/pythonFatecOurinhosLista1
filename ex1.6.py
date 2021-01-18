#6.	Crie um código que faça o cálculo da hipotenusa de um triângulo retângulo, recebendo os valores do cateto adjacente e cateto oposto.
# hipotenusa ao quadrado = soma dos dos quadrados dos catetos
catAdjacente=float(input("Entre com o valor do cateto adjacente: "))
catOposto=float(input("Entre com o valor do cateto oposto: "))
aux=(catAdjacente**2)+(catOposto**2)
hipotenusa=aux**0.5
print("A hipotenusa do triangulo é: ",hipotenusa)
