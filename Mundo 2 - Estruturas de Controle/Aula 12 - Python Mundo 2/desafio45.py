# Jokenpô
from random import choice

opcoes = ['PEDRA','PAPEL','TESOURA']
escolha_usuario = input('Pedra, Papel ou Tesoura? ').upper().strip()
escolha_maquina = choice(opcoes)

if escolha_usuario not in opcoes:
    print('Escolha inválida, tente novamente...')

elif escolha_usuario == escolha_maquina:
    print(f'\nEMPATE.\n(MÁQUINA) {escolha_maquina} x {escolha_usuario} (VOCÊ)\n')

elif (escolha_usuario == 'TESOURA' and escolha_maquina == 'PAPEL') or (escolha_usuario == 'PAPEL' and escolha_maquina == 'PEDRA') or (escolha_usuario == 'PEDRA' and escolha_maquina == 'TESOURA'):
    print(f'\nVOCÊ VENCEU!\n(MÁQUINA) {escolha_maquina} x {escolha_usuario} (VOCÊ)\n')

else:
    print(f'\nVOCÊ PERDEU...\n(MÁQUINA) {escolha_maquina} x {escolha_usuario} (VOCÊ)\n')
