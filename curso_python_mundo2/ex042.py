"""Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não.
 No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
soma=contP=cont=cheap=0
prodC=' '
while True:
    prod=str(input('Digite o nome do produto:'))
    price=float(input('Valor do produto:R$'))
    cont+=1
    soma+=price # Qual é o total gasto na compra
    confirm = ' '
    if cont == 1 or price < cheap:
        cheap = price
        prodC = prod
        # Qual é o nome do produto mais barato
    while confirm not in 'SN':
        confirm=str(input('Você vai continuar?[S/N]')).strip().upper()[0]
    if price > 1000:
        contP+=1
        # Quantos produtos custam mais de R$1000
    if confirm == 'N':
        break
print(f'O total gasto na compra é de R${soma}')
print(f'Temos {contP} produto custando mais de R$1000.00')
print(f'O nome do produto mais barato é {prodC} que custa {cheap}')