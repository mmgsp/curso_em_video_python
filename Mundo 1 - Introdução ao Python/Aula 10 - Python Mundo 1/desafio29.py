# Aplicando multa por excesso de velocidade

velocidade = int(input('Digite a velocidade (Km/h): '))

excedente = velocidade - 80

if excedente <= 0:
    print(f'\nVocê está dentro do limite de velocidade!\nVelocidade atual: {velocidade}Km/h\n')
else:
    print(f'\nVocê foi multado, excedeu o limite de velocidade por {excedente} Km/h!\nVelocidade atual: {velocidade} Km/h\nMulta aplicada: R$ {7*excedente}\n')