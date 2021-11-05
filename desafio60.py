# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# EX:
# 5! = 5x4x3x2x1 = 120
#///////////////////////////////////////////
# Resposta Guanabara

n = int(input('Digite um número para revelar seu fatorial: '))
cont = n
f = 1
print('calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1

print('{}'.format(f))