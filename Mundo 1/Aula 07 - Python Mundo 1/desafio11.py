# Área de uma parede e quantidade de tinta a partir de largura e altura
l = float(input('Digite o valor da largura em metros: '))
a = float(input('Digite o valor da altura em metros: '))
ar = l*a
t = ar/2
print(f'\nA área da parede é {ar:.2f} m²\nSerão necessários {t:.1f} litros de tinta para pintá-la.\n')
