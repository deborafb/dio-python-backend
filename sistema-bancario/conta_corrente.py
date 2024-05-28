from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente):
        super().__init__(cliente)      

    def sacar(self, valor):
        
        return super().sacar(valor)

    def __str__(self):
        return super().conta()