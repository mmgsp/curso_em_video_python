# Escolhendo entre quatro alunos
from random import choice
i = 1
list = []
while i<=4:
    nome = input(f'Digite o nome do(a) {i}º(ª) aluno(a): ')
    list.append(nome)
    i += 1
print(f'\nO aluno sorteado foi: {choice(list)}\n')
