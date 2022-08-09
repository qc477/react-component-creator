from argparse import ArgumentParser

from _types.cmd_arguments import CMDArguments
from _types.prettier import Prettier
from _types.style_sheet import StyleSheet


def get_command_line_arguments() -> CMDArguments:
    args = _create_argument_parser()
    return CMDArguments(
        names=args.names,
        template=args.template,
        is_folder=args.folder,
        prettier=Prettier(
            tab_width=args.tab_width,
            is_semi=args.semi,
            is_single_quote=args.single_quote,
        ),
        stylesheet=StyleSheet(is_module=args.module, template=args.style),
    )


def _create_argument_parser():
    parser = ArgumentParser(description="Bash script for creating React components.")
    _configure_arguments(parser)
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
        "-tw", "--tab-width", type=int, default=2, choices=[2, 4], help="Tab Width."
    )
    parser.add_argument("-s", "--semi", action="store_true", help="Use a semicolon.")
    parser.add_argument(
        "-sq", "--single-quote", action="store_true", help="Use single quotes."
    )
    parser.add_argument(
        "-st",
        "--style",
        type=str,
        choices=["css", "scss", "sass", "less"],
        help="Type stylesheet.",
    )
