""" Crie um programa que leia vários números inteiros pelo teclado
. O programa só vai parar quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)."""

n=soma=0 # todos recebem 0
cont=1
n=int(input('Digite {}° valor [999 para parar]:'.format(cont))) #desconsidera 999
while n != 999: #999 condição de parada
    soma += n
    cont+=1
    n=int(input('Digite {}° valor [999 para parar]:'.format(cont)))

print('A soma dos {} valores é {}'.format(cont-1,soma))
