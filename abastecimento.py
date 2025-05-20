def abastecer(combustiveis):
    print("Combustíveis disponíveis:")
    for i, item in enumerate(combustiveis):
        print(f"{i+1} - {item['combustivel']}")

    escolha = int(input("Qual combustível deseja abastecer? "))
    litros = float(input("Quantos litros deseja abastecer? "))

    item_escolhido = combustiveis[escolha - 1]

    return {
        "combustivel": item_escolhido["combustivel"],
        "litros": litros,
        "valor_litro": item_escolhido["valor_por_litro"]
    }
