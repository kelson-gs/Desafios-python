# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A";
# - Em que posição ela aparece a primeira vez;
# - Em qual posição ela apareceu a última vez;
#//////////////////////////////////////////////////////

#Pedir ao usuário digitar uma frase no teclado;
nom = str(input('Digite uma frase: ')).upper().strip()


#quantidade de vezes que aparece a letra a;
print('quantidade de vezes que aparece a letra a: {}'.format(nom.count('A')))

#posição inicial de 'a';
print('sua posição inicial: {}'.format(nom.find('A')+1))

#posição final de 'a';
print('sua posição final: {}'.format(nom.rfind('A')+1))


