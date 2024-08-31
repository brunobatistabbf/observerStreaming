from observer import Observador

class PatoFlix:
    def __init__(self):
        self.observadores = []
        self.filmes = []

    def inscrever(self, observador: Observador):
        self.observadores.append(observador)

    def cancelar(self, observador: Observador):
        self.observadores.remove(observador)

    def notificar(self, filme):
        for observador in self.observadores:
            if filme.genero in observador.generos:
                observador.atualizar(filme)

    def adicionar_filme(self, filme):
        self.filmes.append(filme)
        self.notificar(filme)
