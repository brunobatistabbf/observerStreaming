from patoFlix import PatoFlix
from usuarioConcreto import UsuarioConcreto
from filme import Filme


if __name__ == '__main__':
    plataforma = PatoFlix()

    usuario1 = UsuarioConcreto("Ana Ribeiro",["Ação", "Romance"])
    usuario2 = UsuarioConcreto("Lucas Silva", ["Comédia", "Terror"])
    usuario3 = UsuarioConcreto("Andre Bona", ["Ação", "Comédia"])
    usuario4 = UsuarioConcreto("Fernanda Ferraz", ["Terror", "Anime"])
    usuario5 = UsuarioConcreto("Bruno Daniel", ["Anime", "Ação"])

    plataforma.inscrever(usuario1)
    plataforma.inscrever(usuario2)
    plataforma.inscrever(usuario3)
    plataforma.inscrever(usuario4)
    plataforma.inscrever(usuario5)

    filme1 = Filme("007: O ultimo tiro", "Ação")
    filme2 = Filme("Exorcistas Aposentados", "Terror")
    filme3 = Filme("One Piece 2", "Anime")
    filme4 = Filme("Blade Runner: Agora a história é outra", "Ficção")
    filme5 = Filme("Beijocas e Tals", "Romance")

    plataforma.adicionar_filme(filme1)
    plataforma.adicionar_filme(filme2)
    plataforma.adicionar_filme(filme3)
    plataforma.adicionar_filme(filme4)
    plataforma.adicionar_filme(filme5)