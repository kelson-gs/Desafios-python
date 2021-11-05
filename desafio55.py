# Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.
# Consertado pela resposta guanabara.
cont = 0
cont2 = 0
for c in range(1, 6):
    peso = float(input('peso da {} pessoa: '.format(c)))
    if c == 1:
        cont = peso
        cont2 = peso
    else:
        if peso > cont:
            cont = peso
        if peso < cont2:
            cont2 = peso
print('o maior peso é {}Kg, e o menor peso é {}Kg'.format(cont, cont2))