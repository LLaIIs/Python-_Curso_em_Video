"""Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com a sua idade:
-Se ele ainda vai se alitar no serviço militar
-Se é hora de se alistar
-Se ja passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou
do prazo.
"""
from datetime import date
cores={'limpa':'\033[m',#lista de cores (dicionário)
       'vermelho': '\033[31m',
       'amarelo':'\033[33m',
        'verde':'\033[32m'}
atual=date.today().year
nasc=int(input('Digite seu ano de nascimento:'))
idade=atual-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade==18:
    print('Você tem que se alistar {}imediatamente!'.format(cores['vermelho']))

elif idade<18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual+saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo=idade-18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano=atual-saldo
    print('Seu alistamento foi em {}'.format(ano))

