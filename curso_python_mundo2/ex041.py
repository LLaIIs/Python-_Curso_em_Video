"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No
final , mostre:
A-) Quantas pessoas tem mais de 18 anos .
B-) Quantos homens foram cadastrados
C-) Quantas mulheres que tem menos de 20 anos"""
contM=contW=cont18=0


while True:
    print('='*20)
    print('Registrador...')
    print('=' * 20)
    age=int(input('Digite idade:'))
    sex=' '
    confirm=' '
    while sex not in 'MF':
       sex=str(input('Digite o sexo:[M/F]')).strip().upper()[0]
    while confirm not in 'SN':
        print('=' * 20)
        confirm=str(input('Você quer continuar?[S/N]')).strip().upper()[0]
    if sex == 'M':
        contM+=1
        # homens cadastrados
    if sex == 'F' and age < 20:
        contW+=1
        # Mulheres com menos de 20 anos
    if age > 18:
        cont18+=1
        # Pessoas com mais de 18 anos
    if confirm == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Total de homens cadastrados: {contM}')
print(f'Total de mulheres com menos de 20 anos: {contW}')