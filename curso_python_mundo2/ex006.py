"""A confederação nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade
-Até 9 anos:mirim
-Até 14 anos:infantil
-Até 19 anos:junior
-Até 20 anos:sênior
-Acima:master"""
from datetime import date
ano=int(input('Digite o seu ano de nascimento:'))
atual=date.today().year
idade=atual-ano
print('O atleta tem {} anos'.format(idade))
if idade<=9:
    print('Classificação:mirim')
elif idade<=14:
    print('Classificação:infantil')
elif idade<=19:
    print('Classificação:junior')
elif idade<=25:
    print('Classificação:sênior')
else:
    print('Classificação:master')