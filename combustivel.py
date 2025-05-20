def pegar_combustivel():
    combustivel = input("Digite o nome do combustível:")
    valor_por_litro = float(input("Digite o valor por litro"))
    print("Combustível cadastrado com sucesso")
    return {
        "combustivel": combustivel,
        "valor_por_litro": valor_por_litro
    }
