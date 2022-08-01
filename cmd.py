from dataclasses import dataclass
from argparse import ArgumentParser

NameComponent = str


@dataclass(slots=True, frozen=True)
class CMDArguments:
    names: list[NameComponent]


def get_command_line_arguments() -> CMDArguments:
    args = _create_argument_parser()
    return CMDArguments(names=args.names)


def _create_argument_parser():
    parser = ArgumentParser(description="Bash script for creating React components.")
    _configure_arguments(parser)
    return parser.parse_args()


def _configure_arguments(parser):
    parser.add_argument("names", nargs="+", help="Name[s] of React components.")


if __name__ == "__main__":
    print(get_command_line_arguments())
