from pathlib import Path

from config import ContentConfig, ComponentConfig
from _types.aliases import (
    DeclaringFunctionalComponent,
    EmptyString,
    FileExtension,
    FileName,
    NameComponent,
    FileContent,
    StyleImportRow,
)
from _types.settings import Settings


class Creator:
    def __init__(self, settings: Settings) -> None:
        self._component_names = settings.component.names
        self._is_folder = settings.component.is_folder
        self._is_typescript = settings.component.is_typescript
        self._tab = settings.tab
        self._semi = settings.semi
        self._quote = settings.quote
        self._styles = settings.styles
        self._cwd = Path.cwd()
        self._component_extension: FileExtension = (
            ComponentConfig.JAVASCRIPTREACT_EXTENSION
        )
        self._declaring_functional_component: DeclaringFunctionalComponent | EmptyString = (
            ""
        )
        self._style_import_row: StyleImportRow | EmptyString = ""
        self._name_styles_file: FileName | None = None

    def create(self) -> None:
        if self._is_folder:
            self._make_folder_component()
        else:
            self._make_file_component()

    def _make_folder_component(self) -> None:
        for name in self._component_names:
            path_component_folder = Path(self._cwd / name)
            self._create_folder(path=path_component_folder, name=name)

    def _make_file_component(self) -> None:
        for name in self._component_names:
            self._create_files(path=self._cwd, name=name)

    def _create_folder(self, path: Path, name: NameComponent) -> None:
        Path.mkdir(path)
        self._create_files(path=path, name=name, is_index=True)

    def _create_files(self, path: Path, name: NameComponent, is_index: bool = False):
        self._write_file_component(path, name)
        if self._name_styles_file is not None:
            Path.touch(path / self._name_styles_file)
        if is_index:
            self._write_index_file(path, name)

    def _write_file_component(self, path: Path, name: NameComponent) -> None:
        self._check_component_extension()
        self._check_styles(name)
        path_component_file = Path(path / f"{name}.{self._component_extension}")
        component_content = ContentConfig.COMPONENT_TEMPLATE.format(
            name=name,
            style_import_row=self._style_import_row,
            declaring_functional_component=self._declaring_functional_component,
            tab=self._tab,
            semi=self._semi,
            quote=self._quote,
        )
        self._write_file(filepath=path_component_file, content=component_content)

    def _write_index_file(self, path: Path, name: NameComponent) -> None:
        path_index_file = Path(path / f"index.{self._component_extension}")
        contents_file_index = ContentConfig.TEMPLATE_FILE_INDEX.format(
            name=name, quote=self._quote, semi=self._semi
        )
        self._write_file(filepath=path_index_file, content=contents_file_index)

    def _check_component_extension(self) -> None:
        if self._is_typescript:
            self._set_component_extension()
            self._set_declaring_functional_component()

    def _check_styles(self, name: NameComponent) -> None:
        if self._styles is not None:
            self._name_styles_file = (
                f"{name}{self._styles.suffix}.{self._styles.extension}"
            )
            self._set_style_import_row()

    def _set_component_extension(self) -> None:
        self._component_extension = ComponentConfig.TYPESCRIPTREACT_EXTENSION

    def _set_declaring_functional_component(self) -> None:
        self._declaring_functional_component = (
            ContentConfig.DECLARING_FUNCTIONAL_COMPONENT
        )

    def _set_style_import_row(self) -> None:
        self._style_import_row = ContentConfig.STYLE_IMPORT_ROW.format(
            quote=self._quote, semi=self._semi, name_styles_file=self._name_styles_file
        )

    def _write_file(self, filepath: Path, content: FileContent):
        with open(filepath, "w") as file:
            file.write(content)
