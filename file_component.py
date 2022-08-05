from pathlib import Path

from _types import CMDArguments, EmptyString


class CreatorFileComponent:
    def __init__(self, cmd_arguments: CMDArguments) -> None:
        self.names = cmd_arguments.names
        self.template = cmd_arguments.template
        self.prettier = cmd_arguments.prettier
        self.stylesheet = cmd_arguments.stylesheet

    def create(self) -> None:
        for name in self.names:
            component_filepath = Path.cwd() / f"{name}.{self.template}"
            stylesheet_filepath = Path.cwd() / self._get_stylescheet_file_name(name)
            print(component_filepath)
            print(stylesheet_filepath)

    def _get_stylescheet_file_name(self, name) -> str:
        suffix = self._get_stylesheet_suffix()
        extension = self._get_stylescheet_file_extension()
        return f"{name}.{suffix}.{extension}"

    def _get_stylesheet_suffix(self) -> str | EmptyString:
        if self.stylesheet.is_module:
            return "module"
        return ""

    def _get_stylescheet_file_extension(self) -> str | EmptyString:
        pass

    def _write_file(self, file_path: Path, content) -> None:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
