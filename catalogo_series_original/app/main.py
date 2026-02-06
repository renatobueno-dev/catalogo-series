from fastapi import FastAPI
from app.routes.series import router as series_router
from app.dp import initialize_database

initialize_database()

app = FastAPI()
app.include_router(series_router)

@app.get("/")
def read_root():
    return {"mensagem": "Bem vindo ao Catálogo de Séries."}
