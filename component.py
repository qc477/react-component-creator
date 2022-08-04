from pathlib import Path

from _types import CMDArguments


def create_component(args: CMDArguments) -> None:
    if args.is_folder:
        _create_folder_type_component(args)
    else:
        _write_file()  # ?


def _create_folder_type_component(args):
    pass


# TODO: уточнить тип для content
def _write_file(filepath: Path, content: str) -> None:
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)
