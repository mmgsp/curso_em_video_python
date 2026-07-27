pessoas = []
dados = []
contador = 0

while True:

    dados.append(str(input("\nNome: ")))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    contador += 1

    continuar = ""

    while continuar != "S" and continuar != "N":
        continuar = input("\nDeseja continuar? [S/N] ").upper().strip()

    if continuar == "N":
        break

for p, pessoa in enumerate(pessoas):

    if p == 0:
        maior_peso = menor_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]

        elif pessoa[1] < menor_peso:
            menor_peso = pessoa[1]

print(f"""

Foram cadastradas {contador} pessoas.
O maior peso foi {maior_peso:.1f} Kg. Peso de {[pessoa[0] for pessoa in pessoas if pessoa[1] == maior_peso]}
O menor peso foi {menor_peso:.1f} Kg. Peso de {[pessoa[0] for pessoa in pessoas if pessoa[1] == menor_peso]}

""")



