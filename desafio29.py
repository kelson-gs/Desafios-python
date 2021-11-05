#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite
#///////////////////////////////////////////////////////////////////q

vel = int(input('determine o valor da velocidade de um carro: '))
calc =float(vel - 80)* 7.00

if vel > 80:
    print('você foi multado')
    print('o valor da multa foi, R${}'.format(calc))
else:
    print('velocidade ideal')
