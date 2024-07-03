# Formas de criar um dicionario
Carro = {"Marca": "Porshe", "Valor": 1000000}
Roupas = dict(Marca="Nike", Valor=150)

print(Carro)
print(Roupas)

# Adicionando nova chave ao dicionario
Carro["contato"] = "11952489512"
print(Carro)

# Consultando objeto especifico
print(Carro["Valor"])

# Substitundo algo no dicionario
Roupas["Valor"] = 200
print(Roupas)
