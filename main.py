from pathlib import Path
import os


def copy():
    source_path = Path.joinpath(Path.home(), "AppData", "Local", "Packages",
                                "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy", "LocalState", "Assets")
    print(Path.home())
    target_path = Path().cwd()
    file_pattern = "*.*"
    for obj in source_path.iterdir():
        if obj.is_file():
            obj.rename(target_path / obj.name)


copy()
