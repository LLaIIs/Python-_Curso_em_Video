"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos dígitos separados"""
num=int(input('Digite um número:'))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print("""|Milhar|Centena|Dezena|Unidade|
|   {}  |   {}   |   {}  |   {}   |""".format(m,c,d,u))
"""print('Unidade:{}'.format(u))
print('Dezenas:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))"""