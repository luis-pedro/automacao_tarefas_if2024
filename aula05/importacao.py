'''
Para utilizarmos as funções criamos em outros aquivos de código fonte devemos importa-las.
Para isso, utilizamos o comando import ou from import

Exemplo 1: Importar todas as funções do arquivo funções
'''
import funcoes

base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))

area = funcoes.calcularAreaTriangulo(10,50)
print(area)