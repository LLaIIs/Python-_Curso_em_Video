"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores."""


cont=soma=media=menor=maior=igual=0
r='S'
while  r=='S':

    n=float(input('Digite um valor:'))
    cont+=1
    soma+=n
    if cont == 1 : # sem isso a menor vai ser sempre 0
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    r=str(input('Você quer continuar?[S/N]')).upper().strip()[0]
media=soma/cont
print('A média dos {} valores digitados é {}'.format(cont,media))

print('{} é maior'.format(maior))
print('{} é menor'.format(menor))

