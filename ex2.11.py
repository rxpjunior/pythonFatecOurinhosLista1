#11 - DESAFIO: Crie um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário adivinhou o número ou não.
import random#Biblioteca para sorteio
sorteio=random.randrange(1,10,1)#Sorteio de 1 até 10 com intervalo de 1 em 1
tentativa=int(input("Tente adivinhar o numero que o computador sorteou. Se trata de um numero de 1 até 10: "))
if tentativa == sorteio:
    print("Parabéns, vc acertou!")
else:
    print("Você errou!. O numero sorteado é o ",sorteio)
