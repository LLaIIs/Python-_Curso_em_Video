"""Desenvolva uma lógica  que leia o peso e altura de uma pessoa
e calcule seu IMC e mostre seu status de acordo com a tabela abaixo
-Abaixo de 18.5:abaixo do peso
-Entre 18.5 e 25:Peso ideal
-25 até 30:sobrepeso
-30 até 40:obesidade
-Acima de 40:obesidade mórbida"""
cores={'limpa':'\033[m',#lista de cores (dicionário)
       'vermelho': '\033[31m',
       'amarelo':'\033[33m',
        'verde':'\033[32m',
       'preto':'\033[30m'}

peso=float(input('Digite o seu peso:(Kg)'))
altura=float(input('Digite a sua altura:(m)'))
imc=peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc<18.5:
    print('{}Abaixo do peso!'.format(cores['vermelho']))
elif 18.5<=imc<25:
    print('{}Peso ideal'.format(cores['verde']))
elif 25<=imc<30:
    print('{}Sobrepeso!'.format(cores['amarelo']))
elif 30<=imc<40:
    print('{}Obesidade!'.format(cores['vermelho']))
elif imc>=40:
    print('{}Obesidade mórbida!'.format(cores['preto']))