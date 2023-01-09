#Condições aninhadas
age=int(input('Digite sua idade:'))
if age<=12:
    print('Você é uma criança!, portanto não é permitida entrada')
elif age <=17:
    print('Você é um adolescente!, portanto pode entrar só com identidade')
else:
    print('Você é um adulto!, portanto pode entrar sem indentidade')