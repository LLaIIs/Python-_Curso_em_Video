"""Refaça o desafio 037 dos triângulos, acrescentado o recurso de
mostrar que tipo de triângulo será formado:
-Equilátero:todos os lados iguais
-Isósceles:dois lados iguais
-Escaleno:todos os lados diferentes"""

a=float(input('Lado a :'))
b=float(input('Lado b :'))
c=float(input('Lado c :'))

if (a<b+c) and (b<a+c) and (c<b+a):

   if a==b==c :
    print('Triângulo equilátero')
   elif a==b or b==c or c==a:
       print('Triângulo isósceles')
   else:
       print('Triângulo escaleno')
else:
    print('Não é triângulo')

