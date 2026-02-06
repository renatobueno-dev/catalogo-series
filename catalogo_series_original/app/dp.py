import sqlite3


def initialize_database():
    conn = sqlite3.connect("data/series.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS series (
            titulo TEXT PRIMARY KEY,
            genero TEXT NOT NULL,
            ano_lancamento INTEGER NOT NULL,
            temporadas INTEGER NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()
