"""Repository layer for JSON persistence."""

from __future__ import annotations

import importlib.util

if importlib.util.find_spec("app.repositories.db") or importlib.util.find_spec("app.repositories.series_sqlite"):
    raise RuntimeError("SQLite backend must not be present in the JSON app.")

from app.repositories.series_json import read_series, write_series

__all__ = ["read_series", "write_series"]
