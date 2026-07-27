def notas(*n,sit=False):

    qtde_notas = len(n)
    maior_nota = max(n)
    media = sum(n)/qtde_notas

    relatorio = {"Total": qtde_notas, "Maior": maior_nota, "Média": f'{media:.1f}'}

    if sit == True:
        if media < 5:
            situacao = 'RUIM'
        elif media >= 7:
            situacao = 'BOA'
        else:
            situacao = 'RAZOÁVEL'

        relatorio["Situação"] = situacao

    return relatorio


notas = notas(5, 4)
print(notas)
