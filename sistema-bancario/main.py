import conta, usuario

usuarios = []

def checar_usuario(cpf):
    return cpf in usuarios

def criar_usuario(*, nome, data, cpf, endereco):
    if checar_usuario(cpf):
        print ("\nUsuário já cadastrado.")
    else:
        usuario.Usuario(nome=nome, data_nascimento=data, cpf=cpf, endereco=endereco)
        usuarios.append(cpf)
        print ("\nUsuário cadastrado com sucesso!")

def criar_conta(cpf, saldo=0):
    if checar_usuario(cpf):
        conta.Conta(saldo, cpf)
        print("\nOpção escolhida: Nova conta \n\nConta criada com sucesso!")
    else:
        print("\nOpção escolhida: Nova conta \n\nUsuário não cadastrado.")
