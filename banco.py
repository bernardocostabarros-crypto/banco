class Conta:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.saldo = saldo
        self.senha = senha
   
    def nome_titular(self, nome):
        self.titular = nome
       
    def definir_senha(self, senha):
        self.senha = senha
       
    def retirar_saldo(self, vsaque):
        if self.saldo >= vsaque:
            self.saldo -= vsaque
            print(f"Saque de R$ {vsaque} realizado!")
        else:
            print("Saldo insuficiente!")

conta = Conta("Márcio", 500, 1234)

conta.retirar_saldo(10)

print(f"Saldo da {conta.titular}: R${conta.saldo}")
