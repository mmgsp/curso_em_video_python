
termo = float(input('Digite o primeiro termo de uma PA: '))
razao = float(input('Digite a razão dessa PA: '))

for c in range(1,11):
    print(f'{c}º termo = {termo:.2f}')
    termo += razao
