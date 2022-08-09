from argparse import ArgumentParser, BooleanOptionalAction

_PARSER = ArgumentParser(
    prog="ccomponents", description="Console utility for creating React components."
)


def get_arguments():
    _set_groups()
    return _PARSER.parse_args()


def _set_groups():
    _set_react_group()
    _set_prettier_group()
    _set_stylesheet_group()


def _set_react_group():
    react_group = _PARSER.add_argument_group("Settings of the React component.")
    exclusive_react_group = react_group.add_mutually_exclusive_group()
    _set_react_arguments(react_group, exclusive_react_group)


def _set_react_arguments(group, exclusive_group):
    group.add_argument("names", nargs="+")
    group.add_argument("-f", "--folder", action="store_true")
    exclusive_group.add_argument("--jsx", action="store_true")
    exclusive_group.add_argument("--tsx", action="store_true")


def _set_prettier_group():
    prettier_group = _PARSER.add_argument_group("Prettier settings.")
    _set_prettier_arguments(prettier_group)


def _set_prettier_arguments(group):
    group.add_argument("-t", "--tab-width", type=int, default=2)
    group.add_argument("--semi", action=BooleanOptionalAction, default=True)
    group.add_argument("-s", "--single-quote", action="store_true")


def _set_stylesheet_group():
    stylesheet_group = _PARSER.add_argument_group("StyleSheet Settings.")
    exclusive_stylesheet_group = stylesheet_group.add_mutually_exclusive_group()
    _set_stylesheet_arguments(stylesheet_group, exclusive_stylesheet_group)


def _set_stylesheet_arguments(group, exclusive_group):
    group.add_argument("-m", "--module", action="store_true")
    exclusive_group.add_argument("--css", action="store_true")
    exclusive_group.add_argument("--scss", action="store_true")
    exclusive_group.add_argument("--sass", action="store_true")
    exclusive_group.add_argument("--less", action="store_true")
