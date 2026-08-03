# IMC 

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso/(altura**2)

if imc < 18.5:
    print(f'\nRESULTADO DO IMC -> ABAIXO DO PESO ({imc:.1f})\n')
elif imc < 25:
    print(f'\nRESULTADO DO IMC -> PESO IDEAL ({imc:.1f})\n')
elif imc < 30:
    print(f'\nRESULTADO DO IMC -> SOBREPESO ({imc:.1f})\n')
elif imc <= 40:
    print(f'\nRESULTADO DO IMC -> OBESIDADE ({imc:.1f})\n')
else:
    print(f'\nRESULTADO DO IMC -> OBESIDADE MÓRBIDA ({imc:.1f})\n')
