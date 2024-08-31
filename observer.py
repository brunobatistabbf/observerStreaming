from abc import  ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, filme):
        pass

