meus_dados = {
    "augustolopes@gmail.com":
        {"senha": 123, "email": "principal", "extra": {"ano": 2010}},
    "lopesguto@outlook.com.br": {"senha": "abc", "email": "secundario"},
    "giannattasio04@gmail.com": {"senha": "abc123", "email": "terciario"},
}
print(meus_dados["lopesguto@outlook.com.br"]["email"])
print(meus_dados["giannattasio04@gmail.com"]["senha"])

# exibindo um dicionario dentro do valor de outro dicionario
extra = meus_dados["augustolopes@gmail.com"]["extra"]["ano"]
print(extra)
