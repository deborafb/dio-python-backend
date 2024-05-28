import itertools
from historico import Historico

class Conta:

    id = itertools.count()

    def __init__(self, cliente):            
        self._saldo = 0        
        self._numero = next(self.id)
        self._agencia = "0001"
        self._cliente = cliente 
        self._historico = Historico()
        self.LIMITE_SAQUE = 500
        self.LIMITE_QTD_SAQUES = 3        
        self.saques_realizados = 0

    @classmethod
    def nova_conta(cls, cliente):
        return cls(cliente)

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito inválido.")
        else:
            self._saldo += valor
            self._historico.adicionar_transacao()
            
            f"\nDepósito realizado no valor de R${valor} \n"
            print("Depósito realizado com sucesso!")

            return True
        
        return False

    def sacar(self, valor):

        excede_qtd_saques = self.saques_realizados == self.LIMITE_QTD_SAQUES
        excede_valor_saque = valor > self.LIMITE_SAQUE
        excede_saldo = valor > self.saldo 

        if excede_qtd_saques:
            print("Quantidade de saques diários excedida.")
        elif excede_valor_saque:
            print("Valor de saque inválido. Limite de saque: R$500")
        elif excede_saldo:
            print("Saldo insuficiente. Saque não realizado.")

        else:                 
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato += f"\nSaque realizado no valor de R${valor} \n"
            print("Saque realizado com sucesso!")   
             
            return True
        
        return False


    @property
    def conta(self):
        return {"saldo": self._saldo,
                "numero": self._numero,
                "agencia": self._agencia,
                "cliente": self._cliente,
                "historico": self._historico                
                }
    