
soma = 0

for c in range(1,501):
    if c%2 != 0:
        if c%3 == 0:
            soma += c

print(f'A soma de todos os números ímpares e múltiplos de 3 entre 1 e 500 é: {soma}')
