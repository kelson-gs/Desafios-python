n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunta nota: '))
m = (n1 + n2)/2
print('a sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua média foi boa! PARABÊNS!')
else:
    print('sua média foi ruim! ESTUDE MAIS!')

