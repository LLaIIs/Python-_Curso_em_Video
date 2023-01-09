"""Melhore o jogo onde o computador vai "pensar" em um número até acertar,
mostrando no final quantos palpites foram nescessários para vencer"""

from random import randint

comp = randint(0, 10)
print('Vou pensar em um número entre 0 e 10.Tente adivinhar')
acertou=False
guess = 0
while not acertou:#Enquanto não True
     n1 = int(input('Qual é o seu palpite?'))
     guess += 1
     if n1 == comp:
        acertou = True
     else:
         if comp > n1:
             print('Mais...Tente mais uma vez')
         else:
             print('Menos...Tente mais uma vez')

print("Acertou!")
print('Foi nescessário {} palpites para acertar. Parabéns!'.format(guess))

#while comp!=n1:
