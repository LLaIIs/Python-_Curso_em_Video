"""Faça um programa que leia três números e mostre qual é o maior
e qual é o menor"""

a=float(input('Digite o primeiro número:'))
b=float(input('Digite o segundo número:'))
c=float(input('Digite o terceiro número:'))
#Verificando quem é o menor
menor=a
if b<a and b<c :
    menor= b
if c<a and c<b:
    menor=c

maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O menor valor digitado é {:.0f}'.format(menor))
print('O maior valor digitado é {:.0f}'.format(maior))


