"""FastAPI application setup for the JSON persistence catalog."""

from fastapi import FastAPI

from app.routes import router as series_router

app = FastAPI()
app.include_router(series_router)


@app.get("/")
def read_root():
    """Healthcheck endpoint returning a welcome message."""

    return {"mensagem": "Bem vindo ao Catálogo de Séries."}
