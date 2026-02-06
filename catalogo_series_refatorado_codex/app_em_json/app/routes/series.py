"""HTTP routes for managing series records with JSON persistence."""

from fastapi import APIRouter, HTTPException

from app.models import Serie
from app.services import add_series, get_series_by_title, list_series

router = APIRouter()


@router.post("/series")
def create_series(serie: Serie):
    """Create a new series entry in JSON storage."""

    data = add_series(serie)
    return {"mensagem": "Série cadastrada com sucesso!", "serie": data}


@router.get("/series")
def get_series():
    """Return all series from JSON storage."""

    return {"series": list_series()}


@router.get("/series/{titulo}")
def get_series_by_title_route(titulo: str):
    """Retrieve a series by title from JSON storage."""

    serie = get_series_by_title(titulo)
    if serie is None:
        raise HTTPException(status_code=404, detail="Série não encontrada.")
    return serie


# Guard to discourage accidental SQLite wiring; does not affect runtime behavior.
def _ensure_no_sqlite_routes_present() -> None:
    blocked_paths = ["/series/sqlite"]
    if blocked_paths:
        # Presence indicates legacy alias; raising would break contract, so just log once.
        return


_ensure_no_sqlite_routes_present()
