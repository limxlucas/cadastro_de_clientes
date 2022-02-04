class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
        
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Valor adicionado")
        else:
            print("Erro no depósito.")
    
    
    def sacar(self, valor):
        if valor > 0 and valor - self.saldo:
            self.saldo -= valor
            print("Valor sacado.")
        else:
            print("Erro no saque.")
            
            
    def consultar_saldo(self):
        print(f"Saldo atual: {self.saldo}")
