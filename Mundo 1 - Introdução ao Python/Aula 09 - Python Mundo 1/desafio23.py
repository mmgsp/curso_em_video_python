# Separando digitos de um numero

num = int(input('Digite um número (de 0 a 9999): '))

uni = num % 10
dez = (num % 100)//10
cen = (num % 1000)//100
mil = (num % 10000)//1000

print(f"""
milhar: {mil}
centena: {cen}
dezena: {dez}
unidade: {uni}""")
