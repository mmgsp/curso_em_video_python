# Melhorando Desafio 61

termo = float(input('Digite o primeiro termo de uma PA: '))
razao = float(input('Digite a razão dessa PA: '))

contador = 1
limite = 10

while contador <= limite:

    print(f'{contador}º termo = {termo:.2f}')

    termo += razao

    if contador == limite:

        continuar = int(input('Deseja mostrar mais quantos valores? '))

        if continuar < 0:

            while continuar < 0:

                continuar = int(input('\nValor inválido, tente novamente...\nDeseja mostrar mais quantos valores? '))

        if continuar > 0:

            limite += continuar

    contador += 1

    

