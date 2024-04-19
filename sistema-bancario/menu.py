import conta

saldo = float(input("Digite o saldo da conta: R$"))

conta_atual = conta.Conta(saldo)

menu = """

[1] Deposito
[2] Extrato
[3] Saque
[4] Sair

Digite uma opção: 
"""

while True:

    opcao = input(menu)

    match opcao:

        case "1":
            print("\nOpção escolhida: Depósito \n\nDigite o valor: ")
            valor = int(input())
            conta_atual.deposito(valor)

        case "2":
            print("\nOpção escolhida: Extrato")            
            extrato, saldo_inicial, saldo_atual = conta_atual.get_extrato()

            print(f"\n-------------- EXTRATO --------------\n\nSaldo anterior: R${saldo_inicial:.2f}")
            print(extrato)
            print(f"Saldo atual: R${saldo_atual:.2f} \n-------------------------------------")          

        case "3":
            print("\nOpção escolhida: Saque \n\nDigite o valor: ")
            valor = int(input())
            conta_atual.saque(valor)

        case "4":
            print("\nOpção escolhida: Sair")
            break

        case default:    
            print("\nOpção inválida.")

