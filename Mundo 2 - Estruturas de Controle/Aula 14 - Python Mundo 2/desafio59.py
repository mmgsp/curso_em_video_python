# Menu e Operações básicas

menu = 0
continuar = ''
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))

while menu != 5:

    continuar = ''
    menu = int(input(f"""
                     
Escolha qual operação executar com os números {num1} e {num2}
                     
[ 1 ] - Somar

[ 2 ] - Multiplicar

[ 3 ] - Maior

[ 4 ] Novos números

[ 5 ] Sair do programa 

Escolha: """))
    
    if menu == 1:

        print(f'\nSoma: {num1} + {num2} = {num1 + num2}')

        while continuar != 'S' and continuar != 'N':

            continuar = input('Deseja continuar? [S/N]: ').strip().upper()

            if continuar not in 'SN':

                print('Opção inválida, tente novamente...\n')

            elif continuar == 'N':

                menu = 5

    elif menu == 2:
        
        print(f'\nMultiplicação: {num1} x {num2} = {num1 * num2}')

        while continuar != 'S' and continuar != 'N':

            continuar = input('Deseja continuar? [S/N]: ').strip().upper()

            if continuar not in 'SN':

                print('Opção inválida, tente novamente...\n')

            elif continuar == 'N':

                menu = 5

    elif menu == 3:

        if num1 > num2:
            print(f'\nMaior: {num1} > {num2}')
        elif num2 > num1:
            print(f'\nMaior: {num2} > {num1}')
        else:
            print(f'Não há Maior: {num1} = {num2}')

        while continuar != 'S' and continuar != 'N':

            continuar = input('Deseja continuar? [S/N]: ').strip().upper()

            if continuar not in 'SN':

                print('Opção inválida, tente novamente...\n')

            elif continuar == 'N':

                menu = 5

    elif menu == 4:
        num1 = float(input('\nDigite um valor: '))
        num2 = float(input('Digite outro valor: '))

        while continuar != 'S' and continuar != 'N':

            continuar = input('Deseja continuar? [S/N]: ').strip().upper()

            if continuar not in 'SN':

                print('Opção inválida, tente novamente...\n')

            elif continuar == 'N':

                menu = 5

    elif menu > 5 or menu <= 0:
        print('\nOpção Inválida, tente novamente...')

print('\nFim da operação...')