# Operações aritmeticas
# 5+2==7 Adição
# 5-2==3 Subtração
# 5*2==10 Multiplicação
# 5/2==2.5 Divisão
# 5**2==25 Potencia
# 5%2==1 Resto

# Ordem de precedência
# ()
# **
# * / // %
# + -

n1=int(input('Digite um número:'))
n2=int(input("Digite um número:"))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s,m,d),end='')
print(' ,Divisão inteira {} e potência {}'.format(di,e))
