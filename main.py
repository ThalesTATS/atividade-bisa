from combustivel import pegar_combustivel
from abastecimento import abastecer
from pagamento import efetuar_pagamento

combustiveis = []

def saida_esperada(abastecimento, pagamento):
    print('--- Registro de Abastecimento ---')
    print('Tipo de Combustível:', abastecimento['combustivel'])
    print('Valor por litro:', abastecimento['valor_litro'])
    print('Quantidade:', abastecimento['litros'], 'litros')
    print('Forma de pagamento:', pagamento['forma_pagamento'])
    print('Desconto aplicado:', pagamento['desconto'])
    print('Total a pagar:', pagamento['valor_total'])


while(True):
    print("1 - Cadastrar tipo de Combustível")
    print("2 - Abastecer")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    if(opcao == "1"):
        combustiveis.append(pegar_combustivel())
    elif(opcao == "2"):
        abastecimento = abastecer(combustiveis)
        pagamento = efetuar_pagamento(abastecimento)
        saida_esperada(abastecimento, pagamento)
    elif(opcao == "3"):
        break
        
        