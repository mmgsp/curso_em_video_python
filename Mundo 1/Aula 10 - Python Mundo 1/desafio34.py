# Calculando aumento baseado no valor do salário atual

salario = float(input('Digite o valor de seu salário atual: R$ '))
if salario > 1250:
    print(f'Seu novo salário será de: R$ {1.1*salario:.2f} (aumento de 10%)')
else:
    print(f'Seu novo salário será de: R$ {1.5*salario:.2f} (aumento de 15%)')
