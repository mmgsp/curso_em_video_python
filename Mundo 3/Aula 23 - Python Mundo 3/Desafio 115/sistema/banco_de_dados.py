import json
from .validacao import leiaNome, leiaInt

dados = []

def linha(caractere):
    return caractere*54

def leiaCod(str_entrada):
        
    cod = leiaInt("Digite o código do cadastro que você deseja alterar: ")
    if 0<=cod<len(dados):
        return cod
    else:
        print("\033[31mErro! Código inválido...\033[0m")
        return leiaCod(str_entrada)

def cadastrar():
    global dados

    pessoa = {}
    pessoa["Nome"] = leiaNome("Nome: ")
    pessoa["Idade"] = leiaInt("Idade: ")
    dados.append(pessoa)

def listar():

    if not dados:
        print("0 usuários cadastrados...")
    else:
        print(f"{linha('-')}\n{'PESSOAS CADASTRADAS':^54}\n{linha('-')}\n{'cod':<4}{'Nome':<40}{'Idade':>10}\n")
        for cod, pessoa in enumerate(dados):
            print(f"{cod:<4}{pessoa["Nome"]:<40}{f"{pessoa["Idade"]} anos":>10}")
        print(f"{linha('-')}")

def atualizar():
    global dados

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

    if not dados:
        print("0 usuários cadastrados...")
    else:
        opcao = leiaInt("\n1 - Deletar um cadastro específico\n2 - Deletar TODO o banco de dados\nEscolha uma opção (1 ou 2): ")

        if opcao == 1:
            listar()
            cod = leiaCod("Digite o código do cadastro que você deseja deletar: ")

            confirmacao = input(f"Tem certeza que deseja apagar o cadastro {dados[cod]} [S/N]?  ").strip().upper()
            if confirmacao == 'S':

                pessoa_removida = dados.pop(cod)
                print(f"Cadastro de {pessoa_removida['Nome']} deletado com sucesso!")
            else:
                print("Operação de exclusão cancelada.")

        elif opcao == 2:
            confirmacao = input("Tem certeza que deseja apagar TODOS os cadastros? [S/N]: ").strip().upper()
            if confirmacao == 'S':
                dados.clear()
                print("Todos os cadastros foram deletados com sucesso!")
            else:
                print("Operação de exclusão cancelada.")
                
        else:
            print("Operação cancelada...")
