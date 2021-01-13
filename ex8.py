#8.	Os produtos de uma loja terão um aumento de 6%. Crie um algoritmo que receba o valor do produto e mostre o seu novo preço com o aumento.
entrada=float(input("Entre com o valor do produto: R$ "))
reajuste=6/100
valorReajustado=entrada+(entrada*reajuste)
print("O valor do produto reajustado é de R$ ", valorReajustado)
