class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente.")
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        valor_total = valor + taxa
        if self.saldo >= valor_total:
            self.saldo -= valor_total
            return True
        else:
            print("Saldo insuficiente.")
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite=0):
        super().__init__(titular, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente.")
            return False

conta_poupanca = ContaPoupanca("João")
conta_poupanca.depositar(100)
print("Saldo da Conta Poupança:", conta_poupanca.saldo)
conta_poupanca.sacar(50)
print("Saldo após saque:", conta_poupanca.saldo)

conta_corrente = ContaCorrente("Maria", saldo=100, limite=50)
print("Saldo da Conta Corrente:", conta_corrente.saldo)
conta_corrente.sacar(120)
print("Saldo após saque:", conta_corrente.saldo)

