"""Faça um programa que leia o número qualquer e mostre o seu fatorial
Ex:
5!= 5x4x3x2 =120"""
#from math import factorial
num=int(input('Digite um número qualquer:'))
cont=num
print('Calculando {}! = '.format(num),end='')
fact=1 # 0x3=0 por isso começa com 1
while cont > 0:
    print('{} '.format(cont), end ='' )
    print('x 'if cont > 1 else '= ',end='')#5 x 4 x 3 x 2 x 1 =
    fact *= cont
    cont-=1
print('{}'.format(fact))