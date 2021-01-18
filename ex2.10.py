#10 - Crie um código que receba os valores de três retas e diga para o usuário se essas retas podem ou não formar um triângulo.
#Para que três retas possam formar um triângulo, o comprimento de um lado não pode ser maior que a soma dos outros dois segmentos do triângulo. Ex: O lado 1 têm que ser menor que a soma do lado 2 e lado 3.
lado1=float(input("Entre com o valor da primeira reta: "))
lado2=float(input("Entre com o valor da segunda reta: "))
lado3=float(input("Entre com o valor da terceira reta: "))
if lado1 <= (lado2+lado3) and lado2 <= (lado1+lado3) and lado3 <=(lado2+lado1):
    print("Com os valores informados É possivel formar um triangulo")
else:
    print("Com os valores informados NÃO É possivel formar um triangulo")
