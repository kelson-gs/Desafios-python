# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
#//////////////////////////////////////////////////////////////
from time import sleep
print('===========TABUADA============')
while True:
    n = int(input('Digite um número para mostrar sua tabuada!: '))
    sleep(1)
    if n <= -0:
        break

    for c in range(0, 11):
        t = n * c
        print(f'{n} x {c} = {t}')
    print('~'* 20)
    sleep(1)

print('Tabuada interrompida!!')
sleep(2)
print('desligando programa...')
sleep(1)
print('em')
for t in range(3, 0, -1):
    sleep(1)
    print(t)