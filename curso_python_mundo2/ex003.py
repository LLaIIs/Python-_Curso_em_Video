"""Escreva um programa que leio dois números inteiros e compare-os
, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

num1=float(input('Primeiro número:'))
num2=float(input('Segundo número:'))
if num1>num2:
    print('Primeiro número é maior')
elif num2>num1:
    print('Segundo número é maior')
else:
    print('Não existe número maior, os dois são iguais')