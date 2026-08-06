class Funcionario:
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.aposentadoria = False

    def aposentar(self):
        if not self.aposentadoria:
            self.cargo = None
            self.setor = None
            self.aposentadoria = True
        else:
            print(f"Funcionário {self.nome} já está aposentado!")

    def apresentacao(self):
        if self.aposentadoria == False:
            return f"O funcionário {self.nome} trabalha como {self.cargo} no setor de {self.setor}."
        else:
            return f"O funcionário {self.nome} está aposentado."

f1 = Funcionario("Gabriel", "RH", "Analista de Contrato")
print(f1.apresentacao())
print(f1.__getstate__())


f1.aposentar()
print(f1.apresentacao())

f1.aposentar()
print(f1.__getstate__())


