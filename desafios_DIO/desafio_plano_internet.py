def recomendar_plano(consumo_mensal):
    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps"
    elif consumo_mensal > 20:
        return "Plano Premium Fibra - 300Mbps"
    elif consumo_mensal > 40:
        return "Plano Mensal Titanium - 600Mbps"


consumo_usuario = float(input())
plano_recomendado = recomendar_plano(consumo_usuario)
print(plano_recomendado)
