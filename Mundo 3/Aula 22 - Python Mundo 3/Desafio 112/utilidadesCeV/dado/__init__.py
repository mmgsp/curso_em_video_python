def valor_numero(valor):
    return valor.replace('.','',1).isdigit()

def leiaDinheiro(mensagem):

    valor = input(mensagem).strip() 

    if not valor:
        print(f'\nValor "{valor}" inválido! Tente novamente...\n')
        return leiaDinheiro(mensagem) 

    if not valor[0].isnumeric():
        print(f'\nValor "{valor}" inválido! Tente novamente...\n')
        return leiaDinheiro(mensagem)

    if ',' in valor:
        valor = valor.replace(',', '.')

    if not valor_numero(valor):
        print(f'\nValor "{valor}" inválido! Tente novamente...\n')
        return leiaDinheiro(mensagem) 
    else:
        return float(valor)
