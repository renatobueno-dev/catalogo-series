"""Repository layer for the SQLite persistence app."""

from __future__ import annotations

import importlib.util

if importlib.util.find_spec("app.repositories.series_json"):
    raise RuntimeError("JSON backend must not be present in the SQLite app.")

from app.repositories.db import DB_PATH, initialize_database
from app.repositories.series_sqlite import get_series_by_title, insert_series, list_series

__all__ = [
    "DB_PATH",
    "initialize_database",
    "get_series_by_title",
    "insert_series",
    "list_series",
]
