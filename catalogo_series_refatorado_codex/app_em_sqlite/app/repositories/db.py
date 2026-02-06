"""Database bootstrap utilities for the SQLite persistence app."""

import sqlite3

DB_PATH = "data/series.db"


def initialize_database() -> None:
    """Ensure the SQLite database file exists with the required schema."""

    conn = sqlite3.connect(DB_PATH)
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
