
import os

def create_numbered_folder(base_dir, folder_name):
    """
    Creates a numbered folder with the given name.

    Args:
        base_dir: The directory where the folder should be created.
        folder_name: The base name of the folder.

    Returns:
        The path to the created folder.
    """

    i = 1
    while True:
        numbered_folder_name = f"{folder_name} ({i})"
        numbered_folder_path = os.path.join(base_dir, numbered_folder_name)
        if not os.path.exists(numbered_folder_path):
            os.makedirs(numbered_folder_path)
            return numbered_folder_path
        i += 1

# Usage:
base_dir = os.path.dirname(__file__)  # Get the directory of the current script
folder_name = "fitbit-app-architecture"
numbered_folder_path = create_numbered_folder(base_dir, folder_name)

# create the folder structure inside the numbered folder
create_folder_structure(numbered_folder_path)

