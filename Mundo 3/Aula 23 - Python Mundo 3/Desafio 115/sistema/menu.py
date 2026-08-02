from . import banco_de_dados

def menu():
    banco_de_dados.carregar()

    while True:

        opcao = input(f"""\n{banco_de_dados.linha('-')}
                ALUMIAR APP (Menu Inicial)
{banco_de_dados.linha('-')}

1 - Cadastrar
2 - Listar cadastros
3 - Atualizar cadastro
4 - Deletar usuário/banco de dados
0 - Sair
            
Escolha: """).strip()

        if opcao == "1":
            banco_de_dados.cadastrar()
        elif opcao == "2":
            banco_de_dados.listar()
        elif opcao == "3":
            banco_de_dados.atualizar()
        elif opcao == "4":
            banco_de_dados.deletar()
        elif opcao == "0":
            banco_de_dados.salvar()
            break  
        else:
            print("Comando inválido, tente novamente...")
