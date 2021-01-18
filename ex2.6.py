#6 - Faça um programa que calcule o peso ideal de uma pessoa de acordo com seu sexo e altura. Após o cálculo, print qual seria este peso ideal de acordo com os dados recebidos. Utilize as seguintes fórmulas como base, onde h é o valor da altura.
#Homens: (72,7 * h) – 58
#Mulheres: (62,1 * h) – 44,7
sexo=input("Entre com f para feminino e m para masculino: ").upper()
if sexo != "M" and sexo !="F":
    print("Genero inválido. Programa cancelado")
else:
    altura=float(input("Entre com a altura. Exemplo 1.80: "))
    if sexo == "M":
        pesoIdeal=(72.7*altura)-58
        print("O peso ideal para o senhor é: ",pesoIdeal)
    else:
        pesoIdeal=(62.1*altura)-44.7
        print("O peso ideal para a senhora é: ",pesoIdeal)
