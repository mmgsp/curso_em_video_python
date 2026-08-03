import moeda

p = float(input("Digite o preço: R$"))

print(f"\nA metade de {moeda.moeda(p)} é: {moeda.metade(p,True)}\nO dobro de {moeda.moeda(p)} é: {moeda.dobro(p,True)}\nAumentando 10% temos: {moeda.aumentar(p,10,True)}\nDiminuindo 10% temos: {moeda.diminuir(p,10,True)}")
