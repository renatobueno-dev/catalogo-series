"""Service layer for series operations using JSON persistence."""

from __future__ import annotations

from typing import List, Sequence

from app.models import Serie
from app.repositories import read_series, write_series


def list_series() -> List[dict]:
    """Return all series stored in JSON."""

    return read_series()


def add_series(serie: Serie) -> dict:
    """Persist a new series to JSON and return its data."""

    series_list = read_series()
    data = serie.model_dump()
    series_list.append(data)
    write_series(series_list)
    return data


def get_series_by_title(title: str) -> dict | None:
    """Retrieve a series by title (case-insensitive) from JSON storage."""

    for serie in read_series():
        if serie.get("titulo", "").lower() == title.lower():
            return serie
    return None
