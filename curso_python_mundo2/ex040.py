"""Faça um programa que jpgue par ou ímpar, com o computador o jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo"""
from random import randint
print('jogo Par ou Ímpar')
win=0
while True:
    comp = randint(0,11)
    player = int(input('Digite um valor:'))
    tipo = ' '
    while tipo not in 'PpiI':
        tipo = str(input('Par ou impar?[P/I] ')).strip().upper()[0]
    total = player + comp
    print(f'Você jogou {player} e o computador {comp}. Total de {total}')
    if total % 2 == 0:
        if tipo == 'P':
            print('Você venceu!')
            win+=1
        else:
            print('Você perdeu!')
            break
    elif total % 2 == 1:
        if tipo == 'I':
            print('Você venceu!')
            win+=1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over. Você venceu {win} vezes.')