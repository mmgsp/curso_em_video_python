# Dois números inteiros -> Maior, menor ou iguais?

n1 =  int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))

if  n2 > n1:
    print(f'\nMaior valor: {n2}\nMenor valor: {n1}\n')
elif n1 > n2:
    print(f'\nMaior valor: {n1}\nMenor valor: {n2}\n')
else:
    print(f'\nOs dois valores são iguais! ({n1} = {n2})\n')
