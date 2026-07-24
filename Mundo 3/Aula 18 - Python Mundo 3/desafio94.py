pessoas = []
mulheres = []
mais_velhos = []
dados = {}


soma_idades = 0

while True:

    dados["Nome"] = input("\nNome: ").strip().title()
    dados["Idade"] = int(input("Idade: "))

    soma_idades += dados["Idade"]
    
    dados["Sexo"] = input("Sexo [M/F]: ").upper().strip()

    while dados["Sexo"] != "M" and dados["Sexo"] != "F":
        dados["Sexo"] = input("\nDado Inválido, tente novamente...\nSexo [M/F]: ").upper().strip()

    if dados["Sexo"] == "F":
        mulheres.append(dados["Nome"])

    pessoas.append(dados.copy())

    continuar = ""

    while continuar != "S" and continuar != "N":
        continuar = input("\nDeseja continuar? [S/N] ").upper().strip()

    if continuar == "N":
        break

media_idades = int(round(soma_idades/len(pessoas)))

for pessoa in pessoas:
    if pessoa["Idade"] > media_idades and pessoa not in mais_velhos:
        mais_velhos.append(pessoa)

print(f"\n- Ao todo foram cadastradas {len(pessoas)} pessoas, com uma média de {media_idades} anos.")
print(f"- As mulheres cadastradas foram: {', '.join(mulheres)}.")
print(f"- Pessoas com idade acima da média dos informados:")

for pessoa in mais_velhos:

    print(f"        Nome: {pessoa['Nome']:<14} Sexo: {pessoa['Sexo']:<4} Idade: {pessoa['Idade']}")

