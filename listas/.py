# Lista comum, mais utilizada
Cores = ["Azul", "Verde", "Amarelo", "Preto"]
print(Cores)
# Liata em branco
Cores = []
print(Cores)

# List separa cada letra em um elemento
letras = list("Python")
print(letras)

# o Range faz com que crie uma lista de 0 a 9
numeros = list(range(10))
print(numeros)

carro = ["Porshe", "Cayenne", 780000, 2024, "São Paulo", True]
print(carro)

# exibe a fruta selecionado contando do 0 até o ultimo objeto
frutas = ["Uva", "Melão", "Kiwi", "Morango"]
print(frutas[1])


# indice negativo, começa a contar apartir do ultimo elemento
frutas = ["Uva", "Melão", "Kiwi", "Morango"]
print(frutas[-4])


# Matriz
matriz = [

    [2, "oi", 3],
    [[1, 2, 3, ["boa", "noite"]], 5, 8],
    [10, 8, "hi"]
]
print(matriz[1][-3][3][1])

print(matriz[-2][-1])
print(matriz[0][-1])

carros = ["Golf", "Mustang", "Jetta"]
for ordem, carro in enumerate(carros):
    print(f"{ordem}: {carro}")


# Filtro Versão 1
numeros = [4, 5, 12, 55, 13, 22, 46, 62, 88]
pares = []
for algaritmo in numeros:
    if algaritmo % 2 == 0:
        pares.append(algaritmo)
print(pares)


# Filtro versão 2
numeros = [4, 5, 12, 55, 13, 22, 46, 62, 88]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


# Alterando filtro versão 2
numeros = [4, 5, 12, 55, 13, 22, 46, 62, 88]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
