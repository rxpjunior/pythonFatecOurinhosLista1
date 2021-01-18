#8 - Em uma empresa haverá um reajuste salarial, onde o salário do funcionário irá ter um aumento percentual de acordo com o cargo ocupado por ele. Desenvolva um algoritmo que calcule esses reajustes e mostre – os para o usuário de acordo com as normas abaixo:
#Gerente: salário = R$ 4.295,60; Reajuste: 5%
#Contador: salário = R$ 3.504,53; Reajuste: 8%
cargo=input("Entre com uma das opções abaixo:\nG para cargo de gerente\nC para cargo de contador\n").upper()
if cargo == "C":
    salario=3504.53
    salarioReajustado=salario*1.08
    print("O salario de contador foi reajustado de %.2f para %.2f" %(salario,salarioReajustado))
else:
    if cargo == "G":
        salario=4295.60
        salarioReajustado=salario*1.05
        print("O salario de gerente foi reajustado de %.2f para %.2f" %(salario,salarioReajustado))
    else:
        print("Opção de cargo inválida")
    
