def leiaInt(str_entrada):

    try:
        entrada = int(input(f"{str_entrada}"))
    except KeyboardInterrupt:
        entrada = 0
        return entrada
    except:
        print("Erro! Digite um valor inteiro válido...")
        return leiaInt(str_entrada)
    else:
        return entrada

def leiaFloat(str_entrada):

    try:
            entrada = float(input(f"{str_entrada}"))
    except KeyboardInterrupt:
        entrada = 0
        return entrada
    except:
        print("Erro! Digite um valor real válido...")
        return leiaFloat(str_entrada)
    else:
        return entrada
