from dataclasses import dataclass
from argparse import ArgumentParser

NameComponent = str
TypeComponent = str
NumberOfSpaces = int


@dataclass(slots=True, frozen=True)
class CMDArguments:
    names: list[NameComponent]
    extension: TypeComponent
    is_file: bool
    is_folder: bool
    is_module: bool
    tab_width: NumberOfSpaces
    is_semi: bool
    is_single_quote: bool
    is_css: bool
    is_scss: bool
    is_sass: bool
    is_less: bool


def get_command_line_arguments() -> CMDArguments:
    args = _create_argument_parser()
    return CMDArguments(
        names=args.names,
        extension=args.extension,
        is_file=args.file,
        is_folder=args.folder,
        is_module=args.module,
        tab_width=args.tab_width,
        is_semi=args.semi,
        is_single_quote=args.single_quote,
        is_css=args.css,
        is_scss=args.scss,
        is_sass=args.sass,
        is_less=args.less,
    )


def _create_argument_parser():
    parser = ArgumentParser(description="Bash script for creating React components.")
    _configure_arguments(parser)
    _configure_group_arguments(parser)
    return parser.parse_args()


def _configure_arguments(parser):
    parser.add_argument("names", nargs="+", help="Name[s] of React components.")
    parser.add_argument(
        "-e",
        "--extension",
        type=str,
        choices=["js", "ts", "jsx", "tsx"],
        default="jsx",
        help="Type of React component.",
    )
    parser.add_argument(
        "-m", "--module", action="store_true", help="Use module stylesheets."
    )
    parser.add_argument(
        "-t", "--tab-width", type=int, default=2, choices=[2, 4], help="Tab Width."
    )
    parser.add_argument("-s", "--semi", action="store_true", help="Use a semicolon.")
    parser.add_argument(
        "-S", "--single-quote", action="store_true", help="Use single quotes."
    )


def _configure_group_arguments(parser):
    file_or_folder = parser.add_mutually_exclusive_group()
    stylesheets = parser.add_mutually_exclusive_group()
    file_or_folder.add_argument(
        "-f", "--file", action="store_true", help="Make a component a file."
    )
    file_or_folder.add_argument(
        "-F", "--folder", action="store_true", help="Make a component a folder."
    )
    stylesheets.add_argument("--css", action="store_true", help="Create a CSS file")
    stylesheets.add_argument("--scss", action="store_true", help="Create a SCSS file")
    stylesheets.add_argument("--sass", action="store_true", help="Create a SASS file")
    stylesheets.add_argument("--less", action="store_true", help="Create a LESS file")
