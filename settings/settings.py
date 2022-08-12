"""
Тестовая часть программы
"""
from _types.aliases import FileExtension
from _types.arguments import Arguments
from _types.component import ReactExtensions
from _types.styles import StyleExtensions
from commands.arguments import get_arguments


def get():
    args = get_arguments()
    settings = _parse_args(args)
    print(settings)


# TODO: рефакторинг
def _parse_args(args: Arguments):
    react_file_extension = _get_file_extension(args.component.file_extensions)
    # if args.component.is_tsx:
    #     extension = "tsx"
    # else:
    #     extension = "jsx"
    #
    # if args.prettier.is_semi:
    #     semi = ";"
    # else:
    #     semi = ""
    #
    # if args.prettier.is_single_quote:
    #     quote = "'"
    # else:
    #     quote = '"'
    #
    # TODO: доделать валидацию стилей
    # suffix = ""
    # style_extension = None
    # stylesheet = False
    # if args.stylesheet.is_module and not any(args.stylesheet.extensions):
    #     suffix = ".module"
    #     style_extension = "css"
    #     stylesheet = {"suffix": suffix, "extension": style_extension}
    # elif args.stylesheet.is_module and any(args.stylesheet.extensions):
    #     suffix = ".module"
    #     for key, value in args.stylesheet.extensions._asdict().items():
    #         if value:
    #             style_extension = key
    #             break
    #     stylesheet = {"suffix": suffix, "extension": style_extension}
    # elif not args.stylesheet.is_module and any(args.stylesheet.extensions):
    #     for key, value in args.stylesheet.extensions._asdict().items():
    #         if value:
    #             style_extension = key
    #             break
    #     stylesheet = {"suffix": suffix, "extension": style_extension}
    #
    # settings = {
    #     "names": args.component.names,
    #     "is_folder": args.component.is_folder,
    #     "extension": extension,
    #     "tab_width": args.prettier.tab_width,
    #     "semi": semi,
    #     "quote": quote,
    #     "stylesheet": stylesheet,
    # }
    # return settings


def _get_file_extension(file_extensions: ReactExtensions | StyleExtensions) -> FileExtension | None:
    for key, value in file_extensions._asdict().items():
        if value:
            return key
