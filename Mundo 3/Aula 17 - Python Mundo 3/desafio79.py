# Vários valores em uma lista, sem repetir, em ordem crescente

numeros = []
continuar = ''

while continuar != 'N':

    numero = int(input('\nDigite um número: '))

    if numero not in numeros:
        numeros.append(numero)
    
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()

    while continuar != 'S' and continuar != 'N':
        continuar = input('\nValor inválido...\nDeseja continuar? [S/N]: ').upper().strip()

print(f'\nLista de números digitados: {sorted(numeros)}\n')
