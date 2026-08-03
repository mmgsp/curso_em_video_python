# Sorteando 5 números inteiros aleatórios e mostrando maior e menor, usando tupla

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

for c in range(0,5):

    if c == 0:
        maior = menor = numeros[c]

    elif numeros[c] > maior:
        maior = numeros[c]

    elif numeros[c] < menor:
        menor = numeros[c]


print(f'\nOs números sorteados foram: {numeros}\nO maior número foi: {maior}\nO menor número foi: {menor}\n')