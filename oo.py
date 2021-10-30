class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando a conta {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def saca(self, valor):
        if valor < self.limite:
            self.saldo -= valor
        elif valor > self.limite:
            print("Estourou o limite")

    def deposita(self, valor):
        self.saldo += valor
