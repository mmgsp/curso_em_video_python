# Somando n números inteiros 

n = 0
soma = 0

while n != 999:
    
    n = int(input('Digite um número: '))
    
    if n != 999:
        
        soma += n
        
print(f'A soma total foi: {soma}')