# Simulador de caixa eletrônico

dinheiro = int(input('Quer sacar quanto? R$ '))
cont_50 = cont_20 = cont_10 = cont_1 = 0


while True:
    
    while dinheiro - 50 >= 0:

        dinheiro -= 50
        cont_50 += 1

    while dinheiro - 20 >= 0:

        dinheiro -= 20
        cont_20 += 1

    while dinheiro - 10 >= 0:

        dinheiro -= 10
        cont_10 += 1

    while dinheiro - 1 >= 0:

        dinheiro -= 1
        cont_1 += 1

    break
        
print(f'\nNotas de R$ 50: {cont_50}\nNotas de R$ 20: {cont_20}\nNotas de R$ 10: {cont_10}\nMoedas de R$ 1: {cont_1}\n')
