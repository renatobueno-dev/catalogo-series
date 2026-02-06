"""SQLite persistence helpers for series records."""

from __future__ import annotations

import sqlite3
from typing import List, Optional

from app.repositories.db import DB_PATH


def get_series_by_title(title: str) -> Optional[dict]:
    """Fetch a series by title (case-insensitive) from SQLite storage."""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT titulo, genero, ano_lancamento, temporadas FROM series WHERE LOWER(titulo) = LOWER(?)",
        (title,),
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "titulo": row[0],
            "genero": row[1],
            "ano_lancamento": row[2],
            "temporadas": row[3],
        }
    return None


def list_series() -> List[dict]:
    """Return all series stored in SQLite."""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, genero, ano_lancamento, temporadas FROM series")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "titulo": row[0],
            "genero": row[1],
            "ano_lancamento": row[2],
            "temporadas": row[3],
        }
        for row in rows
    ]


def insert_series(series_data: dict) -> None:
    """Insert a new series record into SQLite storage."""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO series (titulo, genero, ano_lancamento, temporadas) VALUES (?, ?, ?, ?)",
        (
            series_data["titulo"],
            series_data["genero"],
            series_data["ano_lancamento"],
            series_data["temporadas"],
        ),
    )
    conn.commit()
    conn.close()
