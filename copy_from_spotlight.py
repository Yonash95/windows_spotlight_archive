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
    loop = True
    while loop:  # while loop so we can easily restart after exception
        try:
            copytree(source_path, target_path, dirs_exist_ok=True)  # copy first so original files remain intact
            for i, obj in enumerate(target_path.iterdir()):
                if obj.is_file():
                    new_name = f"img_{i}{new_suffix}"
                    obj.rename(target_path / new_name)
                    print(new_name, " created")
            input("Now you can select images you like, move them wherever you want and delete everything from 'img' "
                  "folder. Press any button to end.")
            loop = False
        except FileExistsError:
            input("Please, delete all files from 'img' folder. Press any button to continue.")


copy()
