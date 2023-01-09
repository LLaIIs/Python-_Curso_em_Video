""" Escreva um programa que leia um número N inteiro qualquer e mostre
 na tela os N primeiros elementos de uma Sequência de Fibonacci.
 Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8"""


termo=int(input('Quantos termos você quer mostrar?'))
#Começa com 3 pois ja leu 3 termos antes do while
t1=0
t2=1
t3=0
cont=3
print('{} ->{}'.format(t1,t2),end='')
while termo >= cont:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ->Fim')