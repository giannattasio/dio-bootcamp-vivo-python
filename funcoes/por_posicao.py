# Opcional nomear os objetos que estão da virgula ou por posicao
def carros(marca, modelo, ano, /, placa, motor, combustivel):
    print(f"{marca}/{modelo}/{ano}/{placa}/{motor}/{combustivel}")


carros("Volkswagen", "Polo", 2024, placa="OIE-5541",
       motor="1.6", combustivel="Flex")
