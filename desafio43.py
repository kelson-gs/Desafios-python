# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso.
# - Entre 18.5 e 25: peso ideal.
# - 25 até 30: sobrepeso.
# - 30 até 40: obesidade.
# - Acima de 40: Obesidade mórbida.
#/////////////////////////////////////////////

peso =float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura atual: '))

imc = peso / altura**2
print('Seu imc é de {:.2f}.'.format(imc))

if imc < 18.5:
    print('abaixo do peso!!')

elif imc <= 25:
    print('peso ideal!!!')

elif imc <= 30:
    print('sobrepeso!!!')

elif imc <= 40:
    print('obesidade!!!')

else:
    print('OBESIDADE MÓRBIDA')
