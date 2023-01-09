"""Faça um programa que leia uma frase pelo teclado e mostre
- Quantas vezes aparece a letra A
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela ultima vez
 """


frase=str(input('Digite uma frase:').strip()).lower()
print('A letra "A" aparece {} vezes '.format(frase.count('a')))
print('A letra "A" aparece na {}° posição pela primeira vez'.format(frase.find('a')+1))
print('A letra "A" "aparece na {}° posição pela ultima vez'.format(frase.rfind('a')+1))