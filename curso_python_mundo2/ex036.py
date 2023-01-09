#Interrompendo reptições while
n=s=0
while True: # Loop infinito
    n= int(input('Digite um número:'))
    if n == 999:
        break # Parar
    s+=n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # fstrings (novo jeito de usar o format)
