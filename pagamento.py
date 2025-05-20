def efetuar_pagamento(dados_abastecimento):

    formas_pagamentos = ["Dinheiro", "PIX", "Cartão de Débito", "Cartão de Crédito"]

    for(i, forma_pagamento) in enumerate(formas_pagamentos):
        print(f"{i+1} - {forma_pagamento}")

    pagamento = input("Escolha a forma de pagamento")
    valor_total = dados_abastecimento["litros"] * dados_abastecimento["valor_litro"]

    if(pagamento == '1' or pagamento == '2' or pagamento == '3'):
        desconto = valor_total * 0.10
        valor_total -= desconto

    return {
        "forma_pagamento": formas_pagamentos[int(pagamento)-1],
        "valor_total": valor_total,
        "desconto": desconto
    }
