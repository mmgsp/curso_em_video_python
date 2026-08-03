# Aprovando ou negando empéstimo bancário para compra de uma casa

casa = float(input('Digite o valor total da casa (em R$): '))
salario = float(input('Digite o valor de seu salário (em R$): '))
anos = int(input('Digite a quantidade de anos em que pretende pagar a casa: '))

valor = casa/(anos*12)

if valor > salario*0.3:
    print(f'\nO empréstimo foi negado!\nO valor da parcela ({valor:.2f}) excede o limite de 30% de seu salário ({salario*0.3:.2f})\n')
else:
    print(f'\nO empréstimo foi aprovado!\nO valor da parcela ({valor:.2f}) não excede o limite de 30% de seu salário ({salario*0.3:.2f})\n')
