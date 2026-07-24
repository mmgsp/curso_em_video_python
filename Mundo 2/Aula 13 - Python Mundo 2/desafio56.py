soma_idade = 0
qtde_mulheres = 0
homens = []
idade_homens = []

for c in range(1,5):

    nome = input(f'Digite o nome da {c}ª pessoa: ')
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = input(f'Digite o gênero dessa pessoa (M/F): ').strip().upper()
    print('\n')

    soma_idade += idade

    if sexo == 'F':
        
        if idade < 20:
            qtde_mulheres += 1

    elif sexo == 'M':

        homens.append(nome)
        idade_homens.append(idade)

media = soma_idade/4

for c in range(0,len(idade_homens)):

    if c == 0:

        idade_velho = idade_homens[0]
        velho =  homens[0]

    elif idade_homens[c] > idade_homens[c-1]:

        idade_velho = idade_homens[c]
        velho = homens[c]

print(media,qtde_mulheres,velho,idade_velho)
