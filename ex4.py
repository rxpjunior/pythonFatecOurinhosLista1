#4.	Um dono de um clube precisa cercar o campo de futebol society com uma tela de aço. O campo mede 30m de largura por 50m de comprimento. Sabendo que cada metro de tela custa R$ 26,00, desenvolva um programa que calcule quanto de tela de aço será necessária para cercar o campo e quanto custará.
largura=float(input("Entre com a largura do terreno: "))
comprimento=float(input("Entre com a comprimento do terreno: "))
valorMetroTela=float(input("Entre com o valor do metro da tela: "))
perimetro=comprimento+largura
custoTotal=perimetro*valorMetroTela
print("Para fechar um terreno de %.2f metros de largura por %.2f metros de comprimento o valor será de R$ %.2f" %(largura,comprimento,custoTotal))
