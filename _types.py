from dataclasses import dataclass

NameComponent = str
TypeComponent = str
NumberOfSpaces = int


@dataclass(slots=True, frozen=True)
class CMDArguments:
    names: list[NameComponent]
    extension: TypeComponent
    is_folder: bool
    is_module: bool
    tab_width: NumberOfSpaces
    is_semi: bool
    is_single_quote: bool
    is_css: bool
    is_scss: bool
    is_sass: bool
    is_less: bool
