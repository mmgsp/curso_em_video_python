def aumentar(moeda=0,porcentagem=0):
    moeda += moeda*(porcentagem/100)
    return moeda

def diminuir(moeda=0,porcentagem=0):
    moeda -= moeda*(porcentagem/100)
    return moeda

def dobro(moeda=0):
    moeda *= 2
    return moeda

def metade(moeda=0):
    moeda /= 2
    return moeda

def moeda(moeda=0,tipo='R$'):

    return f"{tipo}{moeda:.2f}".replace('.',",")
