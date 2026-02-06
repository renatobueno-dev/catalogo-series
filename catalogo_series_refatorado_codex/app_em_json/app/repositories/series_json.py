"""JSON-based persistence helpers for the series catalog."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Sequence


DATA_FILE = Path("data/series.json")


def read_series() -> List[dict]:
    """Return the list of series stored in ``data/series.json``.

    Falls back to an empty list when the file is missing, unreadable,
    or does not contain a JSON list.
    """

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def write_series(series_list: Sequence[dict]) -> None:
    """Persist the given series list to ``data/series.json``.

    On write errors, the function logs to stdout and leaves existing data untouched.
    """

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(list(series_list), file, ensure_ascii=False, indent=4)
    except OSError as exc:
        print(f"Erro ao escrever no arquivo: {exc}")
