nome = 'kelson'
cores = {'limpa':'\033[m',            #fazendo uma lista de cores dentro do programa
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('olá! muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))