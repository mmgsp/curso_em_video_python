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

def linha(caractere):
    return f"{caractere*46}"

def resumo(preço, aumento, declínio):
    preço_aumentado = aumentar(preço,aumento,True)
    preço_diminuido = diminuir(preço,declínio,True)
    preço_metade = metade(preço,True)
    preço_dobro = dobro(preço,True)

    print(f"{linha('-')}\n{'RESUMO DO VALOR':^46}\n{linha('-')}")
    print(f"{"Preço analisado"}{moeda(preço):>31}\n{f'{aumento}% de aumento'}{preço_aumentado:>32}\n{f'{declínio}% de redução'}{preço_diminuido:>32}\n{'Metade do preço'}{preço_metade:>31}\n{'Dobro do preço'}{preço_dobro:>32}")

