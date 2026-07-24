def maior(*numeros):

    qtde_valores = len(numeros)
    maior_numero = max(numeros)
    print(f"Foram informados {qtde_valores} valores: ")

    for valor in numeros:
        print(valor,end=" ")

    print(f"\nSendo o maior deles o número {maior_numero}")

maior(1,4,5,6,10,76)
print()
maior(2,9,4,5,7,1)
