class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1
    
    def resumo(self):
        return f"{self.nome} tem {self.idade} anos."

p1 = Pessoa()
p1.nome = "Gabriel"
p1.idade = 23

pessoa_vazio = Pessoa()

print(p1.resumo())
print(pessoa_vazio.resumo())

p1.aniversario()

print(p1.resumo())
