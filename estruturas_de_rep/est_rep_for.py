a = int(input("Informe um número inteiro:"))
print(a)

a *= 5
print(a)

a -= 148
print(a)

texto = input("Por favor, informe um texto:")
VOGAIS = "AEIOU"

for numero in texto:
    if numero.upper() in VOGAIS:
        print(numero, end="")

else:
    print()
