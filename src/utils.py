import json
import os
from decimal import Decimal
import datetime

def load_config(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _json_default(o):
    if isinstance(o, Decimal):
        return float(o)
    if isinstance(o, (datetime.date, datetime.datetime, datetime.time)):
        return o.isoformat()
    return str(o)

def save_to_json(data, filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=_json_default)
