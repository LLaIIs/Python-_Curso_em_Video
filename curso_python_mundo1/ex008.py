#Programa que le um numero inteiro qualquer e mostre sua tabuada
n1=int(input("Digite um número:"))
print('===============')
for n2 in range (11):
    r=n1*n2
    print("{}X{}={}".format(n1,n2,r))


