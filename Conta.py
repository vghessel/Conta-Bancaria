class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def Extrato(self):
        print("Seu saldo é {}, {}".format(self.__saldo, self.__titular))

    def Depositar(self, valor):
        self.__saldo += valor     #self.__saldo = self.__saldo + valor

    def Sacar(self, valor):
        self.__saldo -= valor    #self.__saldo = self.__saldo - valor

    def Transferir(self,valor,destino):
        self.Sacar(valor)               # Exemplo: conta2.Transferir(10.0, conta1)
        destino.Depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite