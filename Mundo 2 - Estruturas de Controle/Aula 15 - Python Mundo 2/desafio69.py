# Cadastro e análise simples de dados

maiores = homens = mulheres_menor = 0
n = 1

while True:

    idade = int(input(f'Digite a idade da {n}ª pessoa: '))

    while idade <= 0:
        idade = int(input(f'\nValor Inválido, tente novamente...\nDigite a idade da {n}ª pessoa: '))

    sexo = input(f'Digite o sexo da {n}ª pessoa: ').upper().strip()

    while sexo != 'M' and sexo != 'F':
        sexo = input(f'\nValor Inválido, tente novamente...\nDigite o sexo da {n}ª pessoa: ').upper().strip()

    if idade >= 18:
        maiores += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menor += 1

    continuar = input('\nDeseja continuar? [S/N] ').upper().strip()

    while continuar != 'S' and continuar != 'N':
        continuar = input('\nResposta Inválida, tente novamente...\nDeseja continuar? [S/N] ').upper().strip()
    
    if continuar == 'N':
        break

    n += 1

print(f'\nForam cadastrados {maiores} pessoas maiores de idade.\nForam cadastrados {homens} homens\nForam cadastradas {mulheres_menor} mulheres com menos de 20 anos de idade.\n')

