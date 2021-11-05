# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - á vista = dinheiro / cheque: 10% de desconto.
# - á vista no cartão: 5% de desconto.
# - em até 2x no cartão: preço normal.
# - 3x ou mais no cartão: 20% de juros.
#////////////////////////////////////////////////////////////////////////////////////

produto = float(input('qual o valor do produto a ser pago ?: '))
print('Entendido. O valor do produto é {}'.format(produto))

pay = str(input('como pretende pagar ? a dinheiro, a cheque ou cartão ?: '))
print('entendido. você pretende pagar a {}'.format(pay))

din = 'dinheiro'
ch = 'cheque'
card = 'cartão'
a = 'á vista'
b = 'dividido'

if pay == din or pay == ch:
    R = (produto * 90) / 100
    print('você ganhou um desconto de 10%. O valor cairá de R${} para R${}.'.format(produto, R))

else:
    n = str(input('como pretende usar o cartão? dividido ou á vista?: '))

    if n == a:

        R2 = (produto * 95) / 100
        print('Você ganhou 5% de desconto no cartão. O valor de R${} cairá para R${}.'.format(produto, R2))

    else:
        n2 = int(input('quantas vezes quer dividir ?: '))

        if n2 == 2:
            r3 = produto / 2
            print('O preço será normal, dividido em {} meses em R${}'.format(n2, r3))

        elif n2 >= 3:
            R4 = (produto * 120) / 100
            R5 = R4 / n2
            print('Tem um acréscimo de juros de 20%. O valor R${} vai para R${} e será R${} dividido a {} meses'.format(produto, R4, R5, n2))

