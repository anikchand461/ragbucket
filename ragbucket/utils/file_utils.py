from pathlib import Path

def get_text_files(directory):
    path = Path(directory)
    return list(path.glob("*.txt"))
