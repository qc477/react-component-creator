from pathlib import Path

from _types.settings import Settings


class ComponentCreator:
    def __init__(self, settings: Settings) -> None:
        self._folder_path = Path.cwd()
        self._component_names = settings.names
        self._extension = settings.extension
        self._is_folder = settings.is_folder
        self._styles = settings.styles

    def create(self):
        if self._is_folder:
            self._create_folder_component()
        else:
            self._create_file_component()

    def _create_folder_component(self):
        index_file = f"index.{self._extension}"
        for component_name in self._component_names:
            self._create_folder(component_name)
            self._write(index_file, component_name)
            self._create_files(component_name)

    def _create_folder(self, component_name):
        folder_name = component_name
        self._folder_path = Path(Path.cwd() / folder_name)
        Path.mkdir(self._folder_path)

    def _create_file_component(self):
        for component_name in self._component_names:
            self._create_files(component_name)

    def _create_files(self, component_name):
        if self._styles is not None:
            name_of_styles_file = (
                f"{component_name}{self._styles.suffix}.{self._styles.extension}"
            )
            Path.touch(Path(self._folder_path / name_of_styles_file))
            file = f"{component_name}.{self._extension}"
            self._write(file, component_name)

    def _write(self, file, component_name):
        pass
