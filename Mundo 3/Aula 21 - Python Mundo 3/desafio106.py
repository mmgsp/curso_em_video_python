def Pyhelp(comando):

    if comando != 'fim':

        help(comando)

        ajuda = input("Função ou biblioteca > ").strip().lower()

        Pyhelp(ajuda)

    else:
        print("Fim da execução...")
        return

        

ajuda = input("Função ou biblioteca > ").strip().lower()
Pyhelp(ajuda)
