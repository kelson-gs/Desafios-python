from math import sqrt
c1 = float(input('digite um número para o cateto oposto 1: '))
c2 = float(input('digite um número para o cateto adjacente 2: '))
h = pow(c1, 2) + pow(c2, 2)#ou [ hi = math.hypot(c1, c2)] 'hypot = hipotenusa
r = sqrt(h)
print('o cateto oposto é {}, o cateto adjacente é {}, a hipotenusa dos catetos é: {:.2f}'.format(c1, c2, r))