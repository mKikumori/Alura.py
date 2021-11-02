
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando a conta {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def saca(self, valor):
        if valor < self.__limite:
            self.__saldo -= valor
        elif valor > self.__limite:
            print("Estourou o limite")

    def deposita(self, valor):
        self.__saldo += valor
        
   def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
