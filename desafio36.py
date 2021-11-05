# Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
# O programa vai perguntar o 'valor da casa' , o 'salário' do comprador e em 'quantos anos' ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
#///////////////////////////////////////////////////////////////
from time import sleep

print('-=-' * 20)
print('\033[34mVamos ver se o comprador poderá ganhar um empréstimo para financiar sua casa.\033[m')
print('-=-' * 20)

valh = float(input('qual o valor da casa ? '))
sal = float(input('qual o salário do comprador? '))
ano = int(input('Em quantos anos pretende pagar? '))

ms = ano * 12     # cálculo: transformando o ano em meses.

prest = valh / ms   # cálculo da prestação.
print('')
print('valor da prestação é R${:.2f} por mês'.format(prest))
print('')
r = (sal * 70) / 100 - sal   #cálculo para descobrir os 30%
r2 = r * (-1)      #cálculo para eliminar o sinal do ' - '.
print('O valor de 30% do salário é R${}.'.format(r2))
print('')
print('\033[1;35mprocessando...\033[m')
print('')
sleep(3)

if prest > r2:
    print('O valor da prestação é maior que o valor de 30% do seu salário')
    print('\033[31mempréstimo negado!!!\033[m')
else:
    print('\033[32mempŕestimo aceito\033[m')

#///////////////////////////////////////////////////////////////////////////////////////////////////////
#resposta Guanabara

# casa = float(input('valor da casa: R$'))
# salário = float(input('salário do comprador: R$'))
# anos = int(input('quantos anos de financiamento? '))
# prestação = casa / (anos * 12)
# mínimo = salário * 30 / 100
# print('para pagar uma casa de R${:.2f} em {}anos'.format(casa, anos), end='')
# print('a prestação será de R${:.2f}'.format(prestação))
# if prestação <= mínimo:
#   print('emprestimo pode ser concedido!)
#else:
#   print('emprestimo NEGADO!')