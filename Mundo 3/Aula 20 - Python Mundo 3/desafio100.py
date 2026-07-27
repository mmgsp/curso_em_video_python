from random import randint
numeros = []

def sorteia():
    for n in range(5):
        numeros.append(randint(1,10))
    print(f"Números sorteados: {numeros}")

def somapar(numeros):

    soma = 0
    for numero in numeros:
        if numero%2 == 0:
            soma+=numero
    print(f"A soma dos valores pares de {numeros} é: {soma}")

sorteia()
somapar(numeros)

