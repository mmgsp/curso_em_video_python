def fatorial (num,show=False):

    f = 1
    for c in range(num,0,-1):
        f *= c

    if not show:
        return f
    else:
        str_return = ' x '.join(str(n) for n in range(num,0,-1))
        return f'{str_return} = {f}'
    
print(fatorial(7))
print(fatorial(7,True))
