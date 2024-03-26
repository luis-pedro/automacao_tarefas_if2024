conc = int(input('Informe a concentração do princípio ativo do remédio (mg/ml): '))
peso = float(input('Informe o peso da criança: '))
dose = int(input('Informe a dose recomendada (mg por kg): '))

resultado = (peso * dose / conc) * 20

print(resultado)