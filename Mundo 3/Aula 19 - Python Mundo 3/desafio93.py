jogador = {}

jogador["Nome"] = input("CARREIRA JOGADOR\n\nNome: ").strip().title()
jogador["Nº_Camisa"] = int(input("Nº da camisa: "))
jogador["Qtde_partidas"] = int(input("Quantidade de partidas jogadas: "))

partidas = []
total_gols = 0
print()

for partida in range(jogador["Qtde_partidas"]):
    gols = int(input(f"Gols na {partida+1}ª partida: "))
    total_gols += gols

    partidas.append(gols)

jogador["Total_gols"] = total_gols

print(f"\nJogador: {jogador["Nome"]}\nNº da Camisa: {jogador["Nº_Camisa"]}\nPartidas Jogadas: {jogador['Qtde_partidas']}\nTotal de Gols: {jogador["Total_gols"]}\n")
print(f"{"Partida":<9}{"|":<2}{"Nº Gols":<7}")

for p, partida in enumerate(partidas):
    print(f"{p+1:^9}{"|":<2}{partida:^7}")

