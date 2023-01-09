#Condições
n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a sua segunda nota:'))
m=(n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >=6.0:
    print('Você passou de ano!')
else:
    print('Você reprovou!')
print('Continue firme nos estudos!')
#print('você passou'if m>=6 else 'reprovado')