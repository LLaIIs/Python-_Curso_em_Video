"""
Programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar
considere us$1,00=R$3,27
"""

n1=float(input('Digite quanto dinheiro você tem na carteira: R$'))
dol=n1/5.27
print('Com {} você pode comprar US${:.2f} '.format(n1,dol) )

