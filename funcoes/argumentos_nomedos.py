def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# Formas de executar
salvar_carro("Volkswagen", "Polo", 2024, "ABC-1234")
salvar_carro(marca="Volkswagen", modelo="Polo", ano=2024, placa="ABC-1234")
salvar_carro(**{
    "marca": "Volkswagen", "modelo": "Polo", "ano": 2024, "placa": "ABC-1234"})
