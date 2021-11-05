# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
#/////////////////////////////////////////////////////////
# resposta Guanabara
num = int(input('Escolha um número inteiro qualquer:'))
print('escolha uma base para conversão:')
print('[ 1 ] converter para binário')
print('[ 2 ] converter para octal')
print('[ 3 ] converter para hexadecimal')
opção = int(input('sua opção: '))
if opção == 1:
   print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
   print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
   print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
   print('opção inválida. Tente novamente!')

