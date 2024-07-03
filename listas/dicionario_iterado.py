meus_dados = {
    "augustolopes@gmail.com":
        {"senha": 123, "email": "principal", "extra": {"ano": 2010}},
    "lopesguto@outlook.com.br": {"senha": "abc", "email": "secundario"},
    "giannattasio04@gmail.com": {"senha": "abc123", "email": "terciario"},
}

for emails in meus_dados:
    print(emails, meus_dados[emails])

# outra for de usar
for emails, valor in meus_dados.items():
    print(emails, valor)
