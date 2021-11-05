# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o úsuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
n = 0
soma = 0
cont = 0
n = int(input('Digite um número inteiro de 0 a 999(para parar digite 999): '))
while n != 999:

    soma += n
    cont += 1
    n = int(input('Digite um número inteiro [999 para parar]: '))
print('')
print('você digitou {} número(s). A soma destes foram {}.'.format(cont, soma))