# Verifica se o objeto está presente em uma sequência (é case sensitive)

curso = "curso de python"
nomes = "pedro", "augusto", "gabriel", "jonas"
frutas = ["morango", "manga", "kiwi", "pera"]
saques = [1000, 750, 250]

print("python" in curso)

print("jonas" in nomes)

print("augusto" not in nomes)

print("uva" in frutas)

print("abacaxi" not in frutas)

print(749 in saques)

print(400 not in saques)
