def ficha(jogador,gols):

    if not jogador or jogador.isspace():
        jogador = '<desconhecido>'
    if not gols or gols.isspace() or not gols.isnumeric():
        gols = 0
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'

j, g = input("Digite o nome do jogador: "), input("Quantidade de gols: ")

print(ficha(j,g))
