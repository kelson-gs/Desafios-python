# Melhore o desafio61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
# //////////////////////////////////////////////////////////////////////////////////////////
print('Gerador de PA')
print('-='*10)
primeiro = int(input('primeiro termo: '))
razão = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}_'.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos você quer mostrar a mais?: '))
print('progressão finalizada com {} termos mostrados.'.format(total))