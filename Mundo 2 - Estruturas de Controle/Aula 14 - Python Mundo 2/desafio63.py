# N primeiros números de fibonacci usando while

anterior = 0
atual = 1
contador = 0
elementos = []

n = int(input('Quantos elementos de fibonacci você quer ver? '))

if n == 1:
    elementos.append(anterior)
    
elif n == 2:
    elementos.append(anterior)
    elementos.append(atual)
    
elif n > 2:
    
    while contador < n-2:
        
        if contador == 0:
            elementos.append(anterior)
            elementos.append(atual)

        proximo = anterior + atual
        elementos.append(proximo)
        
        temp = atual
        anterior = temp
        atual = proximo
        
        contador += 1

print(elementos)