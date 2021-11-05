# refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
#/////////////////////////
num = int(input('escolha um número para realizar a tabuada: '))
print('-=' *11)
print('TABUADA DE DELON')
print('-=' *11)
for c in range(0, 11):
    n = num * c
    print('{} x {} = {}'.format(num, c, n))
print('fim')