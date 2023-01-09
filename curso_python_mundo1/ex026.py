"""Crie um programa que leia o nome pessoa e diga se ela tem
 "silva " no nome """
nom=str(input('Qual o seu nome completo?')).title()
ol='Silva' in nom#procurar uma string dentro de outra
print('Seu nome tem Silva ? {}'.format(ol))
