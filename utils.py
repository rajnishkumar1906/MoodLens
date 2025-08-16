# utils.py
import json

def save_to_json(data, filename="results.json"):
    """Saves a Python dictionary or list to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

