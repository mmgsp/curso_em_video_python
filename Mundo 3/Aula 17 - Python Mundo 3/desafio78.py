# 5 valores numa lista: maior menor e posição na lista

numeros = []
maior = menor = 0

for contador in range(1,6):

    numero = int(input(f'Digite o {contador}º número: '))

    if contador == 1:
        maior = menor = numero

    elif numero > maior:
        maior = numero

    elif numero < menor:
        menor = numero

    numeros.append(numero)

print(f'\nO maior número digitado foi {maior} nas posições: ', end='')

for c in range(0,len(numeros)):

    if numeros[c] == maior:
            print(c+1, end = ' ')

print(f'\nO menor número digitado foi {menor} nas posições: ', end='')

for c in range (0,len(numeros)):

    if numeros[c] == menor:
        print(c+1, end = ' ')
