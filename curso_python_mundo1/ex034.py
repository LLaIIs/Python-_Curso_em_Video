"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto"""
from datetime import date
ano=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano==0:
    ano = date.today().year#pegar o ano atual
if ano%100!=0 and ano%4==0 or  ano%400==0:
    print('O ano {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é um ano bissexto!'.format(ano))

