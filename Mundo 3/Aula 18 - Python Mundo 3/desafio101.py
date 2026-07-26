from datetime import datetime

def voto(nascimento):

    ano_atual = datetime.today().year
    
    idade = ano_atual - nascimento


    if idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO NEGADO'

ano_nascimento = int(input("Em que ano você nasceu? "))

situacao_voto = voto(ano_nascimento)

print(situacao_voto)






