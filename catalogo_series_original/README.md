# Catálogo de Séries - Versão Original

API de catálogo de séries desenvolvida com FastAPI, suportando persistência em JSON e SQLite.

## Requisitos

- Python 3.10+

## Instalação

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Como executar

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: http://localhost:8000

## Estrutura do Projeto

```
app/
├── __init__.py
├── main.py                 # Aplicação FastAPI principal
├── models.py               # Modelos Pydantic
├── dp.py                   # Inicialização do banco de dados
├── storage.py              # Persistência JSON
├── storage_sqlite.py       # Persistência SQLite
└── routes/
    ├── __init__.py
    └── series.py           # Endpoints da API
data/
├── series.json             # Armazenamento JSON
└── series.db               # Banco SQLite (gerado em runtime)
```

## Endpoints

- `GET /` - Mensagem de boas-vindas
- `POST /series` - Criar nova série
- `GET /series` - Listar todas as séries
- `GET /series/{titulo}` - Buscar série por título

## Exemplo de uso

Criar uma série:
```bash
curl -X POST "http://localhost:8000/series" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Breaking Bad",
    "genero": "Drama",
    "ano_lancamento": 2008,
    "temporadas": 5
  }'
```

Listar séries:
```bash
curl "http://localhost:8000/series"
```
