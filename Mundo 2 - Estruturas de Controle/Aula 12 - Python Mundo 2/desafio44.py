# Calculando valor final de um produto

valor_inicial = float(input('Digite o valor inicial do produto: R$ '))
tipo_pagamento = int(input(f"""
TIPO DE PAGAMENTO:

1 - À VISTA (DINHEIRO/CARTÃO/CHEQUE)
2 - PARCELADO (CARTÃO)

ESCOLHA: """))

if tipo_pagamento == 1:

    metodo_pagamento = int(input(f"""
MÉTODO DE PAGAMENTO:

1 - DINHEIRO (10% DE DESCONTO)
2 - CARTÃO (5% DE DESCONTO)
3 - CHEQUE (10% DE DESCONTO)

ESCOLHA: """))
    
    if metodo_pagamento == 1 or metodo_pagamento == 3:
        valor_final = valor_inicial*0.9
        print(f'\nO produto terá valor final de: R$ {valor_final:.2f}\n')

    elif metodo_pagamento == 2:
        valor_final = valor_inicial*0.95
        print(f'\nO produto terá valor final de: R$ {valor_final:.2f}\n')

    else:
        print('\nValor inválido. Tente Novamente....\n')

elif tipo_pagamento == 2:

    parcelas = int(input('\nEscolha o número de parcelas: '))

    if parcelas <= 0:
        print('\nValor inválido. Tente novamente...\n')
    elif parcelas <= 2:
        print(f'\nO produto terá valor final de: R$ {valor_inicial:.2f} em {parcelas} parcelas de R$ {valor_inicial/parcelas:.2f}\n')
        # Aqui tem uma penalidade intencional pra os usuarios que escolheram a opção parcelado para um pagamento à vista (1 parcela), essa pessoa perde o desconto aplicado ao pagamento à vista no cartão
    else:
        valor_final = valor_inicial*1.2
        print(f'\nO produto terá valor final de: R$ {valor_final:.2f} em {parcelas} parcelas de R$ {valor_final/parcelas:.2f}\n')

else:
    print('\nValor inválido. Tente novamente....')
