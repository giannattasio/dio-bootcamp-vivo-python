# exemplo utilizando um iterável
for numero in range(16):
    print(numero, end=",")
# o end="", exibe os numeros de forma horizontal

# exemplo c função built-in range
for conta in range(0, 20, 4):
    print(conta)
# O step é colocado no final,
# nesse caso sinalizando a tabuada do 4,
# sendo o limite até o numero 20
for tabuada in range(1, 120, 6):
    print(tabuada, end=" , ")
