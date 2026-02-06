"""FastAPI application setup for the SQLite persistence catalog."""

from fastapi import FastAPI

from app.repositories import initialize_database
from app.routes import router as series_router

initialize_database()

app = FastAPI()
app.include_router(series_router)


@app.get("/")
def read_root():
    """Healthcheck endpoint returning a welcome message."""

    return {"mensagem": "Bem vindo ao Catálogo de Séries."}
