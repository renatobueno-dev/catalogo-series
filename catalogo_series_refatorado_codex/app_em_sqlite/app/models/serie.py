"""Data models for the SQLite-based series catalog."""

from pydantic import BaseModel, Field


class Serie(BaseModel):
    """Represents a TV series with validation for year and season count."""

    titulo: str
    genero: str
    ano_lancamento: int = Field(..., gt=1900)
    temporadas: int = Field(..., gt=0)
