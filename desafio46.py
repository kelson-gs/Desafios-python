# faça um programa que mostre na tela um contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
#////////////////////////////////////////////////////////////////////////////////////////////////////
from time import sleep

print('Se prepare para a contagem regressiva para o estouro de fogos de artifício!!!!!!!!')

for c in range(10, -1, -1):
    sleep(1)
    print(c)
sleep(1)
print('BOOOOOM!!!!!\n EEETA \nDISGRAAAAAÇAAAAA')