import json
from time import sleep
from validacao import leiaNome, leiaInt, leiaCod
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
        print(f"{linha('-')}\n{'PESSOAS CADASTRADAS':^54}\n{linha('-')}\n{'cod':<4}{'Nome':<40}{'Idade':>10}\n")
        for cod, pessoa in enumerate(dados):
            print(f"{cod:<4}{pessoa["Nome"]:<40}{f"{pessoa["Idade"]} anos":>10}")
        print(f"{linha('-')}")

def atualizar():
    if not dados:
        print("0 usuários cadastrados...")
    else:
        listar()
        cod = leiaCod("Digite o código do cadastro que você deseja alterar: ")
        nome_atual = dados[cod]["Nome"]
        idade_atual = dados[cod]["Idade"]

        nome = leiaNome(f"Digite o nome novo (Atual - {nome_atual}): ")
        idade = leiaInt(f"Digite a nova idade (Atual - {idade_atual}): ")

        dados[cod]["Nome"] = nome
        dados[cod]["Idade"] = idade
        print("Dados atualizados com sucesso!")

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
    salvar()
