# Fatorial (usando While .-.)

numero = int(input('Digite um número: '))
fatorial = 1

while numero > 0:

    print(f'{numero}', end = '')

    if numero != 1:
        print('x',end = '')

    else:
        print(' =', end = ' ')

    if numero != 0:

        fatorial *= numero

    numero -= 1


print(fatorial)
