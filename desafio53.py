# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# EX:
# - APOS A SOPA
# - A SACADA DA CASA
# - A TORRE DA DERROTA
# - O LOBO AMA O BOLO
# - ANOTARAM A DATA DA MARATONA
#/////////////////////////////////////////////////////////////////////
# resposta guanabara

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palídromo!')
else:
    print('A frase Digitada não é um palídromo!')
