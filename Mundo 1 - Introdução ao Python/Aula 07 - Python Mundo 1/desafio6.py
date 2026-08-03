# Lendo um número e mostrando seu dobro, triplo e raiz quadrada
from math import sqrt
n = float(input('Digite um número: '))
d = 2*n
t = 3*n
r = sqrt(n)
print(f'\nO dobro de {n} é {d:.2f}\nO triplo de {n} é {t:.2f}\nA raíz quadrada de {n} é {r:.2f}\n')
