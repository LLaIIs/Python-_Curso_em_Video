"""Desenvolva um programa que pergunte a distância de uma viagem em km
Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até
200km e R$0.45 para viagens mais longas."""
km=float(input('Digite a distância de uma viagem em Km:'))
if km<=200:
    preço=km*0.50
    print('O preço da passagem é de R${:.2f}'.format(preço))
else:
    preço = km*0.45
    print('O preço da passagem é de R${:.2f}'.format(preço))


