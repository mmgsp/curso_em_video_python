# Escolhendo um número de 1 a 5 e tentando adivinhar o número escolhido, utilizando while

from random import choice

contador = 0

num_maq = int(choice(range(0,6)))
num_usuario = int(input('Digite um número entre 0 a 5: '))

if num_maq == num_usuario:

    contador+= 1
    
else:

    while num_maq != num_usuario:

        contador += 1
        print(f'\nVocê perdeu...\nNúmero da máquina: {num_maq} x {num_usuario} Número do usuário\nNúmero de tentativas: {contador}\n')

        num_maq = int(choice(range(0,6)))
        num_usuario = int(input('Digite um número entre 0 a 5: '))

    contador += 1

print(f'\nVocê venceu!\nNúmero da máquina: {num_maq} x {num_usuario} Número do usuário\nNúmero de tentativas: {contador}')
