"""Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa"""
from math import hypot

#Teorema de pitágoras c²=a²+b²
co=float(input('Comprimento do cateto oposto:'))
ca=float(input('Comprimento do cateto adjacente:'))
#hipo=(co**2 + ca **2)**(1/2)
hipo=hypot(co,ca)
print('A hipotenusa é {:.2f}'.format(hipo))