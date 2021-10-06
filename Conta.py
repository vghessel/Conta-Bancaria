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

                                # GETTERS

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

                                # SETTERS
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

#Implementar Staticamethod