num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
num3 = int(input('digite o terceiro número: '))
count = 0
# verificando quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
    count = count + 1
if num3 < num1 and num3 < num2:
    menor = num3
    count = count + 1

# verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
    count = count + 1
if num3 > num1 and num3 > num2:
    maior = num3
    count = count + 1


print('menor numero é: {}'.format(menor))
print('maior número é: {}'.format(maior))
print('Quantidade de vezes que a operação é realizada: {}'.format(count))
