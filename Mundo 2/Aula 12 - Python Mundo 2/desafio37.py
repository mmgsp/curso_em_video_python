# Convertendo número inteiro para binario, octal ou hexadecimal

numero = int(input('DIgite o valor de um número inteiro: '))
menu = int(input(f"""
(MENU DE CONVERSÃO)

O número {numero} será convertido para:                                  
1 - Binário
2 - Octal
3 - Hexadecimal             
                 
Escolha: """))

if menu == 1:
    print(f'\n{numero} -> {bin(numero)[2:]} (binário)\n')
elif menu == 2:
    print(f'\n{numero} -> {oct(numero)[2:]} (octal)\n')
elif menu == 3:
    print(f'\n{numero} -> {hex(numero)[2:]} (hexadecimal)\n')
else:
    print('\nOpção Inválida, tente novamente...')
