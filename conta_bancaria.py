class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self.__saldo

# Criando uma instância da classe ContaBancaria
minha_conta = ContaBancaria("João",1000)

# Realizando operações na conta
minha_conta.depositar(500)
minha_conta.sacar(2000)

# Obtendo o saldo através do método público
print("Saldo atual:", minha_conta.get_saldo())
