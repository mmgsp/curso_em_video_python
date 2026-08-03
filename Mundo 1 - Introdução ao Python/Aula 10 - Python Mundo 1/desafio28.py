# Escolhendo um número de 1 a 5 e tentando adivinhar o número escolhido

from random import choice

num_maq = int(choice(range(0,6)))

num_usuario = int(input('Digite um número entre 0 a 5: '))

if num_maq == num_usuario:
    print(f'\nVocê venceu!\nNúmero da máquina: {num_maq} x {num_usuario} Número do usuário\n')
else:
    print(f'\nVocê perdeu!\nNúmero da máquina: {num_maq} x {num_usuario} Número do usuário\n')
