from controller.filme_controller import FilmeController


class FilmeView:

    def __init__(self):
        self.controller = FilmeController()

    def menu(self):

        while True:
            print("\n=== SISTEMA DE CINEMA ===")
            print("1 - Cadastrar Filme")
            print("2 - Listar Filmes")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_filme()

            elif opcao == "2":
                self.listar_filmes()

            elif opcao == "0":
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida")

    def cadastrar_filme(self):

        try:
            titulo = input("Título: ")
            duracao = input("Duração (min): ")
            genero = input("Gênero: ")
            classificacao = input("Classificação indicativa: ")
            diretor = input("Diretor: ")

            self.controller.cadastrar_filme(
                titulo,
                duracao,
                genero,
                classificacao,
                diretor
            )

            print("Filme cadastrado com sucesso!")

        except Exception as e:
            print(f"Erro: {e}")

    def listar_filmes(self):

        filmes = self.controller.listar_filmes()

        print("\n=== FILMES CADASTRADOS ===")

        for filme in filmes:
            print(f"\nID: {filme[0]}")
            print(f"Título: {filme[1]}")
            print(f"Duração: {filme[2]} min")
            print(f"Gênero: {filme[3]}")
            print(f"Classificação: {filme[4]}")
            print(f"Diretor: {filme[5]}")