"""Crie um programa que faça o computador jogar jokenpô com você"""

from random import randint
from time import sleep
itens=('Pedra','Papel','Tesoura')
comp=randint(0,2)
print('0 computador escolheu {}'.format(itens[comp]))
print(""" Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
jog=int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*10)
print('O computador jogou {}'.format(itens[comp]))
print('O jogador jogou {}'.format(itens[jog]))
print('-='*10)
if comp==0:
    if jog==0:
        print('Empate')
    elif jog==1:
        print('Jogador vence')
    elif jog==2:
        print('Jogador perde')
    else:
        print('Jogada inválida!')
elif comp==1:
    if jog == 0:
        print('Jogador perde')
    elif jog == 1:
        print('Empate')
    elif jog == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida!')
elif comp==2:
    if jog == 0:
        print('Jogador vence')
    elif jog == 1:
        print('Jogador perde')
    elif jog == 2:
        print('Empate')
    else:
        print('Jogada inválida!')

