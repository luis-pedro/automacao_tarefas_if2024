num = int(input('Informe o número da tabuada: '))

if num >= 0:
    for x in range (1, 11):
        res = num * x
        print(num, 'x', x, '=', res)