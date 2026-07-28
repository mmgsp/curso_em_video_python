import moeda

p = float(input("Digite o preço: R$"))

print(f"\nA metade de R${p:.2f} é: R${moeda.metade(p):.2f}\nO dobro de R${p:.2f} é: R${moeda.dobro(p):.2f}\nAumentando 10% temos: R${moeda.aumentar(p,10):.2f}\nDiminuindo 10% temos: R${moeda.diminuir(p,10):.2f}")
