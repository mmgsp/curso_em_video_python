
div = 0
n = int(input('Digite um número: '))

for c in range(1,n+1):
    if n%c == 0:
        div += 1

if div == 2:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
