"""Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo slário, com 15% de aumento"""

sal=float(input('Digite o seu salário atual:'))
porc=float(input('Digite a porcentagem do aumento:'))
sum=sal+((porc/100)*sal)

print('O salario de R${}, aumentou {:.0f}%, passando a totalizar R${:.2f}'.format(sal,porc,sum))
