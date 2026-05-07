from model.filme import Filme


class FilmeService:

    def validar_dados(self, titulo, duracao, genero, classificacao, diretor):

        if not titulo.strip():
            raise ValueError("Título inválido")

        if int(duracao) <= 0:
            raise ValueError("Duração inválida")

        if not genero.strip():
            raise ValueError("Gênero inválido")

        if not diretor.strip():
            raise ValueError("Diretor inválido")

        return Filme(
            titulo,
            int(duracao),
            genero,
            classificacao,
            diretor
        )