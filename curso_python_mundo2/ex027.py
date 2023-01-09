"""Faça um programa que leia o sexo de uma pessoa mas só aceite 'm' ou 'f' caso esteja errado
 peça a digitação novamente até ter o valor correto"""
sex=str(input('Informe o seu sexo [M/F]:')).strip().upper()[0]# [0]pega somente a primeira letra
while sex not in 'FM':
    sex = str(input('Dados inválidos.Por favor informe o seu sexo [M/F]:')).strip().upper()[0]
print('Sexo {} registrado'.format(sex))