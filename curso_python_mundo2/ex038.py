"""Crie um programa que leia vários números inteiros pelo teclado. O programa
 vai parar quando o usuário digitar o valor 999, que é a condição de parada. No
 final, mostre quantos números forma digitados e qual foi a soma entre eles
 (desconsiderando o flag)"""
n=soma=cont=0

while True:
    n=int(input('Digite um número inteiro:'))
    if n == 999:
        break
    cont+=1
    soma+=n
print(f'A soma dos {cont} valores digitados é {soma}')