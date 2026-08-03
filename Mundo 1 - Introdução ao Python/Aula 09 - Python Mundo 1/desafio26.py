# Lendo uma frase e contando a quantidade de "a" e em que posição aparece pela primeira e última vez na frase

frase = input('Digite uma frase: ')
print(f"""
A Letra 'a' aparece {frase.count('a')} vezes
A letra 'a' aparece pela primeira vez na posição {frase.strip().find('a')+1}
A letra 'a' aparece pela última vez na posição {frase.strip().rfind('a')+1}
      """)
