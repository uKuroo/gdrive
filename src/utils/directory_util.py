from pathlib import Path

def exists_directory(directory):
    path = Path(directory)

    if Path.exists(path) and path.is_dir():
        return True
    return False