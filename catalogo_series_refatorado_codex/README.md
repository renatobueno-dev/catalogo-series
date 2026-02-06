# Solicitação de Refatoração
- Para eu ver como um **suposto** desenvolvedor de back-end Python faria a organização e estrutura do projeto.

## Refatoração realizada

- Separação em dois apps totalmente independentes (JSON e SQLite) sem dependências cruzadas.
- Padronização de docstrings e camadas (models, repositories, services, routes).
- Requisitos mínimos por app (`fastapi`, `uvicorn`) e dados localizados em `data/`.
- Adição de guardas para falhar cedo se backend incorreto for acoplado.

## Catálogo de Séries – Apps Separados

Este repositório contém duas versões independentes do catálogo de séries em FastAPI:

- `app_em_json/`: persistência em arquivo JSON.
- `app_em_sqlite/`: persistência em banco SQLite.

## Requisitos

- Python 3.10+

Cada app possui seu próprio `requirements.txt` com apenas:

```
fastapi
uvicorn
```

Instale os requisitos dentro do diretório de cada app:

```
cd app_em_json   # ou app_em_sqlite
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Como executar

JSON:

```
cd app_em_json
uvicorn app.main:app --reload
```

SQLite:

```
cd app_em_sqlite
uvicorn app.main:app --reload
```


## Estrutura

Cada app possui:

- `app/models/` – modelos Pydantic.
- `app/repositories/` – camada de persistência (exclusiva do backend escolhido).
- `app/services/` – regras de negócio simples.
- `app/routes/` – endpoints FastAPI.
- `data/` – arquivo de dados (`series.json` ou `series.db`).

```
app_em_json/
├── requirements.txt             # fastapi, uvicorn (minimal)
├── app/
│   ├── main.py                  # FastAPI setup
│   ├── models/
│   │   └── serie.py             # Pydantic models
│   ├── repositories/
│   │   └── series_json.py       # JSON storage logic
│   ├── services/
│   │   └── series.py            # Business logic
│   ├── routes/
│   │   └── series.py            # API endpoints
│   └── __pycache__/
└── data/
    └── series.json              # JSON data
```

```
app_em_sqlite/
├── requirements.txt             # fastapi, uvicorn (minimal)
├── app/
│   ├── main.py                  # FastAPI setup
│   ├── models/
│   │   └── serie.py             # Pydantic models
│   ├── repositories/
│   │   ├── db.py                # SQLite connection
│   │   └── series_sqlite.py     # SQLite storage logic
│   ├── services/
│   │   └── series.py            # Business logic
│   ├── routes/
│   │   └── series.py            # API endpoints
│   └── __pycache__/
└── data/                        # Empty (DB created at runtime)
```
## Boas práticas adotadas

- Backends isolados sem imports cruzados.
- Guardas simples em `repositories/__init__.py` para detectar backend errado.
- `.gitignore` inclui artefatos locais (cache, venv, IDE, logs).

## Autoria

Refatoração e documentação assistidas por IA (ChatGPT/Codex) para fins educacionais.
