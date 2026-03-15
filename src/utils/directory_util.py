from pathlib import Path

def exists_directory(directory):
    path = Path(directory).expanduser()

    if Path.exists(path) and path.is_dir():
        return path.as_posix()
    return False