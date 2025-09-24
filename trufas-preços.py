def distribuir_trufas(votos, total_trufas):
    total_votos = sum(votos.values())
    distribuicao = {sabor: round((qtd/total_votos) * total_trufas) for sabor, qtd in votos.items()}

    # Ajusta diferença por arredondamento
    diferenca = total_trufas - sum(distribuicao.values())
    sabores = list(distribuicao.keys())
    if diferenca != 0:
        distribuicao[sabores[0]] += diferenca

    return distribuicao


def calcular_preco_trufas(qtd_trufas, preco_unitario=1.70, taxa_entrega=10):
    valor_trufas = qtd_trufas * preco_unitario
    valor_total = valor_trufas + taxa_entrega
    return round(valor_total, 2)


if __name__ == "__main__":
    # votos da enquete
    votos = {
        "Ovomaltine": 14,
        "Oreo": 15,
        "Leite Ninho": 12,
        "Brigadeiro": 11,
        "Doce de Leite": 7,
        "Casadinho": 6,
        "Sonho de Valsa": 4,
        "Maracujá": 4,
        "Beijinho": 3,
        "Crocante": 3
    }

    # Entrada do usuário
    qtd = int(input("Quantas trufas você deseja comprar? "))

    # Distribuição
    distribuicao = distribuir_trufas(votos, qtd)
    print("\n📊 Distribuição proporcional:")
    for sabor, quantidade in distribuicao.items():
        print(f"- {sabor}: {quantidade}")

    # Preço
    preco = calcular_preco_trufas(qtd)
    print(f"\n💰 Valor total com entrega: R$ {preco}")
