# Organizado valores de uma tupla em formato tabular 

arquivo = ('Arroz', '25.90', 'Feijão', '8.49', 'Macarrão', '4.99', 'Óleo de Soja', '7.89', 'Açúcar', '4.59', 'Café', '14.90', 'Leite', '5.29', 'Farinha de Trigo', '6.19', 'Sal', '2.39', 'Biscoito', '3.79')

print(f'{' TABELA DE PREÇOS ':=^50}')

for c in range(0,len(arquivo),2):

    print(arquivo[c], end = '')

    print('.'*(50-(len(arquivo[c+1])+3)-len(arquivo[c])), end = '')
    
    print(f'R$ {arquivo[c+1]}\n')
