"""Faça um programa que leio o nome completo de uma pessoa
 mostrando em seguida o primeiro e o último separadamente"""
nome=str(input('Digite o seu nome:').title()).strip()
n=nome.split()
print('O seu primeiro nome é {}'.format(n[0]))
#bar=nome.rfind(' ')
#print("O seu último nome é {}".format(nome[bar:]))
print('Seu último nome é {}'.format(n[len(n)-1]))