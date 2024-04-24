class Usuario:

    def __init__(self, nome, data_nascimento, cpf, endereco):            
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
    
    def get_usuario(self):
        return {"cpf": self.cpf,
                "nome": self.nome,
                "data_nascimento": self.data_nascimento,                
                "endereco": self.endereco }
       