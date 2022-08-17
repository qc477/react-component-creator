from _types.aliases import EmptyString, FileExtension, Quote, Semi
from _types.arguments import Arguments
from _types.settings import Settings, StyleSettings
from _types.styles import Styles, StyleExtensions


def parse_arguments(args: Arguments) -> Settings:
    component_extension = _get_component_extension(args.component.is_tsx)
    semi = _get_semi(args.prettier.is_semi)
    quote = _get_quote(args.prettier.is_single_quote)
    styles = _get_style_settings(args.styles)
    return Settings(
        names=args.component.names,
        is_folder=args.component.is_folder,
        extension=component_extension,
        tab_width=args.prettier.tab_width,
        semi=semi,
        quote=quote,
        styles=styles,
    )


def _get_component_extension(is_tsx: bool) -> FileExtension:
    if is_tsx:
        return "tsx"
    return "jsx"


def _get_semi(is_semi: bool) -> Semi | EmptyString:
    if is_semi:
        return ";"
    return ""


def _get_quote(is_single_quote: bool) -> Quote:
    if is_single_quote:
        return "'"
    return '"'


def _get_style_settings(style_args: Styles) -> StyleSettings | None:
    if style_args.is_module and not any(style_args.extensions):
        return StyleSettings(suffix=".module", extension="css")
    elif style_args.is_module and any(style_args.extensions):
        return StyleSettings(
            suffix=".module",
            extension=_get_style_file_extension(style_args.extensions),
        )
    elif not style_args.is_module and any(style_args.extensions):
        return StyleSettings(
            suffix="",
            extension=_get_style_file_extension(style_args.extensions),
        )
    return None


def _get_style_file_extension(extensions: StyleExtensions) -> FileExtension | None:
    for key, value in extensions._asdict().items():
        if value:
            return key
