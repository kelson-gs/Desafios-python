#crie um programa que leia um nome de uma pessoa e diga se ela tem "silva" no nome
#//////////////////////////////////////

#Pedir ao usuário que digite um nome completo;
nome = str(input('digite um nome completo: ')).strip()

#mostrar o resultado se tem ou não o nome 'silva';
print('seu nome tem Silva? {}'.format('silva' in nome.lower()))