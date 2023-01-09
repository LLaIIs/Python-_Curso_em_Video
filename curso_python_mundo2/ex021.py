"""Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas
pessoas ainda não atingiram a maioridade e quantas ja são maiores"""
from datetime import date
atual=date.today().year
cont=0
for pess in range(1,8):
    cont+=1
    nasc=int(input('Em que ano a {}° pessoa nasceu?'.format(cont)))
    idade=atual-nasc
    if idade>=21:
        print('Atingiu maioridade')
    else:
        print('Não atingiu maioridade')
