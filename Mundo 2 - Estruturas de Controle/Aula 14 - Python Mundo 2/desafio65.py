# Média e maior/menor de vários números lidos

# Inicializando variáveis de controle

contador = 0
soma = 0
continuar = ''

# Implementando while

while continuar != 'N':
    
    numero = float(input('\nDigite um número: '))
    
    # Avaliando maior/menor
    
    if contador == 0:
        
        maior = menor = numero
        
    elif numero > maior:
        
        maior = numero
        
    elif numero < menor:
        
        menor = numero
    
    # Incrementando contador e soma após entrada 
    
    contador += 1
    soma += numero
    
    # Implementando 'continuar?' e validando entrada de dados
    
    continuar = input('Deseja continuar? [S/N] ').upper().strip()
    
    if continuar != 'S' and continuar != 'N':
        
        while continuar != 'S' and continuar != 'N':
            
            continuar = input('\nComando Inválido...\nDeseja continuar? [S/N] ').upper().strip()

# Mostrando resultados na tela após finalização do laço de repetição

print(f'\nMaior valor lido: {maior}\nMenor valor lido: {menor}\nMédia total: {soma/contador:.1f}')
