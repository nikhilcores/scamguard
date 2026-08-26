from pathlib import Path


def read_message(file_path):
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8").strip()
