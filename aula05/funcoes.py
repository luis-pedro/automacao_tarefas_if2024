'''
As funções são utilizadas para modulizar o código, ou seja. dividi-lo em partes menores, que podem ser reutilizadas.

Estrutura:

def nome_funcao(param1, param2):
    faz algo
    return valor

Exemplos:
'''

#funçao01
def calcularAreaTriangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado

#função02
def login (usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True
    else:
        return False
    
#chamar a função
#print(login("ivan", "123"))
    
#area = calcularAreaTriangulo(100, 50)
#print('A área do triângulo é: ', area)