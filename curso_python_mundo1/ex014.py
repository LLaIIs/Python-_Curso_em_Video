"""Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado"""

km = float(input('Digite a quantidade de Km percorridos:'))
dias = int(input('Digite a quantidade de dias que foi alugado:'))
pagar = (60*dias)+(0.15*km)

print('O total a pagar é de R${:.2f}'.format(pagar))

print('O total a pagar pe de R${:.2f}'.format(pagar))

