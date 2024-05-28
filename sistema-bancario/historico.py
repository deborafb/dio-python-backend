class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append( 
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor
            }
        )
    
    @property        
    def transacoes(self):
        return self._transacoes