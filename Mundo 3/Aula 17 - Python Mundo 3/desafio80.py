# Organizando 5 números em ordem crescente, de forma manual

numeros = []

for c in range(1, 6):

    numero = int(input(f'Digite o {c}º número: '))

    if c == 1:
        numeros.append(numero)

    elif numero <= numeros[0]:
        numeros.insert(0, numero)

    elif numero >= numeros[len(numeros)-1]:
        numeros.append(numero)

    else:

        for n in range(0, len(numeros)):
            
            if numero <= numeros[n]:
                numeros.insert(n, numero)

print(numeros)
