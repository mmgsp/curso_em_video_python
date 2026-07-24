# Avaliano números do teclado numa tupla

numeros = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))

par = 0

print(f'\nO número 9 foi digitado {numeros.count(9)} vezes.\n')

if 3 in numeros:

    print(f'O número 3 foi digitado na {numeros.index(3)+1}ª posição\n')

else:

    print('O número 3 não foi digitado\n')

for numero in numeros:

    if numero % 2 == 0:

        par += 1

if par >= 1:

    print('Os números pares foram: ', end = '')

    for numero in numeros:

        if numero % 2 == 0:

            print(numero,end = ' ')
    print('\n')

else:

    print('Não foram digitados números pares\n')
