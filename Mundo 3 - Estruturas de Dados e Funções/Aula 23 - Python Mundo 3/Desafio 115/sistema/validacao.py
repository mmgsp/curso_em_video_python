def leiaNome(str_entrada):

    entrada = str(input(str_entrada)).strip()

    nome = entrada.replace(' ','').isalpha()

    if nome:
        return entrada
    else:
        print("\033[31mERRO! Digite um nome válido...\033[0m")
        return leiaNome(str_entrada)

def leiaInt(str_entrada):

    try:
        entrada = int(input(f"{str_entrada}"))
    except KeyboardInterrupt:
        entrada = 0
        return entrada
    except:
        print("\033[31mErro! Digite um valor inteiro válido...\033[0m")
        return leiaInt(str_entrada)
    else:
        return entrada
