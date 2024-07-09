def subtrair(a, b):
    return a - b


def multip(a, b):
    return a*2, b*4


def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado é igual a {resultado}")


exibir_resultado(5, 10, subtrair)
exibir_resultado(10, 4, multip)
exibir_resultado(215, 175, somar)

# Outra forma de colocar em primeira classe
# Se desejado mudar a operação só trocar o nome pós o =(Ex: subtrair por somar)
operacao = subtrair
print(operacao(5, 17))
