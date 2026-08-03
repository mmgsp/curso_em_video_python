# Passou de ano?

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media >= 7:
    print(f'\nAprovado! Média: {media:.1f}\n')
elif media >= 5:
    print(f'\nRecuperação... Média: {media:.1f}\n')
else:
    print(f'\nReprovado. Média: {media:.1f}\n')
