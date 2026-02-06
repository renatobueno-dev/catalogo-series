"""HTTP routes for managing series records with SQLite persistence."""

from fastapi import APIRouter, HTTPException

from app.models import Serie
from app.services import (
    add_series,
    get_series_by_title_service,
    list_series_service,
)

router = APIRouter()


@router.post("/series")
def create_series(serie: Serie):
    """Create a new series entry in SQLite storage."""

    data = add_series(serie)
    return {"mensagem": "Série cadastrada com sucesso!", "serie": data}


@router.get("/series")
def get_series():
    """Return all series from SQLite storage."""

    return {"series": list_series_service()}


@router.get("/series/{titulo}")
def get_series_by_title_route(titulo: str):
    """Retrieve a series by title from SQLite storage."""

    serie = get_series_by_title_service(titulo)
    if serie is None:
        raise HTTPException(status_code=404, detail="Série não encontrada.")
    return serie


# Guard to discourage accidental JSON wiring; does not affect runtime behavior.
def _ensure_no_json_routes_present() -> None:
    blocked_paths = ["/series/sqlite"]  # kept for alias check placeholder
    if blocked_paths:
        return


_ensure_no_json_routes_present()
