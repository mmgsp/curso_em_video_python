from time import sleep

def contador(inicio,fim,passo):

    
    if inicio < fim and passo >= 0:

        print(f"\nContando de {inicio} até {fim} de {passo} em {passo}:\n")
        sleep(1.5)
        numero = inicio

        if passo == 0:
            passo = 1

        while numero < fim:
            print(numero, end=" ",flush=True)
            sleep(0.25)
            numero += passo
        print(numero)

    elif inicio > fim:

        print(f"\nContando de {inicio} até {fim} de {passo} em {passo}:\n")
        sleep(1.5)
        numero = inicio

        if passo < 0:
            passo *= -1

        while numero > fim:
            print(numero, end=" ",flush=True)
            sleep(0.25)
            numero -= passo

        print(numero)
    else:
        print("Comando Inválido")
        
contador(1,10,1)
contador(10,0,2)

inicio = int(input("\nContagem Personalizada:\n\nNúmero inicial: "))
fim = int(input("Número final: "))
passo = int(input("Passo: "))

contador(inicio,fim,passo)
