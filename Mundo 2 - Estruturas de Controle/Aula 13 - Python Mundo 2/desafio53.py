
frase = input('Digite uma frase: ')

frase_analise = frase.upper().replace(' ','')

palindromo = ''

for c in range(len(frase_analise)-1,-1,-1):
    palindromo += frase_analise[c]

if frase_analise == palindromo:
    print(f'A frase {frase} é um palindromo.')
else:
    print(f'A frase {frase} não é um palindromo.')
