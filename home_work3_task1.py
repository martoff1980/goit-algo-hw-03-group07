from pathlib import Path
from shutil import copy2
from sys import argv
import os


def display_tree(path: Path, dist):
    if not Path(dist).exists():
        Path.mkdir(dist)

    if not Path(f"{dist}\\ANOTHER\\").exists():
        Path.mkdir(f"{dist}\\ANOTHER\\")

    if path.is_file():
        if path.name.rfind(".") == -1:
            full_name2 = f"{dist}\\ANOTHER\\"

        if path.name.rfind(".") != -1:
            dir_name2 = path.name[path.name.rfind(".")+1:].upper()
            full_name2 = f"{dist}\\{dir_name2}"

        if not Path(full_name2).exists():
            Path.mkdir(full_name2)

        if not Path(f"{full_name2}\\{path.name}").exists():
            copy2(path, f"{full_name2}\\{path.name}")

    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, dist)


if __name__ == "__main__":
    root = Path(argv[1])
    if len(argv) == 2:
        dist = Path(f"{os.getcwd()}\\dist")
    if len(argv) == 3:
        dist = argv[2]

    display_tree(root, dist)
