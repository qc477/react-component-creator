from dataclasses import dataclass

from _types.aliases import (
    EmptyString,
    FileExtension,
    NameComponent,
    NumberOfSpaces,
    Quote,
    Semi,
    Suffix,
)


@dataclass(slots=True, frozen=True)
class StyleSettings:
    suffix: Suffix | EmptyString
    extension: FileExtension | None


@dataclass(slots=True, frozen=True)
class Settings:
    names: list[NameComponent]
    is_folder: bool
    extension: FileExtension
    tab_width: NumberOfSpaces
    semi: Semi | EmptyString
    quote: Quote
    styles: StyleSettings | None
