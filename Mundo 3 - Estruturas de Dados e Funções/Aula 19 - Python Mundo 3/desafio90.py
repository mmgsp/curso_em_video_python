boletim = {}

boletim["Nome"] = input("Nome: ")
boletim["Média"] = float(input(f"Média de {boletim["Nome"]}: "))

if boletim["Média"] >= 7:
    boletim["Situação"] = "Aprovado"
else:
    boletim["Situação"] = "Reprovado"

print()
for chave, valor in boletim.items():
    print(f"{chave}: {valor}")

