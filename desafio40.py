#crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
#/////////////////////////////////////////

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
m = (nota1 + nota2) / 2
print('-=-'*10)
print('sua média é {}'.format(m))
print('-=-'*10)
if m < 5.0:
    print('\033[31mREPROVADO\033[m')
elif m <= 6.9:
    print('\033[31mRECULPERAÇÃO\033[m')
elif m >= 7.0:
    print('\033[36mAPROVADO\033[m')

#/////////////////////////////////////////////q
# resposta guanabara

# nota1 = float(input('primeira nota: '))
# nota2 = float(input('segunda nota: '))
# média = (nota1 + nota2) / 2
# print('Tirando {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
# if 7 > média >= 5:
#   print('o aluno está em RECULPERAÇÃO.')
# elif média < 5:
#   print('o aluno está REPROVADO.')
# elif média >= 7:
#   print(print'o aluno está APROVADO')
