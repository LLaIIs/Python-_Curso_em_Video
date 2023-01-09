"""Escreva um programa para aprovar  o empréstimo bancário para a compra de
uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. Calcule o valor da prestação mensal
sabendo que ela não pode exceder 30% do salário ou então o empréstimo
negado"""
cores={'limpa':'\033[m',#lista de cores (dicionário)
       'vermelho': '\033[31m',
       'amarelo':'\033[33m',
        'preto_e_branco':'\033[7;30m'}
casa=float(input('Digite o valor da casa desejada:R$'))
sal=float(input('Digite o seu salário:R$'))
anos=int(input('Digite em quantos anos você vai pagar:'))
prest=(casa/anos)/12
val=(30/100)*sal
print('A prestação é de {:.2f}'.format(prest))
if prest>val:
    print('Emprestimo {}negado!'.format(cores['vermelho']))
else:
    print('Emprestimo {}aprovado!'.format(cores['amarelo']))