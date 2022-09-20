from os import path
from pathlib import Path


def print_info(_path: Path):
    if _path.is_dir():
        print(f"OK: directory '{_path.name}'")
    else:
        directory = path.basename(path.split(_path.as_posix())[0])
        print(f"OK: '{path.join(directory, _path.name)}'")
