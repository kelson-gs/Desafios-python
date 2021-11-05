# Faça um programa que jogue par ou ímpar com o computador.
# O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final.
#///////////////////////////////////////////////////////////////////////////////////////////////////
from random import randint

soma = cont = par= 0
impar = 1

while True:
    comp = randint(0, 11)
    jogador = int(input('escolha um número: '))
    r = jogador + comp

    ip = str(input('Escolha [ímpa/par]: ' ))

    print(f'o computador escolheu: {comp}')
    print(f'a soma de {jogador} + {comp} = {r}')

    if r % 2 == 0:
        print('par')
        if ip == par:
            print('venceu')
        else:
            print('perdeu')
            break
    else:
        print('impar')
        if ip == impar:
            print('perdeu')
            break
        else:
            print('venceu')


print('Terminou')