from pathlib import Path

from _types.settings import Settings


class Creator:
    def __init__(self, settings: Settings) -> None:
        self._folder_path = Path.cwd()
        self._component_names = settings.names
        self._extension = settings.extension
        self._is_folder = settings.is_folder
        self._styles = settings.styles

    def run(self):
        if self._is_folder:
            self._create_folder_component()
        else:
            self._create_file_component()

    def _create_folder_component(self):
        pass

    def _create_file_component(self):
        pass
