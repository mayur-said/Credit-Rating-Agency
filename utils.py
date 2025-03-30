import json


def read_json_file(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        return json.load(f)
    

def process_error_response(title: str, errors: dict) -> dict:
    return {"error": True, "message": {"title": title, "details": errors}}