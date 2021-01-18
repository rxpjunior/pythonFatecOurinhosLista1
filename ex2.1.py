#1 - Crie um algoritmo que leia a velocidade em Km/h que um veículo passou em uma rodovia e informe se ele será multado ou não. Se a velocidade exceder 90 Km/h, o motorista deve ser MULTADO, se não, exiba uma mensagem de boa viagem.
velocidade=float(input("Entre com a velocidade do veículo: "))
if velocidade > 90:
    print("Motorista multado!")
else:
    print("Boa viagem!")
