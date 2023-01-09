"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
mais alguns termos.  O programa encerrará quando ele disser que quer
mostrar 0 termos."""


print('Gerador de PA')
n=int(input('Primeiro termo:'))
r=int(input('Razão:'))
total=0
mais=10
cont=1
f=0
while mais != 0:
    total+=mais
    while cont <= total:
        f += r
        cont+=1
        print('{}'.format(f),end='-> ')
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print('Progressão finalizada com {} termos mostrados'.format(total))