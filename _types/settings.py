from dataclasses import dataclass

from _types.aliases import (
    EmptyString,
    FileExtension,
    Tab,
    Quote,
    Semi,
    Suffix,
)
from _types.component import Component


@dataclass(slots=True, frozen=True)
class StyleSettings:
    suffix: Suffix | EmptyString
    extension: FileExtension | None


@dataclass(slots=True, frozen=True)
class Settings:
    component: Component
    tab: Tab
    semi: Semi | EmptyString
    quote: Quote
    styles: StyleSettings | None
