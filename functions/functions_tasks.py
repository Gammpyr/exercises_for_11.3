from pathlib import Path

def is_dir():
    pass


def is_file():
    pass


def count_file_in_dir(path=Path.cwd(), recurse=True) -> dict:
    files = 0
    folders = 0


    result = {
        'files': files,
        'folders': folders
    }
    return result


path_to_file = Path('/data')

print(Path.home())
print(Path.cwd().parent)
