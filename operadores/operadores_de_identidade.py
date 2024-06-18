curso = "curso de python"
nome_do_curso = curso
saldo, limite = 400, 400

#  Compara se os objetos testados fazem parte da mesma posição na memória

print(curso is nome_do_curso)

print(curso is saldo)

print(curso is not nome_do_curso)

print(saldo is not curso)

print(saldo is limite)

# Se as variaveis apontarem para o mesmo objeto, inverte a condição booleana,
# o que era False vira True, e o que era True, vira False
