"""Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal"""
cores={'limpa':'\033[m',#lista de cores (dicionário)
       'vermelho': '\033[31m',
       'amarelo':'\033[33m',
        'preto_e_branco':'\033[7;30m'}
num=int(input('Digite um número inteiro:'))
print("""
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal""")
op=int(input('Escolha uma opção de conversão:'))
if op==1:
    print('{} convertido para binário é {}'.format(num,bin(num)[2:]))#bin() converte para binário
elif op==2:                                                      #[2:] para fatiar as iniciais ex:0b,0x,0o
    print('{} convertido para octal é {}'.format(num,oct(num)[2:]))#oct() converte para octal
elif op==3:
    print('{} convertido para hexadecimal é {}'.format(num,hex(num)[2:]))#hex() converte para hexadecimal
else:
    print('{}Opção invalida!'.format(cores['vermelho']))