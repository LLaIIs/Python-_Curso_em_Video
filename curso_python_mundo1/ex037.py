"""Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não se formar um triângulo"""
a=float(input('Digite a o comprimento da primeira reta:'))
b=float(input('Digite o comprimento da segunda reta:'))
c=float(input('Digite o comprimento da terceira reta:'))

if (a<b+c) and (b<a+c) and (c<b+c):
    print('É triângulo!')
else:
    print('Não é triângulo!')
