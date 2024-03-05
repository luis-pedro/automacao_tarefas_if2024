'''
Exercício 2
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Crie um programa que recebe 2 números reais como entrada e um operador matemático.
De acordo com o operador matemático fornecido o programa deve calcular e apresentar 
o resultado da operação

Exemplo de entrada
1.2
2.3
+

Exemplo saída
O resultado da soma é 3.5
'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
op = input('Digite um operador matemático: ')

if op == '+':
    print(f'{n1} + {n2} = {n1 + n2}')
elif op == '-':
    print(f'{n1} - {n2} = {n1 - n2}')
elif op == '*':
    print(f'{n1} * {n2} = {n1 * n2}')
elif op == '/':
    print(f'{n1} / {n2} = {n1 / n2}')