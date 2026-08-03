# Separar valores pares e impares de uma lista inicial:

numeros = []
par = []
impar = []
continuar = ''

while continuar != 'N':

    numeros.append(int(input('Digite um número: ')))

    continuar = input('\nDeseja continuar? [S/N]: ').upper().strip()

    while continuar != 'S' and continuar != 'N':
        continuar = input('\nValor Inválido...\nDeseja continuar? [S/N]: ').upper().strip()

for valor in numeros:

    if valor%2 == 0:
        par.append(valor)

    else:
        impar.append(valor)

print(f'\nLista original: {numeros}\nNúmeros pares: {par}\nNúmeros ímpares: {impar}\n')
