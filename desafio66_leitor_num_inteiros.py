# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No dinal, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).
#//////////////////////////////////////////////////////////////////////////////////////////////
cont = soma = 0
print('digite:999 para finalizar o programa.')
while True:
    n = int(input('Digite um número: '))

    if n == 999:
        break

    soma += n
    cont += 1
print(f'Foram digitados {cont} números')
print(f'A soma dos números são {soma}')