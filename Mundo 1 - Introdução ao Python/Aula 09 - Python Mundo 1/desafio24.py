# Nome da cidade começa com Santo ou não?

cidade = input('Digite o nome de uma cidade: ')
print(f'\nO nome da cidade começa com Santo? (True ou False): {cidade.strip().upper().split()[0] == 'SANTO'}\n')
