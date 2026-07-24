# Avaliando se um ano é bissexto ou não:
# Regra Geral: Divisível por 4. Exceção -> Anos centenários (terminados em 00): Divisível por 400

ano = int(input('Digite um ano: '))

if ano % 100 == 0:
    if ano % 400 == 0:
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')
else:
    if ano % 4 == 0:
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')
