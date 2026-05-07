from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService


class FilmeController:

    def __init__(self):
        self.repository = FilmeRepository()
        self.service = FilmeService()

        self.repository.criar_tabela()

    def cadastrar_filme(self, titulo, duracao, genero, classificacao, diretor):

        filme = self.service.validar_dados(
            titulo,
            duracao,
            genero,
            classificacao,
            diretor
        )

        self.repository.salvar(filme)

    def listar_filmes(self):
        return self.repository.listar()