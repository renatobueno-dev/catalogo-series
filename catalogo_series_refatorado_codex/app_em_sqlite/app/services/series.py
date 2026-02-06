"""Service layer for series operations using SQLite persistence."""

from __future__ import annotations

from typing import List

from app.models import Serie
from app.repositories import get_series_by_title, insert_series, list_series


def list_series_service() -> List[dict]:
    """Return all series stored in SQLite."""

    return list_series()


def add_series(serie: Serie) -> dict:
    """Persist a new series to SQLite and return its data."""

    data = serie.model_dump()
    insert_series(data)
    return data


def get_series_by_title_service(title: str) -> dict | None:
    """Retrieve a series by title (case-insensitive) from SQLite storage."""

    return get_series_by_title(title)
