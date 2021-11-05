# refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero = todos os lados iguais.
# - Isósceles = dois lados iguais.
# - Escaleno = todos os lados diferentes.
#///////////////////////////////////////////////

r1 = float(input('dê o valor de um cm: '))
r2 = float(input('dê mais um valor de um cm: '))
r3 = float(input('dê mais um valor de um cm: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('_'*20)
    print('\033[32mé um triângulo\033[m')

    if r1 == r2 == r3:
        print('é um triângulo EQUILÁTERO.')
        print('_'*20)

    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('é um triângulo ISÓSCELES.')
        print('_'*20)

    elif r1 != r2 != r3:
        print('é um triângulo ESCALENO.')
        print('_'*20)
else:
    print('\033[31mnão é um triângulo\033[m')