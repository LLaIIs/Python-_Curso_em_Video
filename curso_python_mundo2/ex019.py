"""Faça um ´programa que leia um número e diga se ele é ou não um número primo"""
cont=0
n=int(input('Digite um número:'))
for c in range (1,1+n):
    if n%c==0:
        print('\033[33m',end=' ')
        cont+=1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
print('\nO número {} foi divisível {} vezes'.format(n,cont))
if cont==2:
    print('Por isso ele é primo!!')
else:
    print('Por isso não é primo!!')



