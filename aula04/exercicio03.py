'''
Exercício 3
------------------------------------------------------------------------
Crie um programa que execute repetidamente o programa do exercício 2. 
Após a apresentação do resultado o programa deve perguntar se o usuário 
deseja contiunuar a calcular, se a resposta for S (Sim) o programa deve
continuar se a resposta for N (Não) o programa deve terminar
'''

while True:
    n1 = float(input('Digite o primeiro número: '))
    op = input('Digite um operador matemático: ')
    n2 = float(input('Digite o segundo número: '))

    if op == '+':
        print(f'{n1} + {n2} = {n1 + n2}')
    elif op == '-':
        print(f'{n1} - {n2} = {n1 - n2}')
    elif op == '*':
        print(f'{n1} * {n2} = {n1 * n2}')
    elif op == '/':
        print(f'{n1} / {n2} = {n1 / n2}')
    resp = input('Deseja continuar S - (Sim) ou N (Não): ')
    if (resp == 'N'):
        break