#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
#///////////////////////////////////////////////////////

import random
print('o computador escolheu um número, advinhe qual foi !!!')
num = random.randint(0 , 5)

adv = int(input('escolha um número de 0 á 5: '))
if num == adv:
    print('você venceu')
else:
    print('você perdeu')
print('O computador escolheu : {}'.format(num))
