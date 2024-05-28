from cliente import Cliente

class PessoaFisica(Cliente):

    def __init__(self, nome, data_nascimento, cpf, endereco):            
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        super().__init__(endereco)
    
    @property
    def pessoa(self):
        return {"cpf": self._cpf,
                "nome": self._nome,
                "data_nascimento": self._data_nascimento,
                "endereço": self._endereco                
                }
       