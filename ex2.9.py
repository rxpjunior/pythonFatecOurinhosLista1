#9 -Crie um código que receba um ano e informe para o usuário se este ano é bissexto ou não. Para um ano ser bissexto ele deve ser divisível por 400 ou se o ano for divisível por 4 e não divisível por 100.
ano=int(input("Entre com um ano paradeterminar se é bissexto: "))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 !=0:
    print("O ano %i é bissexto" %ano)
else:
     print("O ano %i não é bissexto" %ano)
