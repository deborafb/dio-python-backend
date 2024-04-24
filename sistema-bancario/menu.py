import conta, main

conta_atual = conta.Conta(5000, "123456789")

menu = """

-------------- MENU --------------

[1] Novo cliente
[2] Nova conta
[3] Deposito
[4] Extrato
[5] Saque
[6] Sair


Digite uma opção: 
"""

while True:

    opcao = input(menu)

    match opcao:

        case "1":

            print("\nOpção escolhida: Novo cliente \n\nDigite o nome: ") 
            nome = input()
            print("\nDigite a data de nascimento: ")
            data = input()
            print("\nDigite o cpf: ")
            cpf = input()
            print("\nDigite o endereço: ")
            endereco = input()

            main.criar_usuario(nome=nome, data=data, cpf=cpf, endereco=endereco)            

        case "2":

            print("\n\nDigite o cpf: ")
            cpf = input()
            main.criar_conta(cpf)

        case "3":
            print("\nOpção escolhida: Depósito \n\nDigite o valor: ")
            entrada = int(input())
            conta_atual.depositar(entrada)

        case "4":
            print("\nOpção escolhida: Extrato")            
            extrato, saldo_inicial, saldo_atual = conta_atual.visualizar_extrato()

            print(f"\n-------------- EXTRATO --------------\n\nSaldo anterior: R${saldo_inicial:.2f}")
            print(extrato)
            print(f"Saldo atual: R${saldo_atual:.2f} \n-------------------------------------")          

        case "5":
            print("\nOpção escolhida: Saque \n\nDigite o valor: ")
            entrada = int(input())
            conta_atual.sacar(valor = entrada)

        case "6":
            print("\nOpção escolhida: Sair")
            break

        case default:    
            print("\nOpção inválida.")
