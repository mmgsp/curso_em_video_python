from random import choice
from time import sleep

jogadores = {}
selecionado = []

for j in range (1,5):
    
    jogadores[f"Jogador {j}"] = choice(range(1,7))
    sleep(0.5)
    print(f"O Jogador {j} tirou {jogadores[f"Jogador {j}"]}")

sleep(1)
print()

for colocacao, ordem in enumerate(sorted(jogadores.values(), reverse=True)):
    for jogador, valor in jogadores.items():
        if valor == ordem:
            print(f"{colocacao+1}º lugar => {jogador} com {valor}")
            break
