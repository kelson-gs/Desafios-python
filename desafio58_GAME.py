# melhore o jogo do desafio28 onde o computador vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
#//////////////////////////////////////////////////////////////////////
from random import randint
from time import sleep

computador = randint(0, 10)
print('=================JOGO DA ADVINHAÇÃO===============')
print('-=' *20)
print('\033[33mvou pensar em um número entre 0 e 10. Tente advinhar...\033[m')
print('-=' *20)

cont = 0
r = 'S'
print('')
jogador = int(input('Em que número eu pensei? '))
print('')
sleep(2)

if jogador != computador:
    print('')
    print('\033[31mvocê errou!\033[m')

while jogador != computador and r == 'S':
    l = int(input('Tente mais uma vez:'))
    cont += 1
    sleep(2)

    if l != computador:
        r = str(input('\033[31mvocê errou de novo, desja continuar ?\033[m [S/N]')).upper()

    elif l == computador:
            l = r = 'N'
            print('')
            print('\033[32mparabéns, acertou!!\033[m')

print('você teve {} tentativas'.format(cont))
print('Adeus, obrigado por jogar comigo!!')

#=========================================================================================================================================================
# resposta Guanabara:

# from random import randint
# computador = randint(0, 10)
# print('Sou seu computador... Acabei de pensar em um número entre 0 e 10!')
# print('será que você consegue advinhar qual foi ?')
# acertou = false
# palpites = 0
# while not acertou:
#        jogado = int(input('Qual é seu palpite? '))
#        palpites += 1
#        if jogador == computador:
#            acertou = True
#        else:
#            if jogador < computador:
#                print('Mais... Tente mais uma vez.')
#            elif jogador > computador:
#                print('Menos... Tente mais uma vez')
# print('Acertou com {} tentativas. Parabéns!'.format(palpites))





