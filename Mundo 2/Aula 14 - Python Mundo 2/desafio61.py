# Refazendo o desafio 51 usando while

termo = float(input('Digite o primeiro termo de uma PA: '))
razao = float(input('Digite a razão dessa PA: '))
contador = 1

while contador < 11:
    print(f'{contador}º termo = {termo:.2f}')
    termo += razao
    contador += 1
