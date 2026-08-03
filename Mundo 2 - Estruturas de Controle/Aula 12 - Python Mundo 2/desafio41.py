# Categoria de atleta por idade

idade = int(input('Digite a idade do atleta: '))

if idade < 0:
    print('\nValor inválido. Tente novamente...')
elif idade <= 9:
    print(f'\nCATEGORIA: MIRIM ({idade} anos)')
elif idade <= 14:
    print(f'\nCATEGORIA: INFANTIL ({idade} anos)')
elif idade <= 19:
    print(f'\nCATEGORIA: JÚNIOR ({idade} anos)')
elif idade <= 20:
    print(f'\nCATEGORIA: MIRIM ({idade} anos)')
else:
    print(f'\nCATEGORIA: MASTER. ({idade} anos)')
