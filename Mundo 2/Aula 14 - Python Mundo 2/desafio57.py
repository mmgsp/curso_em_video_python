# Validando entrada de dados

sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()

while sexo not in 'MF':
    print('\nResposta inválida, tente novamente... ')
    sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()

print(f'\nResposta válida, o sexo informado foi: {sexo}\n')
