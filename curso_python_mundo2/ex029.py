"""  Crie um programa que leia dois valores e mostre um menu na tela:
[1] +
[2] *
[3]>
[4]novos números
[5]Sair do programa
seu programa deverá realizar a operação em cada caso"""
from time import sleep
soma = 0
prod = 0
choose = 0
n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor:'))
while choose != 5 :
    print("""    [ 1 ] Soma
    [ 2 ] Multiplicação
    [ 3 ] Maior
    [ 4 ] novos números
    [ 5 ] Sair do programa
    """)
    choose = int(input('>>>>>>>Escolha a operação:'))
    if choose == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1,n2,soma))
    elif choose == 2:
        prod = n1 * n2
        print('A multiplicação entre {} * {} é {}'.format(n1,n2,prod))
    elif choose == 3:
            if n1 != n2:
                if n1 > n2:
                    print('Número {} é maior que {} '.format(n1,n2))
                else:
                    print('Número {} é maior que {}'.format(n2,n1))
            else:
                print('Os valores são iguais')
    elif choose == 4:
        n1 = float(input('Digite o primeiro valor:'))
        n2 = float(input('Digite o segundo valor:'))
    elif choose == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print('Fim do programa!')





