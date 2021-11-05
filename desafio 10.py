money = float(input('o quanto de dinheiro que a pessoa tem: '))
print('o dolar vale 3.27, quanto dolar ele podrá comprar?')
s = money / 3.27
print('{:.2f} / 3.27 = {:.2f}'.format(money, s))
print('mais ou menos {:.2f} dólares'.format(s))
#acrescentando para ponto flutuante( ":.2f" )