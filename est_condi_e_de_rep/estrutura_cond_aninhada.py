conta_comum = False
conta_universitaria = True

saldo = 2000

saque = 1999

cheque_especial = 300

if conta_comum:
    if saldo >= saque:
        print("Saque realizado!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("você não tem saldo suficiente para realizar o saque!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado!")
    else:
        print("você não tem saldo suficiente")
