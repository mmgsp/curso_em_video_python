import json
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
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except: 
        return

def salvar():
    global dados

    with open("dados.json", "w", encoding = "utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def deletar():
    global dados

    dados.clear()
