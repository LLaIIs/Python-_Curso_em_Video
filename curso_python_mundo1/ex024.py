"""Crie um programa que leio nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome """
nom=str(input('Digite o seu nome completo:')).strip()
print('O seu nome em Maiúsculo é {}'.format(nom.upper()))
print('O seu nome me minúsculo é {}'.format(nom.lower()))
print('Seu nome tem {} letras '.format(len(nom)-nom.count(' ')))#Quantidade de letras com espaço no meio - espaços
div=nom.split()
print('O seu primeiro nome tem {} letras'.format(len(div[0])))
#Nome.find(' ')


