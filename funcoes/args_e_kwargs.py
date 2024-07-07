# Args/Kwargs podem ser definidos por qualq nome desde que tenham os devidos *

def exibir_poema(data_extenso, *poema, **informacoes):
    texto = "\n".join(poema)
    meta_dados = "\n".join(
        [f"{chave.title()}: {valor}" for chave, valor in informacoes.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Domingo, Sete de Julho de 2024",
    "Poema No Meio do Caminho",

    "No meio do caminho tinha uma pedra",
    "tinha uma pedra no meio do caminho",
    "tinha uma pedra",
    "no meio do caminho tinha uma pedra.",
    "Nunca me esquecerei desse acontecimento",
    "na vida de minhas retinas tão fatigadas.",
    "Nunca me esquecerei que no meio do caminho",
    "tinha uma pedra",
    "tinha uma pedra no meio do caminho",
    "no meio do caminho tinha uma pedra",

    autor="Carlos Drummond de Andrade",
    ano=1929,
)
