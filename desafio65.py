# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o menor e o maior valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# ///////////////////////////////////////////////////////////////////////////////////////////

c = 's'
soma = 0
cont = 0
m = 0
maior= 0
menor = 0
while c in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor  = n
    c = str(input('deseja continuar?[S/N]: ')).upper().strip()[0]

print('{} é a média de números digitados.'.format(m))
print('{} é o maior, e {} é o menor'.format(maior, menor))
