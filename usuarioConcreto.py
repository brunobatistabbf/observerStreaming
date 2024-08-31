from observer import Observador

class UsuarioConcreto(Observador):
    def __init__(self, nome, generos):
        self.nome = nome
        self.generos = generos

    def atualizar(self, filme):
        print()
        print(f"Hey {self.nome}, {filme.titulo} está no Catalogo da Pato Flix!!!")
