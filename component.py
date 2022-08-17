from pathlib import Path

from _types.settings import Settings


class ComponentCreator:
    def __init__(self, settings: Settings) -> None:
        self._folder_path = Path.cwd()
        self._names = settings.names
        self._extension = settings.component_extension
        self._is_folder = settings.is_folder
        self._styles = settings.styles

    def create(self):
        if self._is_folder:
            self._create_folder_component()
        else:
            self._create_file_component()

    def _create_folder_component(self):
        for name in self._names:
            self._folder_path = Path(self._folder_path / name)
            Path.mkdir(self._folder_path)
            self._write(f"index.{self._extension}", name)
            self._create_files(name)

    def _create_file_component(self):
        for name in self._names:
            self._create_files(name)

    def _create_files(self, name):
        if self._styles is not None:
            Path.touch(
                Path(
                    self._folder_path
                    / f"{name}{self._styles.suffix}.{self._styles.file_extension}"
                )
            )
            file = f"{name}.{self._extension}"
            self._write(file, name)

    def _write(self, file, name_component):
        pass
