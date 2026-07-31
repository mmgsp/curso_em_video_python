from validacao import leiaNome, leiaInt
from menu import linha
dados = []

def cadastrar():

    pessoa = {}
    pessoa["Nome"] = leiaNome("Nome: ")
    pessoa["Idade"] = leiaInt("Idade: ")
    dados.append(pessoa)

def listar():
    global dados

    if not dados:
        print("0 usuários cadastrados...")
    else:
        print(f"{linha('-')}\n{'PESSOAS CADASTRADAS':^54}\n{linha('-')}")
        for pessoa in dados:
            print(f"{pessoa["Nome"]:<44}{f"{pessoa["Idade"]} anos":>10}")
        print(f"{linha('-')}")


def carregar():
    global dados

    with open("dados.txt", "r") as arquivo:
        dados = arquivo.read()

def salvar():
    global dados

    with open("dados.txt", "w", encoding = "utf-8") as arquivo:
        arquivo.write(dados)

def deletar():
    global dados

    dados.clear()


cadastrar()
cadastrar()
cadastrar()
listar()
