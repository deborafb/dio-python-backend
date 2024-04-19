class Conta:

    def __init__(self, saldo):            
        self.LIMITE_SAQUE = 500
        self.LIMITE_QTD_SAQUES = 3

        self.saldo = saldo
        self.saldo_inicial = saldo
        self.saques_realizados = 0
        self.viu_extrato = False
        self.extrato = ""

    def deposito(self, valor):
        if valor <= 0:
            print("Depósito inválido.")
        else:
            self.saldo += valor
            self.extrato += f"\nDepósito realizado no valor de R${valor} \n"
            print("Depósito realizado com sucesso!")

    def saque(self, valor):

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

    def get_extrato(self):
        return self.extrato, self.saldo_inicial, self.saldo

