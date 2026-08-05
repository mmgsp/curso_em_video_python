class contaBancaria:
    """
Cria uma conta bancária, permitindo fazer saques e depósitos
    """

    def __init__(self,id,nome,saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = float(saldo)

    def saque(self):
        if self.saldo == 0:
            print("Impossível sacar, saldo zerado...")
        else:
            valor_saque = float(input(f"SAQUE MÁXIMO: R$ {self.saldo:.2f}\nDIGITE O VALOR DO SEU SAQUE: R$ "))
            if valor_saque > self.saldo:
                print("\nSAQUE INVÁLIDO, TENTE NOVAMENTE\n")
                return self.saque()
            else:
                self.saldo -= valor_saque
                print(f"\nOPERAÇÃO REALIZADA COM SUCESSO / NOVO SALDO: R$ {self.saldo:.2f}")
                
    def deposito(self):
        valor_deposito = float(input("DIGITE O VALOR DO SEU DEPÓSITO: R$ "))
        if valor_deposito <= 0:
            print("\nDEPÓSITO INVÁLIDO, TENTE NOVAMENTE\n")
            return self.deposito()
        else:
            self.saldo += valor_deposito
            print(f"\nOPERAÇÃO REALIZADA COM SUCESSO / NOVO SALDO: R$ {self.saldo:,.2f}")


    def __str__(self):
        return f"A CONTA {self.id} DE {self.titular} TEM R$ {self.saldo:,.2f} DE SALDO"

conta = contaBancaria(123,"Gabriel",4000)
conta.deposito()
print(conta)
    