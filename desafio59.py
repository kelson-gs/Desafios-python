# crie um programa que leia dois valores e mostre um menu na tela:
# - [1] somar
# - [2] multiplicar
# - [3] maior
# - [4] novos números
# - [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
#/////////////////////////////////////////////////////////////////////////////
itens = (1, 2, 3, 4, 5)
it = 0
while it != 5 or it == 4:
    n1 = int(input('escolha um número: '))
    n2 = int(input('escolha mais um número: '))
    print('')

    print('''MENU DE OPÇÕES:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] trocar os números
    [5] sair do programa''')
    print('')
    it = int(input('escolha uma opção:'))
    print('')

    if it == 1:
        r = n1 + n2
        print('-=' *11)
        print('a soma dos números {} e {} são {}!'.format(n1, n2, r))
        print('-=' *11)
        it = 5

    elif it == 2:
        r = n1 * n2
        print('-=' *11)
        print('A multiplicação dos números {} e {} são {}'.format(n1, n2, r))
        print('-=' *11)
        it = 5

    elif it == 3:
        if n1 > n2:
            print('-=' *11)
            print('{} é o maior'.format(n1))
            print('-=' *11)
            it = 5

        elif n2 > n1:
            print('-=' *11)
            print('{} é o maior'.format(n2))
            print('-=' *11)
            it = 5

        elif n1 == n2:
            print('-=' *11)
            print('Os dois são do mesmo valor')
            print('-=' *11)
            it = 5
print('')
print('fim!!')