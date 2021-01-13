#5.	Uma empresa deve aumentar em 5% os salários de todos os seus programadores. Faça um algritmo que calcule o valor do novo salário sabendo que o atual salário de um programador é de 3500$.
salario=float(input("Entre com o salario do funcionario: "))
reajuste=float(input("Entre com o percentual do reajuste: "))
salarioReajustado=salario+(salario*(reajuste/100))
print("O valor do salário reajustado é de: R$ ",salarioReajustado)
