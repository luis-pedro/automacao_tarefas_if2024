print('Digite sua idade: ')
idade = int(input())

if idade <= 12:
    print('Você é uma criança')
elif idade < 18:
    print('Você é um adolescente')
elif idade >= 18 and idade < 65:
    print('Você é um adulto')
elif idade >= 65:
    print('Você é um idoso')

idade = idade + 1
print('Sua idade ano que vem é de ', idade)