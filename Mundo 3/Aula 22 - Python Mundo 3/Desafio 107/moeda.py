def aumentar(moeda,porcentagem):
    moeda += moeda*(porcentagem/100)
    return moeda

def diminuir(moeda,porcentagem):
    moeda -= moeda*(porcentagem/100)
    return moeda

def dobro(moeda):
    moeda *= 2
    return moeda

def metade(moeda):
    moeda /= 2
    return moeda


