def area(largura,comprimento):
    a = largura * comprimento
    print(f"\nA área do terreno {largura:.2f}x{comprimento:.2f} é igual a {a:.2f} m²")

largura = float(input("CALCULADOR DE ÁREA\n\nDigite a largura do terreno (m): "))
comprimento = float(input("Digite o comprimento do terreno (m): "))

area(largura,comprimento)
