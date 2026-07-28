import moeda

p = float(input("Digite o preço: R$"))

print(f"\nA metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))}\nO dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}\nAumentando 10% temos: {moeda.moeda(moeda.aumentar(p,10))}\nDiminuindo 10% temos: {moeda.moeda(moeda.diminuir(p,10))}")
