from datetime import datetime
dados_trabalhistas = {}

dados_trabalhistas["Nome"] = input("Nome: ")
dados_trabalhistas["Ano de Nascimento"] = int(input("Ano de nascimento: "))
dados_trabalhistas["Idade"] = int(datetime.now().year) - dados_trabalhistas["Ano de Nascimento"] 
dados_trabalhistas["CTPS"] = input("CTPS (0 se não tiver): ")

if dados_trabalhistas["CTPS"] != 0:
    dados_trabalhistas["Ano de Contratação"] = int(input("Ano de Contratação: "))
    dados_trabalhistas["Salário"] = float(input("Salário: R$ "))
    dados_trabalhistas["Tempo de Contribuição"] = int(datetime.now().year) - dados_trabalhistas["Ano de Contratação"]

    if dados_trabalhistas["Tempo de Contribuição"] >= 35:
        dados_trabalhistas["Aposentadoria"] = "Sim"
        dados_trabalhistas["Tempo Restante"] = 0

    else:
        dados_trabalhistas["Aposentadoria"] = "Não"
        dados_trabalhistas["Tempo Restante"] = 35 - dados_trabalhistas["Tempo de Contribuição"]

print(f"\n{"Nome":<25}{"|":<2}{"Nascimento":<12}{"|":<2}{"Idade":<8}{"|":<2}{"CTPS":<13}{"|":<2}{"Contratação":<13}{"|":<2}{"Salário":<12}{"|":<2}{"Contribuição":<14}{"|":<2}{"Aposentadoria":<15}{"|":<2}{"Restante":<8}\n----------------------------------------------------------------------------------------------------------------------------------------\n{dados_trabalhistas["Nome"]:<25}{"|":<2}{dados_trabalhistas["Ano de Nascimento"]:<12}{"|":<2}{dados_trabalhistas["Idade"]:<8}{"|":<2}{dados_trabalhistas["CTPS"]:<13}{"|":<2}{dados_trabalhistas["Ano de Contratação"]:<13}{"|":<2}{dados_trabalhistas["Salário"]:<12}{"|":<2}{dados_trabalhistas["Tempo de Contribuição"]:<14}{"|":<2}{dados_trabalhistas["Aposentadoria"]:<15}{"|":<2}{dados_trabalhistas["Tempo Restante"]:<8}")
