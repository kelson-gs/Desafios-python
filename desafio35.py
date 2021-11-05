#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#/////////////////////////////////////////

r1 = float(input('dê o valor de um cm: '))
r2 = float(input('dê mais um valor de um cm: '))
r3 = float(input('dê mais um valor de um cm: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mé um triangulo\033[m')
else:
    print('\033[31mnão é um triãngulo\033[m')