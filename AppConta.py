class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo
        print(f"Meu saldo é: {saldo} reais\n")

    def Depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de {valor} reais efetuado com sucesso.")
        print(f"Saldo Atual: {self._saldo} reais\n")

    def Sacar(self, valor):
        if self._saldo < valor:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de {valor} reais efetuado com sucesso.")
            print(f"Saldo Atual: {self._saldo} reais\n")


print("CONTA DO BANCO\n")

conta = Conta(100)

conta.Depositar(100)

conta.Sacar(50)

conta.Depositar(800)

conta.Sacar(949)

conta.Sacar(1)
