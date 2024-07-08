# somente por nome e nao por posicão, necessario de chave em todos
def carros(*, marca, modelo, ano, placa, motor, combustivel):
    print(f"{marca}/{modelo}/{ano}/{placa}/{motor}/{combustivel}")


carros(marca="Volkswagen", modelo="Polo", ano=2024, placa="OIE-5541",
       motor="1.6", combustivel="Flex")
# Forma Válida

carros("Volkswagen", "Polo", ano=2024, placa="OIE_215", motor="1.6",
       combustivel="Flex",)
# Forma Inválida
