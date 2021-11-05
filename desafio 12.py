pro = float(input('Preço do produto: '))
porc = int(input('porcentagem: '))
#corrigindo
novo = pro - (porc * pro / 100)
s = pro * porc / 100
print('preço do produto com desconto de {}%: R${}'.format(porc,s))
print('o preço custa agora: R${}'.format(novo))
