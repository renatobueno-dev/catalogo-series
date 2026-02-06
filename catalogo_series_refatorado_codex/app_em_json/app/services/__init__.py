"""Service layer for the JSON persistence app."""

from app.services.series import add_series, get_series_by_title, list_series

__all__ = ["add_series", "get_series_by_title", "list_series"]
