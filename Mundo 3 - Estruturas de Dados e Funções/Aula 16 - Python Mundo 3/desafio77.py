# Analisando Strings contidas em Tupla -> Vogais

palavras = ('janela', 'computador', 'estrada', 'oceano', 'montanha', 'relógio', 'biblioteca', 'teclado', 'lâmpada',
            'caderno', 'nuvem', 'espelho', 'cadeira', 'telefone', 'garrafa', 'floresta', 'chuva', 'avião', 'porta', 'areia')

for palavra in palavras:

    print(f'{palavra} -> ', end='')

    for letra in palavra.upper():

        if letra in ('AEIOU'):

            print(f'{letra}', end=' ')

    print(f'\n')
