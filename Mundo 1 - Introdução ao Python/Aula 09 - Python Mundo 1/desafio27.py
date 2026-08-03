# Mostrando o primeiro e último nome separadamente

nome = input('Digite um nome completo: ')
print(f'\nPrimeiro nome: {nome.strip().split()[0]}\nÚltimo nome: {nome.strip().split()[len(nome.split())-1]}\n')
