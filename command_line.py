from argparse import (
    ArgumentParser,
    BooleanOptionalAction,
    _ArgumentGroup,
    _MutuallyExclusiveGroup,
)

from _types.arguments import Arguments
from _types.component import Component
from _types.prettier import Prettier
from _types.styles import Styles, StyleExtensions

_PARSER = ArgumentParser(
    prog="ccomponents", description="Console utility for creating React components."
)


def get_arguments() -> Arguments:
    _set_groups()
    args = _PARSER.parse_args()
    return Arguments(
        component=Component(names=args.names, is_folder=args.folder, is_tsx=args.tsx),
        prettier=Prettier(
            tab_width=args.tab_width,
            is_semi=args.semi,
            is_single_quote=args.single_quote,
        ),
        styles=Styles(
            is_module=args.module,
            extensions=StyleExtensions(
                css=args.css, scss=args.scss, sass=args.sass, less=args.less
            ),
        ),
    )


def _set_groups() -> None:
    _set_react_group()
    _set_prettier_group()
    _set_stylesheet_group()


def _set_react_group() -> None:
    react_group = _PARSER.add_argument_group("Settings of the React component.")
    _set_react_arguments(react_group)


def _set_react_arguments(group: _ArgumentGroup) -> None:
    group.add_argument("names", nargs="+")
    group.add_argument("-f", "--folder", action="store_true")
    group.add_argument("--tsx", action="store_true")


def _set_prettier_group() -> None:
    prettier_group = _PARSER.add_argument_group("Prettier settings.")
    _set_prettier_arguments(prettier_group)


def _set_prettier_arguments(group: _ArgumentGroup) -> None:
    group.add_argument("-t", "--tab-width", type=int, default=2)
    group.add_argument("--semi", action=BooleanOptionalAction, default=True)
    group.add_argument("-s", "--single-quote", action="store_true")


def _set_stylesheet_group() -> None:
    stylesheet_group = _PARSER.add_argument_group("StyleSheet Settings.")
    exclusive_stylesheet_group = stylesheet_group.add_mutually_exclusive_group()
    _set_stylesheet_arguments(stylesheet_group, exclusive_stylesheet_group)


def _set_stylesheet_arguments(
    group: _ArgumentGroup, exclusive_group: _MutuallyExclusiveGroup
) -> None:
    group.add_argument("-m", "--module", action="store_true")
    exclusive_group.add_argument("--css", action="store_true")
    exclusive_group.add_argument("--scss", action="store_true")
    exclusive_group.add_argument("--sass", action="store_true")
    exclusive_group.add_argument("--less", action="store_true")
