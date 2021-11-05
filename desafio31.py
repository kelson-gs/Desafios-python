#Desenvolva um programa que pergunte a distância de uma viagem em Km. calcule o preço da passagem, cobrando R$0,50 opor km para viagens de até 200km e R$0,45 para viagens mais longas.



dis = float(input('determine uma distância: '))
if dis <= 200:
    val = dis * 0.50
    print('valor da passagem será: {:>2}'.format(val))
else:
    val2 = dis * 0.45
    print('valor da passagem será: {:>2}'.format(val2))