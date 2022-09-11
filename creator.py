import templates

from pathlib import Path
from _types.aliases import NameComponent, FileContent
from _types.settings import Settings


class Creator:
    def __init__(self, settings: Settings) -> None:
        self._cwd = Path.cwd()
        self._component_names = settings.names
        self._extension = settings.extension
        self._is_folder = settings.is_folder
        self._tab_width = settings.tab_width
        self._semi = settings.semi
        self._quote = settings.quote
        self._styles = settings.styles

    def create_components(self):
        if self._is_folder:
            self._create_folder_component()
        else:
            self._create_file_component()

    def _create_folder_component(self):
        for name in self._component_names:
            path_component_folder = Path(self._cwd / name)
            Path.mkdir(path_component_folder)
            self._create_files(
                path=path_component_folder, name=name, is_index_file=True
            )

    def _create_file_component(self):
        pass

    def _create_files(
        self, path: Path, name: NameComponent, is_index_file: bool = False
    ):
        if self._styles is not None:
            Path.touch(path / f"{name}{self._styles.suffix}.{self._styles.extension}")
        if is_index_file:
            path_index_file = Path(path / f"index.{self._extension}")
            contens_file_index = templates.INDEX_FILE.format(
                name=name, quote=self._quote, semi=self._semi
            )
            self._write_file(filepath=path_index_file, content=contens_file_index)

    def _write_file(self, filepath: Path, content: FileContent):
        with open(filepath, "w") as file:
            file.write(content)
