# Calculando a hipotenusa a partir dos catetos
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print(f'A hipotenusa vale: {hypot(co, ca):.2f}')
