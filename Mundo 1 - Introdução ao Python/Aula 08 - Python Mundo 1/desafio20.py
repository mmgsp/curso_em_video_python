# Sorteando ordem dos alunos
from random import shuffle
i = 1
list = []
while i <= 4:
    nome = input(f'Digite o nome do(a) {i}º(ª) aluno(a): ')
    list.append(nome)
    shuffle(list)
    i += 1
print(f'\nA ordem sorteada dos alunos escolhidos será: {list}\n')
