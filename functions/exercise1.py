# Задача 1
from pathlib import Path


def count_files_in_dir(path=Path.cwd(), recurse=False) -> dict:
    files = 0
    folders = 0
    if recurse:
        for data in path.rglob('*'):
            if data.is_dir():
                folders += 1
            if data.is_file():
                files += 1
    else:
        for data in path.iterdir():
            if data.is_dir():
                folders += 1
            if data.is_file():
                files += 1

    result = {
        'files': files,
        'folders': folders
    }
    return result


test_path = Path('.')
print(count_files_in_dir(test_path, True))
