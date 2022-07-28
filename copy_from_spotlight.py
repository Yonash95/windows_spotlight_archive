from pathlib import Path
from shutil import copytree


def copy():
    """ This funcion only let you move files on one drive"""

    source_path = Path.joinpath(Path.home(), "AppData", "Local", "Packages",
                                "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy", "LocalState", "Assets")
    target_path = Path.joinpath(Path().cwd(), 'img')
    new_suffix = ".jpg"
    input("Files will be copied from source directory to 'img' directory, created in place where script was started. "
          "Press any button to continue.")
    copytree(source_path, target_path, dirs_exist_ok=True)  # copy first so original files remain intact
    for i, obj in enumerate(target_path.iterdir()):
        if obj.is_file():
            new_name = f"img_{i}{new_suffix}"
            print(new_name, " created")
            obj.rename(target_path / new_name)
    input("Now you can select images you like, move them wherever you want and delete everything from 'img "
          "folder. Press any button to end.")


copy()
