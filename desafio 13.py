n = float(input('salário do funcionário: '))
por = int(input('porcentagem: '))
novo = n + (n * por / 100)
s = n * por / 100
print('o salário do funcionário aumentado {}%: {}'.format(por, s))
print('O salário do funcionário almentado é: {}'.format(novo))
