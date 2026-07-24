# Vários números na lista, analisando dados

numeros = []
continuar = ''

while continuar != 'N':

    numero = int(input('\nDigite um número: '))
    numeros.append(numero)

    continuar = input('\nDeseja continuar? [S/N]: ').upper().strip()

    while continuar != 'S' and continuar != 'N':
        continuar = input('\nValor Inválido...\nDeseja continuar? [S/N]: ').upper().strip()

print(f'\n{numeros}\n\nForam digitados {len(numeros)} valores.\nLista em ordem decrescente: {sorted(numeros,reverse=True)}')

if 5 in numeros:

    print('O número 5 foi encontrado nas posições: ', end='')

    for c in range(0,len(numeros)):

        if numeros[c] == 5:
            print(c+1, end= ' ')

else:
    print('O número 5 não foi encontrado na lista.')
