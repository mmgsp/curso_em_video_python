# Avaliando parênteses em expressões matemáticas

cursor = aberto = fechado = 0
parenteses = []

exp = str(input('Digite uma expressão: ')).strip()

for c in range (0,len(exp)):

    if exp[c] == '(' or exp[c] == ')': 
        parenteses.append(exp[c])

while cursor != len(parenteses):

    if parenteses[cursor] == '(':

        aberto += 1

        for c in range (cursor, len(parenteses)):

            if parenteses[c] == ')':

                fechado += 1
                del parenteses[c]
                break

    cursor+= 1

if aberto == fechado and ')' not in parenteses: print(f'Expressão correta')

else: print(f'Expressão incorreta')

