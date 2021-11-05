import random #ou \ from random import choice

print('nome selecionado para apagar o quadro:')
al1 = input('digite um nome: ')
al2 = input('digite mais um nome: ')
al3 = input('digite mais um nome: ')
al4 = input('digite mais um nome: ')
n = [al1, al2, al3, al4]
alr = random.choice(n)#e apagar o random.
print('a pessoa é:', alr)

