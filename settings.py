import json

from pathlib import Path
from exceptions import SettingsFileNotFound


def get_settings():
    # with open(Path.cwd() / ".ccomponentsrc", "r") as file:
    #     data = json.loads(file.read())
    # print(data['format'])
    path_to_project_folder = _get_path_to_project_folder()
    file_settings = _get_file_settings(path_to_project_folder)
    print(file_settings)


def _get_path_to_project_folder():
    return str(Path.cwd()).split("/src")[0]


def _get_file_settings(path):
    target = Path(path) / ".ccomponentsrc"
    if Path.is_file(target):
        return str(target)
    raise SettingsFileNotFound


if __name__ == "__main__":
    get_settings()
