#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza
#////////////////////////////////////////////////////

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()

print('primeiro = {}'.format(dividido[0]))

print('último = {}'.format(dividido[len(dividido)-1))

