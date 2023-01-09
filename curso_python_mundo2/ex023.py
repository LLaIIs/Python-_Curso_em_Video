"""Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final do programa
mostre:
-A média de idade do grupo
-Qual é o nome do homem mais velho
-Quantas mulheres têm menos de 20 anos"""
soma_age=0
maismen=0
name=0
totmulher20=0
for p in range(1,5):
    print('------{}ª PESSOA--------'.format(p))
    Nome=str(input('Nome:')).strip()
    idade=int(input('Idade:'))
    sexo=str(input('[M/F]:')).strip()
    soma_age+= idade
    if p==1 and sexo in 'Mm':
        maismen=idade
        name=Nome

    if sexo in 'Mm' and idade>maismen :
            maismen=idade
            name=Nome
    if sexo in 'Ff' and idade<20:
        totmulher20+=1
print('A média de idade do grupo é {} anos'.format(int(soma_age/p)))
print('O nome do homen mais velho é {}'.format(name))
print('Tem {} mulheres com menos de 20 anos'.format(totmulher20))