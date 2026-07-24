from random import choice

jogos = []
jogo = []

qtde_jogos = int(input("GERADOR DE JOGOS DA MEGA SENA\n\nDigite quantos jogos deseja gerar: "))

if qtde_jogos > 0:
    for j in range(qtde_jogos):
        while len(jogo) < 6:

            numero = choice(range(61))
            if numero not in jogo and numero != 0:
                jogo.append(numero)

        jogos.append(jogo[:])
        jogo.clear()

print()
for numero_jogo, mega_sena in enumerate(jogos):
    print(f"JOGO {numero_jogo+1}: {sorted(mega_sena)}")

