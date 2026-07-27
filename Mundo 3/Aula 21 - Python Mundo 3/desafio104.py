def leia_int(str_entrada):

    entrada = input(f"{str_entrada}")

    while not entrada or entrada.isspace() or not entrada.isnumeric():
        entrada = input("ERRO! Digite um número inteiro válido.\nDigite um número: ")

    return entrada


n = leia_int('Digite um número: ')
print(f"Você acabou de digitar o numero {n}")
   