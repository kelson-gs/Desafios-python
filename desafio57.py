# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

dv = 'S'
while dv == 'S':
    M = dv = 'N'
    F = dv ='N'
    pessoa = str(input('qual o seu sexo? [M/F]')).upper()


    if pessoa != 'M' and pessoa != 'F':

        dv = str(input('Digito errado. Precione [S] para continuar, e [N] para parar.')).upper()
print('Sua resposta foi {}, Digito aceito!!'.format(pessoa))
