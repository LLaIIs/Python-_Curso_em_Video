"""Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$1,250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15% """
sal=float(input('Digite o seu salário:R$'))
if sal>1250:
    aum=sal+(10/100)*sal
    print('O seu salário com aumento de 10% é R${:.2f}'.format(aum))
else:
    aum=sal+(15/100)*sal
    print('O seu salário com 15% de aumento é R${:.2f}'.format(aum))
