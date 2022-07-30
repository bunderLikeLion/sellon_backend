from pathlib import Path


def create_file_if_not_exists(path: str):
    file = Path(path)
    file.touch(exist_ok=True)
