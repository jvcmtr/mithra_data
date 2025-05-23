from pathlib import Path


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
