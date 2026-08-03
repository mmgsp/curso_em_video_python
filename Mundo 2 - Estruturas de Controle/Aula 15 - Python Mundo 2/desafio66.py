# Lendo vários números e somando-os

contador = soma = 0

while True:

    numero = int(input('Digite um número (999 = Stop): '))

    if numero == 999:
        break

    else:
        soma += numero
        contador += 1

print(f'\nO somatório total dos {contador} números digitados foi: {soma}')
