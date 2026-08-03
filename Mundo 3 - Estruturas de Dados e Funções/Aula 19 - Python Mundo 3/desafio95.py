jogadores = []
jogador = {}

while True:

    jogador["Nome"] = input("\nCARREIRA JOGADOR\n\nNome: ").strip().title()
    jogador["Nº_Camisa"] = int(input("Nº da camisa: "))
    jogador["Qtde_partidas"] = int(input("Quantidade de partidas jogadas: "))

    partidas = []
    total_gols = 0
    print()

    for partida in range(jogador["Qtde_partidas"]):
        gols = int(input(f"Gols na {partida+1}ª partida: "))
        total_gols += gols

        partidas.append(gols)

    jogador["Partidas"] = partidas
    jogador["Total_gols"] = total_gols

    jogadores.append(jogador.copy())

    continuar = ""
    
    while continuar != "S" and continuar != "N":
        continuar = input("\nDeseja continuar? [S/N] ").upper().strip()
    
    if continuar == "N":
        break

print(f"\n{'ID':<4}{'|':<2}{'Jogador':<15}{'|':<2}{'Nº_Camisa':<15}{'|':<2}{'Qtde_partidas':<20}{'|':<2}{'Total_gols':<14}\n-----------------------------------------------------------------------------------")

for j, jogador in enumerate(jogadores):
    print(f"{j:<4}{'|':<2}{jogador['Nome']:<15}{'|':<2}{jogador['Nº_Camisa']:<15}{'|':<2}{jogador['Qtde_partidas']:<20}{'|':<2}{jogador['Total_gols']:<14}")

while True:

    selecionado = int(input("\nDeseja ver o histórico de qual jogador? (999 para sair): "))

    if selecionado == 999:
        break

    print(f"\nHistórico de {jogadores[selecionado]["Nome"]}\n{'Partida':<9}{'|':<2}{'Nº Gols':<7}")

    for p, partida in enumerate(jogadores[selecionado]["Partidas"]):

        print(f"{p+1:^9}{"|":<2}{partida:^7}")
