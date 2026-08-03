# Três numeros, maior e menor

n1 = float(input('Digite um número: '))
maior = n1
n2 = float(input('Digite outro número: '))
if n2 > n1:
    maior = n2
    menor = n1
else:
    menor = n2
n3 = float(input('Digite um último número: '))
if n3 < menor:
    menor = n3
else:
    if n3 > maior:
        maior = n3
print(f'\nO menor número entre {n1,n2,n3} é: {menor}\nO maior número entre {n1,n2,n3} é: {maior}\n')
