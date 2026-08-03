# Maiores e menores pesos

maior = 0
menor = 0

for c in range(1,5):
    peso = float(input(f'Digite o peso (kg) da {c}ª pessoa: '))

    if c == 1:
        maior = peso
        menor = peso

    elif peso > maior:
        maior = peso

    elif peso < menor:
        menor = peso

print(f'O maior peso é: {maior:.1f} kg e o menor peso é: {menor:.1f} kg')
