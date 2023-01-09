"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão"""
#Progressão aritmetica = primeiro_termo + (n-1) * razão

n=int(input('Primeiro termo:'))
r=int(input('Razão:'))
decimo=n+(11-1)*r # (10-1) quantidade de termo
for c in range(n,decimo,r):# (Inicio,Fim,pular)
    print('{}'.format(c),end='-> ')
print('Fim',end='')


