# Mostrando um número por extenso (de 0 a 20)

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numero = int(input('Qual número você deseja ver por extenso (de 0 a 20)? '))

while numero < 0 or numero > 20:
    numero = int(input('\nValor Inválido, tente novamente...\nQual número você deseja ver por extenso (de 0 a 20)? '))

print(f'{numero} -> {numeros[numero]}')
