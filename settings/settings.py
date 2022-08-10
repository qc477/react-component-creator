"""
Тестовая часть программы
"""
from _types.arguments import Arguments
from commands.arguments import get_arguments


def get():
    args = get_arguments()
    settings = _parse_args(args)
    print(settings)


# TODO: рефакторинг
def _parse_args(args: Arguments):
    if args.component.is_tsx:
        extension = "tsx"
    else:
        extension = "jsx"

    if args.prettier.is_semi:
        semi = ";"
    else:
        semi = ""

    if args.prettier.is_single_quote:
        quote = "'"
    else:
        quote = '"'

    # TODO: доделать валидацию стилей
    suffix = ""
    style_extension = "css"
    if any(args.stylesheet.extensions):
        if args.stylesheet.is_module:
            suffix = ".module"

        for key, value in args.stylesheet.extensions._asdict().items():
            if value:
                style_extension = key
                break

    settings = {
        "names": args.component.names,
        "is_folder": args.component.is_folder,
        "extension": extension,
        "tab_width": args.prettier.tab_width,
        "semi": semi,
        "quote": quote,
        "stylesheet": {"suffix": suffix, "extension": style_extension},
    }
    return settings
