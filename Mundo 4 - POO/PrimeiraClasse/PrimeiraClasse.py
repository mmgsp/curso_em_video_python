class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
    
    def resumo(self):
        return f"{self.nome} tem {self.idade} anos."

p1 = Pessoa("Gabriel", 23)

pessoa_vazio = Pessoa()

print(p1.resumo())
print(pessoa_vazio.resumo())

p1.aniversario()

print(p1.resumo())
