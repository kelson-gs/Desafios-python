# Faça um programa que leia um número de 0 e 9999 e mostre na tela cada um dos digitos separados
# ex:
#digite um número: 1834

#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
#/////////////////////////

#pedindo ao usuário para digitar um numero inteiro qualquer entre 0  e 9999;

num = int(input('Digite um número: '))

#mostrando sua unidade, dezena, centena e milhar;
print()
#print('unidade:', num1[3])
#print('dezena:', num1[2])
#print('centena:', num1[1])
#print('milhar:', num1[0])
#refazendo
#/////////////////////////////////

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))