#2 - Crie um código que calcule a média entre três notas de um aluno e apresente como resposta: se o número for maior ou igual a 6, o aluno foi APROVADO; se o resultado for menor do que 6 o aluno foi REPROVADO.
n1=float(input("Entre com a primeira nota do aluno: "))
n2=float(input("Entre com a segunda nota do aluno: "))
n3=float(input("Entre com a terceira nota do aluno: "))
somaNotas=n1+n2+n3
media=somaNotas/3
if media >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
