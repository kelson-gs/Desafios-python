# Refaça o desafio51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# /////////////////////////////////////////////////
#corrigito pelo de Guanabara
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} _'.format(termo), end='')
    termo += razão
    cont += 1
print('fim')