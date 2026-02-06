import json
import os

DATA_FILE = "data/series.json"


def read_series():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def write_series(series_list):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(series_list, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}")