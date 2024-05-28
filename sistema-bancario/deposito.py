from transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        realizar_deposito = conta.depositar(self.valor)
        if realizar_deposito:
            conta.historico.adicionar_transacao(self)
    
    @property
    def valor(self):
        return self._valor()
    

