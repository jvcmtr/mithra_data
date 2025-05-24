
from pathlib import Path

# Created using AI

def read_file(path):
    """
    Reads a file from the given path using pathlib and returns its contents.
    Returns an empty string if the file does not exist or is not a file.

    :param path: str or Path - Path to the file
    :return: str - Contents of the file or empty string if not found
    """
    file_path = Path(path)

    if not file_path.is_file():
        return ""

    try:
        return file_path.read_text(encoding='utf-8')
    except (FileNotFoundError, IsADirectoryError, OSError):
        return ""

def foreach_subfolder(folder_path, func):
    """
    Applies a given lambda function to all subfolders in the provided folder path.

    Parameters:
    - folder_path (str or Path): Path to the main folder.
    - func (callable): A lambda or any callable that takes one argument (the subfolder Path object).
    """
    path = Path(folder_path)

    if not path.is_dir():
        raise ValueError(f"'{folder_path}' is not a valid directory.")

    for subfolder in path.iterdir():
        if subfolder.is_dir():
            func(subfolder)

