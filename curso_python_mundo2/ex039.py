"""Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa é interrompido quando o número
solicitado for negativo"""

num=vezes=0

while True:
    num = int(input('Quer ver a tabuada de qual valor :'))
    if num < 0:
        break
    for c in range (1,11):
        vezes=num*c
        print(f'{num} x {c} = {vezes}')
print('Programa tabuada encerrado!')