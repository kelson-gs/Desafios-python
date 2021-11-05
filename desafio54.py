# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#//////////////////////////////////////////////////////////////////////
from datetime import date
atual = date.today().year
soma = 0
cont = 0
soma2 = 0
cont2 = 0
for c in range(1, 8):
    data = int(input('{} - Qual o ano de seu nascimento?: '.format(c)))
    idade = atual - data
    if idade < 21:
        soma += data
        cont += 1
    if idade >= 21:
        soma2 += data
        cont2 += 1
print('{} são menores de idade, e {} são maiores de idade!!'.format(cont, cont2,))

