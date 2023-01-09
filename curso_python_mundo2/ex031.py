"""Refaça o desafio , lendo o primeiro termo e a razão de uma PA (Progressão Aritmétca)
, mostrando os 10 primeiros termos da progressão usando while"""

print('Gerador de PA')
n=int(input('Primeiro termo:'))
r=int(input('Razão:'))
cont=1
f=0
while cont<=10:
    f += r
    cont+=1
    print('{}'.format(f),end='-> ')
print('Fim',end='')