# Calculando preço de aluguel de carros
km = float(input('Quantidade de quilômetros rodados: '))
d = int(input('Quantidade de dias de aluguel do carro: '))
v = 60*d + 0.15*km
print(f'O valor do aluguel será R$ {v:.2f}')
