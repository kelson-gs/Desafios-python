import math
ang = int(input('Digite um valor de um ângulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('O seno do ângulo {} é : {:.2f} \n O cosseno do ângulo {} é : {:.2f} \n O tangente do ângulo {} é : {:.2f}'.format(ang, s, ang, c, ang, t))
#############

#faltou a transformação do 'radians'
#math.sin(math.radians(x))
