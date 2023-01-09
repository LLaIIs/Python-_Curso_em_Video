"""Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5 % de desconto"""

prod=float(input('Digite o preço do produto :'))
desc=float(input("Digite o desconto:" ))
porc=prod-((desc/100)*prod)
print('O total com o desconto de {:.0f}% é {:.2f}'.format(desc,porc))