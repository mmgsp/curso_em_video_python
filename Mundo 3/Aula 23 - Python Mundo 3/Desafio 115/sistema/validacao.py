from banco_de_dados import dados

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


def leiaCod(str_entrada):
        
    cod = leiaInt("Digite o código do cadastro que você deseja alterar: ")
    if 0<=cod<len(dados):
        return cod
    else:
        print("\033[31mErro! Código inválido...\033[0m")
        return leiaCod(str_entrada)

