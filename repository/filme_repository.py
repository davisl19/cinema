from database.connection import get_connection


class FilmeRepository:

    def criar_tabela(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                duracao INTEGER NOT NULL,
                genero TEXT NOT NULL,
                classificacao TEXT NOT NULL,
                diretor TEXT NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    def salvar(self, filme):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO filmes
            (titulo, duracao, genero, classificacao, diretor)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            filme.titulo,
            filme.duracao,
            filme.genero,
            filme.classificacao,
            filme.diretor
        ))

        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM filmes")
        filmes = cursor.fetchall()

        conn.close()
        return filmes