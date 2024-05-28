from transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        realizar_saque = conta.sacar(self.valor)
        if realizar_saque:
            conta.historico.adicionar_transacao(self)
    
    @property
    def valor(self):
        return self._valor()
    