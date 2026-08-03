matriz = [ [],
           [],
           [] ]

soma_pares = soma_terceira_coluna = 0

for linha in range(3):
    for coluna in range(3):
        numero = int(input(f"Digite o número para a posição {linha, coluna}: "))

        if numero%2 == 0:
            soma_pares += numero
        
        if coluna == 2:
            soma_terceira_coluna += numero

        matriz[linha].append(numero)

for linha in matriz:
    print()
    for coluna in linha:
        print(f"[ {coluna:^5} ]", end=" ")

print(f"\n\nA soma dos números pares é: {soma_pares}\nA soma dos números da terceira coluna é: {soma_terceira_coluna}\nO maior valor da segunda linha é {max(matriz[1])}\n")
