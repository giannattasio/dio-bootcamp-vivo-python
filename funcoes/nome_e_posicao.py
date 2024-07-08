def carros(marca, modelo, ano, /, placa, *, motor, combustivel):
    print(f"{marca}/{modelo}/{ano}/{placa}/{motor}/{combustivel}")
# objetos após o *, devem ser nomeados obrigatoriamente


carros("Volkswagen", "Polo", 2024, "OIE-5541", motor="1.6", combustivel="Flex")
# Forma válida


carros("Volkswagen", "Polo", 2024, "OIE-5541", "1.6", combustivel="Flex")
# Forma Invalida
