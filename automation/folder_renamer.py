# This script automates the renaming of numeric folders
# to a standardized format (e.g., 1 -> unit-01).
# It helps to maintain proper sorting in file managers.

import os


def rename_folders(base_path):
    if not os.path.exists(base_path):
        return

    os.chdir(base_path)
    for folder_name in os.listdir("."):
        # Check if it's a directory and the name is a number
        if os.path.isdir(folder_name) and folder_name.isdigit():
            # Format the new name with a prefix and leading zero
            new_name = f"unit-{int(folder_name):02d}"
            os.rename(folder_name, new_name)
            print(f"Rename in {base_path}: {folder_name} -> {new_name} ")


if __name__ == "__main__":
    paths = [
        "/home/me/my_it/english-learning-roadmap/materials/part-1/audio",
        "/home/me/my_it/english-learning-roadmap/materials/part-2/audio",
    ]

    for path in paths:
        rename_folders(path)
