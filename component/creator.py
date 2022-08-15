"""
__version__: alpha
"""
from pathlib import Path

from _types.aliases import FileExtension, FileName, FolderName
from _types.settings import Settings


class Creator:
    def __init__(self, settings: Settings) -> None:
        self._names = settings.names
        self._is_folder = settings.is_folder
        self._component_extension = settings.component_extension
        self._tab_width = settings.tab_width
        self._semi = settings.semi
        self._quote = settings.quote
        self._styles = settings.styles
        self._path_to_folder: Path = Path.cwd()

    def start(self) -> None:
        if self._is_folder:
            print("folder")
            exit(1)
        else:
            self._create_file_component()

    def _create_file_component(self) -> None:
        for name in self._names:
            self._create_and_write_file(name, self._component_extension)

    def _create_and_write_file(
        self, name: FileName, extension: FileExtension, content: str = ""
    ) -> None:
        with open(
            Path(self._path_to_folder / f"{name}.{extension}"), "w", encoding="utf-8"
        ) as file:
            file.write(content)
