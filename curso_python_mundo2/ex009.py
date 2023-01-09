"""Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento:
-á vista dinheiro/cheque:desconto de 10%
-á vista no cartão:5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão:20% de juros"""
cores={'limpa':'\033[m',#lista de cores (dicionário)
       'vermelho': '\033[31m',
       'amarelo':'\033[33m',
        'verde':'\033[32m',
       'preto':'\033[30m'}
preço=float(input('Digite o preço das compras:R$'))
print('FORMAS DE PAGAMENTO')
print("""
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
op=int(input('Digite a opção:'))

if op==1:
    desc=preço-(10/100)*preço

elif op==2:
    desc=preço-(5/100)*preço

elif op==3:
    desc=preço
    parc=desc/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parc))

elif op==4:
    desc=preço+((20/100)*preço)
    totparc=int(input('Quantas parcelas?'))
    parc=desc/totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc,parc))
else:
    desc=preço
    print('{}opção invalida!'.format(cores['vermelho']))

print('Sua compra de R${}, vai custar R${:.2f} no final'.format(preço,desc))