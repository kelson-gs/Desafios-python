# A confederação NAcional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
# - até 9 anos; mirim
# - até 14 anos; infantil
# - até 19 anos; junior
# - até 20 anos; Sênior
# - acima; master
#///////////////////////////////////////////////////////
from time import sleep


print('\033[1;34mA Confederação Nacional de Natação irá determinar qual categoria pertence!!\033[m')
print('-'*20)
idade = int(input('Por favor, indique sua idade: '))
print('\033[1mprocessando...\033[m')
sleep(2)

if idade <= 9:
    print('_'*20)
    print('')
    print('Sua categoria é: \033[33mMIRIM\033[m !!!!')
    print('_'*20)

elif idade <= 14:
    print('_'*20)
    print('')
    print('Sua categoria é: \033[33mINFANTIL\033[m !!!!')
    print('_'*20)

elif idade <= 19:
    print('_'*20)
    print('')
    print('Sua categoria é: \033[32mJUNIOR\033[m !!!')
    print('_'*20)

elif idade <= 25:
    print('_'*20)
    print('')
    print('Sua categoria é: \033[35mSÊNIOR\033[m !!!')
    print('_'*20)

else:
    print('_'*20)
    print('')
    print('Sua categoria é: \033[31mMASTER\033[m !!!!')
    print('_'*20)