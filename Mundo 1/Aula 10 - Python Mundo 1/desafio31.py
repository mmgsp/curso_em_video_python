# Calculando valor de viagens por Km

distancia = float(input('Digite a distância da viagem (em Km): '))

if distancia <= 200:
    print(f'O valor da viagem será de: R$ {distancia*0.5:.2f}')
else:
    print(f'O valor da viagem será de: R$ {distancia*0.45:.2f}')
