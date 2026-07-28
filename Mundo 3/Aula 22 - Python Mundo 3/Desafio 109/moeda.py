def moeda(preço=0,tipo='R$'):

    return f"{tipo}{preço:.2f}".replace('.',",")

def aumentar(preço=0,porcentagem=0,format=False):
    preço_aumentado = preço
    preço_aumentado += preço*(porcentagem/100)
    if format == False:
        return preço_aumentado
    else:
        return moeda(preço_aumentado)

def diminuir(preço=0,porcentagem=0,format=False):
    preço_diminuido = preço
    preço_diminuido -= preço*(porcentagem/100)
    if format == False:
        return preço_diminuido
    else:
        return moeda(preço_diminuido)

def dobro(preço=0,format=False):
    preço_dobrado = preço
    preço_dobrado *= 2
    if format == False:
        return preço_dobrado
    else:
        return moeda(preço_dobrado)

def metade(preço,format=False):
    preço_metade = preço
    preço_metade /= 2
    if format == False:
        return preço_metade
    else:
        return moeda(preço_metade)

