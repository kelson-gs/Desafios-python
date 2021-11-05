# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares. Se o valor digitado for ímpar, desconsidere-o
#///////////////////////////////////////////////////////////////////////////////////
#Respota guanabara

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite um valor '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('você informou {} números pares e a soma foi {}'.format(cont, soma))
