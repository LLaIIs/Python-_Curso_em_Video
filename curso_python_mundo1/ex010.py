"""Faça um programa que leia a largura e a altura de uma parede em metros
calcule  a sua área e  a quantidade de tinta nescessária para pintá-la
sabendo que cada litro de tinta pinta uma aréa de 2m²"""
al=float(input('Digite a altura:'))
la=float(input('Digite a largura:'))
ar=al*la
print('A sua área é {}m²'.format(ar))
lil=ar/2
print('Para {} você precisara de {:.3f}l de tinta'.format(ar,lil))