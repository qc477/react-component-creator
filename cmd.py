from argparse import ArgumentParser

from _types import CMDArguments, Prettier, StyleSheet, StyleSheetTemplate


def get_command_line_arguments() -> CMDArguments:
    args = _create_argument_parser()
    # TODO: сортировка стилей: нужны ли они вообще, если да, то какое расширение использовать
    return CMDArguments(
        names=args.names,
        template=args.template,
        is_folder=args.folder,
        prettier=Prettier(
            tab_width=args.tab_width,
            is_semi=args.semi,
            is_single_quote=args.single_quote,
        ),
        stylesheet=StyleSheet(
            is_module=args.module,
            template=StyleSheetTemplate(
                is_css=args.css,
                is_scss=args.scss,
                is_sass=args.sass,
                is_less=args.less,
            ),
        ),
    )


def _create_argument_parser():
    parser = ArgumentParser(description="Bash script for creating React components.")
    _configure_arguments(parser)
    _configure_group_arguments(parser)
    return parser.parse_args()


def _configure_arguments(parser):
    parser.add_argument("names", nargs="+", help="Name[s] of React components.")
    parser.add_argument(
        "-f", "--folder", action="store_true", help="Make a component a folder."
    )
    parser.add_argument(
        "-t",
        "--template",
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
    stylesheets = parser.add_mutually_exclusive_group()
    stylesheets.add_argument("--css", action="store_true", help="Create a CSS file")
    stylesheets.add_argument("--scss", action="store_true", help="Create a SCSS file")
    stylesheets.add_argument("--sass", action="store_true", help="Create a SASS file")
    stylesheets.add_argument("--less", action="store_true", help="Create a LESS file")
