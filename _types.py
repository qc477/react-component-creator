from dataclasses import dataclass
from typing import NamedTuple, TypeAlias

NameComponent: TypeAlias = str
ComponentTemplate: TypeAlias = str
NumberOfSpaces: TypeAlias = int
EmptyString: TypeAlias = str


class StyleSheetTemplate(NamedTuple):
    is_css: bool
    is_scss: bool
    is_sass: bool
    is_less: bool


@dataclass(slots=True, frozen=True)
class Prettier:
    tab_width: NumberOfSpaces
    is_semi: bool
    is_single_quote: bool


@dataclass(slots=True, frozen=True)
class StyleSheet:
    is_module: bool
    template: StyleSheetTemplate


@dataclass(slots=True, frozen=True)
class CMDArguments:
    names: list[NameComponent]
    template: ComponentTemplate
    is_folder: bool
    prettier: Prettier
    stylesheet: StyleSheet
