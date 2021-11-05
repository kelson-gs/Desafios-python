# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#///////////////////////////////////////////////
from time import sleep

print('-=-' * 25)
print('\033[31mresponda a pergunta abaixo para saber se poderá servir ao exercito.\033[m')
print('-=-' * 25)

dat = int(input('digite o ano em que você nasceu: '))
r = 2018 - dat
print('')
print('\033[33mprocessando...\033[m')
sleep(3)
print('')
print('você nasceu em {} e sua idade é {}'.format(dat, r))
if r <= 16:
    print('\033[36mVocê ainda não tem idade para se alistar!\033[m')
elif r <= 18:
    print('\033[36mestá na hora de se alistar!!\033[m')
else:
    print('\033[36mjá passou da hora de se alistar!!!!!!\033[m')

#///////////////////////
#respota guanabara

# from datetime import date
# atual = date.today().year
# nasc = int(input('Ano de nascimento: '))
# idade = atual - nasc
# print(' quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
# if idade == 18:
#   print('você tem que se alistar IMEDIATAMENTE!')
# elif idade < 18:
#   saldo = 18 - idade
#   print('ainda faltam {} anos para o alistamento'.format(saldo))
#   ano = atual + saldo
#   print('seu alistamento será em {}.'.format(ano))
# elif idade > 18:
#   saldo = idade - 18
#   print('Você já deveria ter se alistado há {} anos.'.format(saldo))
#   ano = atual - saldo
#   print('seu alistamento foi em {}.'.format(ano))