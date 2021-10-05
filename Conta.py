class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def Extrato(self):
        print("Seu saldo é {}, {}".format(self.saldo, self.titular))

    def Depositar(self, valor):
        self.saldo += valor     #self.saldo = self.saldo + valor

    def Sacar(self, valor):
        self.saldo -= valor    #self.saldo = self.saldo - valor

    def Transferir(self,valor,destino):
        self.Sacar(valor)               # Exemplo: conta2.Transferir(10.0, conta1)
        destino.Depositar(valor)
