#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiúsculas;
# - o nome com todas minúsculas;
# - quantas letras ao todo (sem considerar espaços);
# - quantas letras tem o primeiro nome;
#/////////////////////////////////////]

nome = str(input('digite seu nome: ')).strip()   #pode adc o '.strip()' para modificar a saida do str;

# o nome com todas as letras maiúsculas;

print(nome.upper())
print('===================')
# o nome com todas minúsculas;

print(nome.lower())
print('===================')

# quantas letras tem ao todo ( sem considerar espaços);

len(nome)
print(nome.strip(),len(nome) - nome.count(' '))
print('===================')

# quantas letras tem o primeiro nome;


print(nome.find(' '))
