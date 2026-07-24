# Par ou Impar

from random import randint
contador = 0

while True:

    numero_usuario = int(input('Digite um número (0 a 10) '))

    while numero_usuario < 0 or numero_usuario > 10:

        numero_usuario = int(input('\nValor Inválido, tente novamente...\nDigite um número (0 a 10) '))

    escolha_usuario = input('Par ou Ímpar? [P/I] ').upper().strip()

    while escolha_usuario != 'P' and escolha_usuario != 'I':

        escolha_usuario = input('\nValor Inválido, tente novamente...\nPar ou Ímpar? [P/I] ').upper().strip()

    numero_maquina = randint(1,10)
    total = numero_maquina + numero_usuario

    if escolha_usuario == 'P' and total % 2 == 0:

        print(f'\nVocê jogou {numero_usuario} e a máquina {numero_maquina}. Total de {total} deu PAR\nVocê GANHOU! Continue...\n')
        contador += 1

    elif escolha_usuario == 'P' and total % 2 != 0:

        print(f'\nVocê jogou {numero_usuario} e a máquina {numero_maquina}. Total de {total} deu ÍMPAR\nVocê PERDEU!\n')
        break

    elif escolha_usuario == 'I' and total % 2 != 0:

        print(f'\nVocê jogou {numero_usuario} e a máquina {numero_maquina}. Total de {total} deu ÍMPAR\nVocê GANHOU! Continue...\n')
        contador += 1

    elif escolha_usuario == 'I' and total % 2 == 0:

        print(f'\nVocê jogou {numero_usuario} e a máquina {numero_maquina}. Total de {total} deu PAR\nVocê PERDEU!\n')
        break

print(f'GAME OVER! Você ganhou {contador} vezes.\n')
