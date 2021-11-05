#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salários superiores a R$1250,00 , calcule um aumento de 10%.
#para os inferiores ou iguais, o aumento é de 15%.
#/////////////////////////////////////

sal = float(input('qual o seu salário? '))
if sal >= 1250:
    r = sal * 110 / 100
    print('você recebeu um aumento de 10%. Seu salário agora é: {}'.format(r))
else:
    r2 = sal * 115 / 100
    print('você recebeu um aumento de 15%. Seu salário agora é: {}'.format(r2))