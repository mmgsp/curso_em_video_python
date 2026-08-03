# Maiores e menores de idade 

from datetime import date

maior = 0
menor = 0

for c in range (1,8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = date.today().year - nascimento

    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'\nDas pessoas informadas {maior} são maiores de idade e {menor} são menores de idade.')
