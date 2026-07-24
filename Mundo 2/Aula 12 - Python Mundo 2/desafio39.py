# Avanliando data de alistamento militar
from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
alistamento = nascimento + 18
atual =  date.today().year
idade = atual - nascimento

if idade == 18:
    print(f'\nChegou sua hora!\nVocê já tem {idade} anos, deverá se alistar neste ano ({atual})\n')
elif idade<18:
    print(f'\nAinda não chegou sua hora...\nVocê tem {idade} anos de idade. Faltam {alistamento-atual} anos para você se alistar.\nVocê precisará se alistar no ano de {alistamento}\n')
else:
    print(f'\nJá passou da sua hora!\nVocê tem {idade} anos de idade. Passaram-se {atual-alistamento} anos desde o ano de seu alistamento.\nVocê deveria se alistar no ano de {alistamento}\n')
