# Mostrando um nome em maiúsculas, minúsculas, quantidade de letras do nome todo/só o primeiro nome

nome = input('Digite um nome: ')

print(f"""
Nome maiúsculo: {nome.upper().strip()}
Nome minúsculo: {nome.lower().strip()}
Quantidade  de letras do nome completo: {len(nome.replace(' ',''))}
Quantidade de letras do primeiro nome: {len(nome.split()[0])}
""")
