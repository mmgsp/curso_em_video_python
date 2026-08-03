# Tabuada de vários números 

while True:
    numero = int(input('\nDigite um número e mostrarei sua tabuada (número negativo para parar): '))
    if numero < 0:
        break
    else:
        for c in range (1,11):
            print(f'{numero} x {c} = {numero*c}')

print('\nFim da execução.')
