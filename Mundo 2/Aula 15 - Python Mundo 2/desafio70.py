# Cadastro e análise simples de dados pt2

total = caros = 0
n = 1

while True:

    nome = input(f'\nDigite o nome do {n}º produto: ').upper().strip()

    preço = float(input(f'Digite o preço do {n}º produto: R$ '))

    while preço < 0:
        preço = float(f'\nValor inválido, tente novamente...\nDigite o preço do {n}º produto: R$ ')
    
    total += preço

    if preço > 1000:
        caros += 1

    if n == 1:
        nome_barato = nome
        barato = preço

    elif preço < barato:
        nome_barato = nome
        barato = preço

    continuar = input('\nDeseja continuar? [S/N] ').upper().strip()

    while continuar != 'S' and continuar != 'N':
        continuar = input('\nResposta Inválida, tente novamente...\nDeseja continuar? [S/N] ').upper().strip()
    
    if continuar == 'N':
        break

    n += 1

print(f'\nTotal gasto na compra: R$ {total:.2f}\n{caros} produtos custam mais de R$ 1000\nO produto mais barato foi o {nome_barato}, que custa R$ {barato:.2f}\n')
