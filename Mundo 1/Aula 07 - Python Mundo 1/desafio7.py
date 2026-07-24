# Lendo duas notas de um aluno e calculando a média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'\nA média do aluno foi: {m:.1f}')
if m >= 7:
    print('Ele foi aprovado!\n')
else:
    print('Ele foi reprovado...\n')
