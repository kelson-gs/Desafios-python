# crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
#////////////////////////////////////q
for c in range(0, 51):
    n = c % 2
    if n == 0:
        print(c, end=' ')
print('fim')