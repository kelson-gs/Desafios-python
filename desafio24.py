# cria um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome "santo"
#///////////////////////////

#pedindo ao usuário que digite um nome de uma cidade;

nome = str(input('digite um nome de uma cidade: ')).strip()

#mostrando na tela o resultado;

print(nome[:5].upper() == 'SANTO')