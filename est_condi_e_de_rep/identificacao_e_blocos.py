def sacar(valor):
    saldo = 750

    if saldo >= valor:
        print("valor sacado!")
        print("por favor retirar seu dinheiro no caixa.")
    else:
        print("saldo insuficiente")

    print("Obrigado por ser nosso cliente, tenha uma otima tarde!")


def depositar(valor):
    saldo = 500
    saldo += valor


sacar(750)
