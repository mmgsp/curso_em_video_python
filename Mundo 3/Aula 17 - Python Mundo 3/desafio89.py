boletim = []

while True:

    nome = input("\nNome: ")
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1+nota_2)/2
    boletim.append([nome,[nota_1,nota_2], media])

    continuar = ""

    while continuar != "S" and continuar != "N":
        continuar = input("\nDeseja continuar? [S/N] ").upper().strip()
    
    if continuar == "N":
        break

print(f"\n{"No.":<4}{"Nome":<10}{"Média":>8}\n-----------------------------------")

for n, aluno in enumerate(boletim):
    print(f"{n:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

while True:

    aluno = int(input(f"\nDeseja ver as notas de qual aluno? (999 para interromper): "))

    if aluno == 999:
        break
    elif aluno < len(boletim):
        print(f"Notas de {boletim[aluno][0]}: {boletim[aluno][1]}")
    else:
        print("Número inválido, tente novamente...")
