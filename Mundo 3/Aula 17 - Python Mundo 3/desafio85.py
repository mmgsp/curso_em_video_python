numeros = [[],[]]

for n in range(7):

    numero = int(input(f"Digite o {n+1}º valor: "))

    if numero%2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(f"\nNúmeros pares: {sorted(numeros[0])}")
print(f"Números ímpares: {sorted(numeros[1])}\n")
