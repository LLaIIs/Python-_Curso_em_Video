"""Faça um programa que faça o computador pensar em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador
o programa deverá escrever na tela se o usuário venceu ou perdeu"""
from random import randint
from time import sleep
num =randint(0, 5)#Número aleatorio entre 0 e 5
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
n1=int(input('Em que número pensei?'))#Jogador tenta adivinhar
print('Processando...')
sleep(2)
if num == n1:
    print('Você venceu!Parabéns!')
else:
    print('Você perdeu!')
    print('Mais sorte da proxima vez')

