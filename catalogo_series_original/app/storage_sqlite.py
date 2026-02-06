import sqlite3

def get_series_by_title(title: str):
    conn = sqlite3.connect("data/series.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT titulo, genero, ano_lancamento, temporadas FROM series WHERE LOWER(titulo) = LOWER(?)",
        (title,),
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"titulo": row[0], "genero": row[1], "ano_lancamento": row[2], "temporadas": row[3]}
    return None

def post_series(series_data: dict):
    conn = sqlite3.connect("data/series.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO series (titulo, genero, ano_lancamento, temporadas) VALUES (?, ?, ?, ?)",
        (series_data["titulo"], series_data["genero"], series_data["ano_lancamento"], series_data["temporadas"]),
    )
    conn.commit()
    conn.close()