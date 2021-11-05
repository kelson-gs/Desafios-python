# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
# EX:
# 0 - 1 - 1 - 2 - 3 - 5 - 8
#//////////////////////////////////////////////////////////////////////////////////
valor = int(input('digite um valor: '))
a, b = 0, 1      #dando o valor de 'a' e 'b'
while b < valor:    # enquanto o valor de b for menor que o 'valor'
    print(b,'', end='')
    a, b = b, a+b   #'a' e 'b'recebe 'b', 'a' mais 'b'/ '0,1' recebe '1, 0+1'
print('\nfibonacci')
#////////////////////////////////////////////////////////////////////////////////////
# Resposta Guanabara
print('-' * 30)
print('sequência de fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('~' * 30)
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('- {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('- fim')
print('~' * 30)