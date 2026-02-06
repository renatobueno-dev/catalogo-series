from fastapi import APIRouter, HTTPException
from app.models import Serie
from app.storage import read_series, write_series
from app.storage_sqlite import get_series_by_title as fetch_series, post_series


router = APIRouter()


@router.post("/series")
def create_series(serie: Serie):
    series_list = read_series()
    series_list.append(serie.model_dump())
    write_series(series_list)
    return {"mensagem": "Série cadastrada com sucesso!", "serie": serie.model_dump()}


@router.get("/series")
def get_series():
    series_list = read_series()
    return {"series": series_list}

@router.post("/series/sqlite")
def create_series_sqlite(serie: Serie):
    post_series(serie.model_dump())
    return {"mensagem": "Série cadastrada com sucesso!", "serie": serie.model_dump()}

@router.get("/series/{titulo}")
def get_series_by_title(titulo: str):
    serie = fetch_series(titulo)
    if serie is None:
        raise HTTPException(status_code=404, detail="Série não encontrada.")
    return serie
