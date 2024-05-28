from abc import ABC, abstractmethod

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass

    @abstractmethod
    def valor(self):
        pass
