from config import SettingsConfig, StyleFileConfig
from _types.aliases import EmptyString, FileExtension, Quote, Semi
from _types.arguments import Arguments
from _types.settings import Settings, StyleSettings
from _types.styles import Styles, StyleExtensions


def parse_arguments(args: Arguments) -> Settings:
    semi = _get_semi(args.prettier.is_semi)
    quote = _get_quote(args.prettier.is_single_quote)
    styles = _get_style_settings(args.styles)
    tab = " " * args.prettier.tab_width
    return Settings(
        component=args.component,
        tab=tab,
        semi=semi,
        quote=quote,
        styles=styles,
    )


def _get_semi(is_semi: bool) -> Semi | EmptyString:
    if is_semi:
        return SettingsConfig.SEMI
    return ""


def _get_quote(is_single_quote: bool) -> Quote:
    if is_single_quote:
        return SettingsConfig.SINGLE_QUOTE
    return SettingsConfig.DOUBLE_QUOTE


def _get_style_settings(style_args: Styles) -> StyleSettings | None:
    if style_args.is_module and not any(style_args.extensions):
        return StyleSettings(
            suffix=StyleFileConfig.SUFFIX, extension=StyleFileConfig.DEFAULT_EXTENSION
        )
    elif style_args.is_module and any(style_args.extensions):
        return StyleSettings(
            suffix=StyleFileConfig.SUFFIX,
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
