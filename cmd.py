from dataclasses import dataclass
from argparse import ArgumentParser

NameComponent = str


@dataclass(slots=True, frozen=True)
class CMDArguments:
    names: list[NameComponent]
    typescript: bool
    module: bool
    css: bool
    scss: bool
    sass: bool
    less: bool


def get_command_line_arguments() -> CMDArguments:
    args = _create_argument_parser()
    return CMDArguments(
        names=args.names,
        typescript=args.typescript,
        module=args.module,
        css=args.css,
        scss=args.scss,
        sass=args.sass,
        less=args.less,
    )


def _create_argument_parser():
    parser = ArgumentParser(description="Bash script for creating React components.")
    group = parser.add_mutually_exclusive_group()
    _configure_arguments(parser, group)
    return parser.parse_args()


def _configure_arguments(parser, group):
    parser.add_argument("names", nargs="+", help="Name[s] of React components.")
    parser.add_argument(
        "-t", "--typescript", help="Create a TypeScript component.", action="store_true"
    )
    parser.add_argument(
        "-m", "--module", help="Use module stylesheets.", action="store_true"
    )
    group.add_argument("-c", "--css", help="Use CSS.", action="store_true")
    group.add_argument("-s", "--scss", help="Use SCSS.", action="store_true")
    group.add_argument("-a", "--sass", help="Use SASS.", action="store_true")
    group.add_argument("-l", "--less", help="Use LESS.", action="store_true")


if __name__ == "__main__":
    print(get_command_line_arguments())
