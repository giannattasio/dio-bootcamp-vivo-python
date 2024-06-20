while True:
    numero = int(input("Por favor, informe um número:"))

    if numero == 15:
        break

    print(numero)

# Também é possivel usar o For para essa ocasião, no caso fica assim:
for numero in range(81):
    # caso eu queira pular um número especifíco, como o 14 nesse caso, \
    # seria só eu substituir o break pelo continue, \
    # que a sequencia ira ignorar o número 6
    if numero >= 6:
        break

    print(numero)

# Nesse caso estou usando o %, para que seja \
# exibido somento os números ímpares de 1 até 40
for numero in range(40):

    if numero % 2 == 0:
        continue

    print(numero, end=",")
