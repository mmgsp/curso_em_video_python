def escreva(mensagem):
    tamanho = len(mensagem) + 4

    print("~"*tamanho)
    print(f"{mensagem:^{tamanho}}")
    print("~"*tamanho)

mensagem = input("Digite sua mensagem: ")
print()
escreva(mensagem)
