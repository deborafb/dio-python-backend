import itertools

class Conta:

    id = itertools.count()

    def __init__(self, saldo, usuario_cpf):            
        self.saldo = saldo        
        self.numero_conta = next(self.id)
        self.usuario = usuario_cpf 

        self.agencia = "0001"
        self.LIMITE_SAQUE = 500
        self.LIMITE_QTD_SAQUES = 3        
        self.saldo_inicial = saldo
        self.saques_realizados = 0
        self.extrato = ""

    def depositar(self, valor, /):
        if valor <= 0:
            print("Depósito inválido.")
        else:
            self.saldo += valor
            self.extrato += f"\nDepósito realizado no valor de R${valor} \n"
            print("Depósito realizado com sucesso!")

    def sacar(self, *, valor):

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

    def visualizar_extrato(self):
        return self.extrato, self.saldo_inicial, self.saldo
    
    def get_conta(self):
        return self.usuario, self.numero_conta, self.agencia

