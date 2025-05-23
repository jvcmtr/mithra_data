import os
import json

def write_file(path, data):
    """
    Write data to a JSON file at the specified path.
    Creates directories if they don't exist.
    Args:
        path (str): The file path where JSON will be written.
        data (any): The data to write as JSON.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)  # Ensure directory exists
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def read_file(path):
    """
    Read and return JSON data from the specified file path.
    Args:
        path (str): The file path to read JSON from.
    Returns:
        any: The data loaded from the JSON file.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    

def read_as(path, cls):
    """
    Read JSON data from a file and construct an instance of the provided class.

    Args:
        path (str): The path to the JSON file.
        cls (type): The class to instantiate.

    Returns:
        An instance of that data-class populated with data from the JSON.
    """
    data = read_file(path)
    return cls(**data)