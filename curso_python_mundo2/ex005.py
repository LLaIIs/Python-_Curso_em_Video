"""Crie um programa que leia duas notas de um aluno e calcule sua
média, mostrando uma mensagem no final, de acordo com a média
atingida:
-Média abaixo de 5.0:
REPROVADO
-Média entre 5.0 e 6.9:
RECUPERAÇÃO
-Média 7.0 ou superior:
APROVADO"""
cores={'limpa':'\033[m',#lista de cores (dicionário)
       'vermelho': '\033[31m',
       'amarelo':'\033[33m',
        'verde':'\033[32m'}
nota1=float(input('Digite a sua primeira nota:'))
nota2=float(input('Digite a sua segunda nota:'))
media=(nota1+nota2)/2
if media<5.0:
    print('{}Reprovado!'.format(cores['vermelho']))
elif media<6.9:
    print('{}Recuperação!'.format(cores['amarelo']))
else:
    print('{}Aprovado!'.format(cores['verde']))