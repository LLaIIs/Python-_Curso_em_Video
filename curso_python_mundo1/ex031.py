"""Escreva um programa que leia a velocidade do carro. Se ele
ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite"""

vel=float(input(('Digite a velocidade do carro:')))
if vel>80 :
    print('Você ultrapassou o limite de velocidade !')
    print('Você esta multado!')
    multa=(vel-80)*7
    print('Você ultrapassou o limite com {:.0f}Km, sua multa é de R${:.2f}'.format(vel,multa))
else:
    print('Você esta no limite de velocidade!')
    print('Tenha um Bom dia, dirija com segurança')
