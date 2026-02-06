"""Service layer for the SQLite persistence app."""

from app.services.series import (
    add_series,
    get_series_by_title_service,
    list_series_service,
)

__all__ = ["add_series", "get_series_by_title_service", "list_series_service"]
