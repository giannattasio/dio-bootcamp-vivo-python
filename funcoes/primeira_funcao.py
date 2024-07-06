def exibir_mensagem():
    print("Boa tarde!")


def mensagem(nome):
    print(f"Boa tarde {nome}!")


def mensagem_1(nome="Augusto"):
    print(f"Seja bem vindo {nome}!")

# quando não é informado um valor acima, é preciso informar na hora de exibir


exibir_mensagem()
mensagem("Guto")
# consigo alterar o valor definido em cima definindo na hora de exibir
mensagem_1("Giannattasio")
